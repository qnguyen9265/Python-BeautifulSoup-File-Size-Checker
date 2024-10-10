from bs4 import BeautifulSoup 
import requests 
import re
import sys

# Links to test: 
# https://www.cs.odu.edu/~mweigle/courses/cs532/pdfs.html
# https://www.cs.odu.edu/~mln/pubs/all.html
# https://homepages.rpi.edu/~brings/

req = requests.get(sys.argv[1]) # makes request with supplied link from command line
soup = BeautifulSoup(req.text, 'html.parser') # parses the response
PDFpattern = re.compile(r"\.pdf$") # ends in .pdf; was practicing using a way to get pdf links with regular expressions
HTTPpattern = re.compile(r"^https?:\/\/") # starts with http:// or https://

for link in soup.find_all('a'):
    #print("\n{}".format(link))
    href = link.get('href')
    #print(href)
    m = HTTPpattern.match(href)
    if (m != None):
        #print("\n{}".format(m))    
        req = requests.get(href)
        if req.headers["content-type"] == "application/pdf":
            print("\nURI: {}".format(href))
            print("Final URI: {}".format(req.url))
            try:
                print("Content Length: {:,} bytes".format(int(req.headers.get("content-length")))) # turns the content-length string into an int so that it can be formatted with commas
            except:
                print("Content Length: 0 bytes")

# tested a way to get all .pdf links with regular expressions
#    m = PDFpattern.search(href) # m = PDFpattern.match was always returning None 
#    if (m != None):
#        m = href
#        print(m)
