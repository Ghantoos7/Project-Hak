# Project Report

## Introduction

This report outlines the steps taken to complete a project, which involved writing Python code to validate links on a website. The project required the use of regular expressions, HTTP requests, and Python libraries such as Requests.

## Code Overview
The code consists of several functions, each of which is responsible for performing a specific task. The ```openFile``` function reads a file and stores each line as an element in a list. The ```writeToFile``` function writes the contents of a list to a file. The ```openUrl``` function sends an HTTP GET request to a URL using the Requests library and returns the response object containing the server's response. The ```getHtml``` function takes a Requests object as input and returns the text content of the response as a string. The ```getHrefList``` function uses a regular expression to find all href links in an HTML string and returns a list of all href links found in the HTML. The ```removeSpace```, ```removeQuestionMark```, and ```removePathParams``` functions are used to remove trailing whitespace characters, query parameters, and path parameters from a URL string, respectively. The ```validateLinks``` function takes a list of hrefs and removes any query or path parameters before returning the cleaned links. The ```getValidLinks function``` sends a GET request to each link in a list of links to check if the link is valid. If the link is valid (status code in range 200-299), the link is added to a list of valid links. The ```getValidLinksList``` function calls ```getHrefList```, ```validateLinks```, and ```getValidLinks``` to get a list of valid links for a given URL. The ```getValidSubDomains``` function sends a GET request to each sub-domain in a list of sub-domains to check if the sub-domain is valid. If the sub-domain is valid (status code in range 200-299), the sub-domain is added to a list of valid sub-domains. The ```getValidDirectories``` function sends a GET request to each directory in a list of directories to check if the directory is valid. If the directory is valid (status code in range 200-207), it is added to a list of valid directories.

## Challenges Encountered

One of the main challenges encountered during the project was dealing with exceptions in the code. There were several types of exceptions that needed to be handled, such as RequestException, HTTPError, and MissingSchema. These exceptions were handled using try-except blocks in the code.

Another challenge was a lack of knowledge about the web and how it works. This was overcome by researching the relevant topics and reading documentation about the libraries and functions used in the code.

## Conclusion

To sum up, through this project, I gained an understanding of how the web works, including how requests and responses are sent and received, and how to validate links on a website using Python. The project presented several challenges, such as handling exceptions and dealing with unfamiliar concepts, but I was able to overcome them by researching and using try-except blocks in the code. Overall, this project provided valuable experience in web development and Python programming.