import requests as req
from bs4 import *
import os

link = req.get("https://unsplash.com/@konick")
parse = BeautifulSoup(link.text, "html.parser")

links = []
x = parse.select('img[src^="https://images.unsplash.com/photo-"]')

for img in x:
    links.append(img['src'])

#for l in links:
#   print(l)

os.mkdir('konick_photos')
i=1

for index, img_link in enumerate(links):
    if i<=10:
        img_data = req.get(img_link).content
        with open("konick_photos/" +str(index+1)+'.jpg', 'wb') as f:
            f.write(img_data)
        i +=1
    else:
        f.close()
        break



