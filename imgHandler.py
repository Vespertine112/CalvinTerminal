import requests
from datetime import date
from bs4 import BeautifulSoup

# Comic-Img Grab inspired by this gist - https://gist.github.com/lawrenceccheung/1a92c3d02e0a314bc8f58ff4d8ab13c4
def GrabImage():
    # Set the headers
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
        }

    # Set the date to grab the comic
    year = date.today().year
    month = date.today().month
    day = date.today().day

    # The url of the comic strip
    url=f"https://www.gocomics.com/calvinandhobbes/{year}/{month}/{day}"

    # What file to save it as
    savefile=f"calvinhobbes_{year}_{month}_{day}.jpg"

    # Request the page
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, 'html.parser')


    # Get all links with the lazyload img-fluid class
    links=soup.find_all(class_="img-fluid")

    picurl = ""
    searchstring='Calvin and Hobbes Comic Strip' # Search string is the alt-text for the image.
    # Search for the "Calvin and Hobbes Comic Strip" image
    for link in links:
        if searchstring in link['alt']:
            # Get the url of the image
            picurl=link['src']
            # print(picurl)

    # # Save the file
    r = requests.get(picurl, allow_redirects=True)
    open(savefile, 'wb').write(r.content)
    return savefile