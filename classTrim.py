from bs4 import BeautifulSoup

def remove_classes(html_file):
    with open(html_file, 'r') as f:
        html_content = f.read()

    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all elements with classes and remove classes
    for tag in soup.find_all(True, class_=True):
        tag.attrs.pop("class", None)

    # Write modified HTML content back to file
    with open(html_file, 'w') as f:
        f.write(str(soup))

if __name__ == "__main__":
    html_file = input("Enter HTML file path: ")
    remove_classes(html_file)
    print("Classes removed from HTML elements successfully.")
