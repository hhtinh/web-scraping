from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# keyword in lower case
keyword = "vinpro"
pageURL = "http://tuyendungplus.com/1725-trung-tam-dien-may-vinpro-tap-doan-vingroup-tuyen-dung.html"
count = 0

html = urlopen(pageURL)
bsObj = BeautifulSoup(html, "html.parser")

# 1. Remove HTML
texts = bsObj.findAll(text = True)
[s.extract() for s in bsObj(['style', 'script', '[document]', 'head', 'title'])]
visible_text = bsObj.getText()
#print (visible_text)

# 2. Remove non-letters
letters_only = re.sub("[^a-zA-Z]", " ", visible_text)
#print (letters_only)

# 3. Convert to lower case, split into individual words
words = letters_only.lower().split()

for word in words:
    if word == keyword:
        count += 1

print("Total word(s) = " + str(count))
