
from bs4 import BeautifulSoup

html_file ="eg.html"
user_exception =input("Enter the class name you dont want to remove:(separate it by comma(,)) ")
exception =user_exception.split(",")
# Our html string we want to remove the class attribute from
with open(html_file, 'r',encoding="utf8") as f:
        html_content = f.read()
f.close()        
soup = BeautifulSoup(html_content, 'html.parser')
for link in soup.find_all():
        if link.attrs.get('class'):
                value = ' '.join(link.attrs.get('class'))
                if value not in exception:
                        link.attrs.pop("class", None)

                

with open("output.html", 'w',encoding="utf8") as f:
        f.write(str(soup))
f.close()

