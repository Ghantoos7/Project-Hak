import requests
import re


# This function opens a file and stores each line as an element in a list
def openFile(file_name):
    with open(file_name, "r") as file1:
        name_list = []
        for f in file1:
            name_list.append(f.lower())
        return name_list


# This function writes to a file and stores each element in the list in a line
def writeToFile(valid_list,file_name):

    with open(file_name, "w") as file:
        for valid in valid_list:
            file.write(valid + "\n")


# This function takes a URL as input and sends an HTTP GET request to the URL using the requests library.
# It then returns the response object containing the server's response to the request.
def openUrl(url):
    request = requests.get("https://" + url)
    return request


# This function takes a requests object as input and returns the text content of the response as a string.
def getHtml(request : requests):
    html = request.text
    return html


# This function takes an HTML string as input and uses a regular expression to find all href links in the HTML.
# It then returns a list of all href links found in the HTML.
def getHrefList(html):
    pattern = r'<(?:a|link|image|audio|video) href="(.+?)">'
    href_list = re.findall(pattern,html)
    return href_list


# This function takes a string as input and removes all trailing whitespace characters.
# It returns the modified string with the whitespace removed.
def removeSpace(str1):
    pattern = re.compile(r"\s.*$")
    str2 = pattern.sub("", str1)
    return str2


# This function takes a string as input and removes any query parameters (i.e., anything after a '?' character).
# It returns the modified string with the query parameters removed.
def removeQuestionMark(str1):
    pattern = re.compile(r"\?.*$")
    str2 = pattern.sub("", str1)
    return str2


# This function takes a string as input and removes any path parameters (i.e., anything after a '\' character).
# It returns the modified string with the path parameters removed.
def removePathParams(str1):
    pattern = re.compile(r"\\.*$")
    str2 = pattern.sub("", str1)
    return str2


# This function takes a list of hrefs and removes any query or path parameters before returning the cleaned links.
def validateLinks(href_list : list):
    links = []
    for href in href_list:
        link_removed_space = removeSpace(href)
        link_removed_question = removeQuestionMark(link_removed_space)
        link_removed_path = removePathParams(link_removed_question)
        links.append(link_removed_path)
    return links


# This function takes a list of links and sends a GET request to each link to check if the link is valid.
# If the link is valid (status code in range 200-299), the link is added to a list of valid links. 
def getValidLinks(links_list : list):
    valid_links = []
    for link in links_list:
        try:
            response = requests.get(link)
        except requests.exceptions.RequestException:
            continue
        except requests.exceptions.HTTPError:
            continue
        except requests.exceptions.MissingSchema:
            continue
        if (response.status_code in range(200,300)):
            valid_links.append(link)
    return valid_links


# This function takes a list of sub-domains and a domain name as input and sends a GET request to each sub-domain to check if the sub-domain is valid.
# If the sub-domain is valid (status code in range 200-299), the sub-domain is added to a list of valid sub-domains.
def getValidSubDomains(sub_domains_list,url):
    valid_domains = []
    for sub_domain in sub_domains_list:
        try:
            request = requests.get("https://" + sub_domain + '.' + url)
        except requests.exceptions.RequestException:
            continue
        except requests.exceptions.HTTPError:
            continue
        except requests.exceptions.MissingSchema:
            continue
        status_code = request.status_code
        
        if (status_code in range(200,300)):
            valid_domains.append("https://" +sub_domain + "." + url)

    return valid_domains


# This function takes a list of directories and a domain name as input and sends a GET request to each directory to check if the directory is valid.
# If the directory is valid (status code in range 200-207), it is added to a list of valid directories.
def getValidDirectories(dirs_list,url):
    valid_directories = []
    for directory in dirs_list:
        try:
            request = requests.get(url + "/" + directory)
        except requests.exceptions.RequestException:
            continue
        except requests.exceptions.HTTPError:
            continue
        except requests.exceptions.MissingSchema:
            continue
        status_code = request.status_code
        if (status_code in range(200,300)):
            valid_directories.append(url + "/" + directory )

    return valid_directories 
