
from bs4 import BeautifulSoup
html_file ="eg.html"

exception ="mt-content-container"
# Our html string we want to remove the class attribute from
with open(html_file, 'r',encoding="utf8") as f:
        html_content = f.read()
f.close()        
soup = BeautifulSoup(html_content, 'html.parser')
for link in soup.find_all():
    if link.attrs.get('class'):
        if exception not in link.attrs.get('class'):
            link.attrs.pop("class",None)
            print(link.attrs.get('class'))
   

with open("output.html", 'w',encoding="utf8") as f:
        f.write(str(soup))


