import requests
import urllib.request
from PIL import Image
response = requests.get("https://api.github.com/emojis")
if response.status_code==200:
 emojis = response.json()
else:
    print("Status Code error,You cannot connect to the Api")
key={}
listF=[]
def print_all_icons():
    print("list of Icon")
    for emoji in emojis:
        print(emoji)
def search_icons_by_keyword(keyword):
   key=filter(lambda k:keyword in k,emojis)
   for k in key:
       i=0
       print(k)
       listF.insert(i,k)
       i=i+1

def display_icon(nameOfEmoji):
    if nameOfEmoji in listF:
       url= emojis[nameOfEmoji]
    else:
       print( "Emoji not found")

    urllib.request.urlretrieve(url, "gfg.png")
    img = Image.open("gfg.png")
    img.show()

