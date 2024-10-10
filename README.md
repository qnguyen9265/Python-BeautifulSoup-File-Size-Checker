# Python Beautiful Soup File Size Checker

This is a Python script that uses BeautifulSoup and Requests to query websites and return the file size in bytes of .pdf files. This is a reupload of a project done in 2022 for a Python coding course with all references to course material removed.

## Explanation and Reasoning

Below, I explain my thoughts and reasoning while working through this project.

I imported requests and beautifulsoup4 to make requests on URIs and read the responses, sys to take command-line arguments, and re to practice a few different ways to ensure that only viable websites are checked.

fileSizeChecker.py:
* take the URI of a webpage as a command-line argument
* extract all the links from the page
* for each link, request the URI and use the `Content-Type` HTTP response header to determine if the link references a PDF file 
* for all links that reference a PDF file, print the original URI (found in the source of the original HTML), the final URI (after any redirects), and the number of bytes in the PDF file.

req holds the response from the URI taken at the command line, and soup holds the parsed response. PDFpattern and HTTPpattern are regexes I made to check that a string ends in ".pdf" and starts with "http://" or "https://" respectively.

```python
for link in soup.find_all('a'):
    href = link.get('href')
    m = HTTPpattern.match(href)
    if (m != None):   
        req = requests.get(href)
        if req.headers["content-type"] == "application/pdf":
            print("\nURI: {}".format(href))
            print("Final URI: {}".format(req.url))
            try:
                print("Content Length: {:,} bytes".format(int(req.headers.get("content-length"))))
            except:
                print("Content Length: 0 bytes")
```
For each link inside of soup, this loop takes the href and checks if it starts with http:// or https://. If it does, the loop goes on to make a new request with that href before printing out the beginning URI, final URI, and content length.

## References

https://curl.se/docs/manpage.html#

https://docs.python.org/3/library/re.html

https://requests.readthedocs.io/en/latest/

https://www.crummy.com/software/BeautifulSoup/bs4/doc/