import requests
from datetime import date
from bs4 import BeautifulSoup
import random

# Comic-Img Grab inspired by this gist - https://gist.github.com/lawrenceccheung/1a92c3d02e0a314bc8f58ff4d8ab13c4

def GrabImage():
    # Set the headers - This is to prevent Cloudflare issues
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'
    }

    # The url of the comic strip
    rootUrl="https://wallpapercave.com/"
    url=f"{rootUrl}/calvin-and-hobbes-desktop-wallpaper"

    # What file to save it as
    savefile=f"calvinhobbes_daily.jpg"

    # Request the page
    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    # Get all links with the lazyload img-fluid class
    links=soup.find_all(class_="wimg")

    # Search for the "Calvin and Hobbes Comic Strip" image
    images = []
    for image in links:
        images.append(rootUrl+image['src'])

    # Grab a random image
    pic = images.pop(random.randint(0,random.randint(0,len(images)-1)))

    # Save the file
    r = requests.get(pic, allow_redirects=True)
    open(savefile, 'wb').write(r.content)

    # Return the name of the savefile
    return savefile