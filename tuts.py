from urllib.request import urlopen
import keyboard
from bs4 import BeautifulSoup
import sys

if keyboard.is_pressed('l'):
    sys.exit() 
while True: 
    url_start = 'https://pirate.monkeyness.com/api/translate?english='
    url_end = input("Please enter engrish 🔥 for spaces type %20: ")
    url = url_start + url_end

    html = urlopen(url).read() 
    soup = BeautifulSoup(html, features="html.parser")
    # kill all script and style elements 
    for script in soup(["script", "style"]):
        script.extract()
    # rip it out 
    # get text 
    text = soup.get_text() 
    # break into lines and remove leading and trailing space on each 
    lines = (line.strip() for line in text.splitllines()) # break multi-headlines into a line each 
    chunks = (phrase.strip() for line in lines for phrase in line.split(" ")) # drop blank lines 
    text = '\n'.join(chunk for chunk in chunks if chunk)
    print(text)   
