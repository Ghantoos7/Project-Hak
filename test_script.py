import requests
import re

def openFile(file_name):

    with open(file_name, "r") as file1:
        name_list = []
        for f in file1:
            name_list.append(f.lower())
        return name_list
# method to open a file and store each line as an element in a list


def writeToFile(valid_list,file_name):

    with open(file_name, "w") as file:
        for valid in valid_list:
            file.write(valid + "\n")
# method to write to a file and store each element in the list in a line


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