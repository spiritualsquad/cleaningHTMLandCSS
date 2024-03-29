import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
import os
import cssutils

def remove_classes(html_file, exceptions):
    with open(html_file, 'r', encoding="utf8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    for link in soup.find_all():
        if link.attrs.get('class'):
            value_class = ''.join(link.attrs.get('class'))
            if value_class not in exceptions:
                link.attrs.pop("class", None)
        if link.attrs.get('id'):
            value_id = ''.join(link.attrs.get('id'))
            if value_id not in exceptions:
                link.attrs.pop("id", None)
            

        
    original_directory = os.path.dirname(html_file)
    original_filename = os.path.basename(html_file)
    cleaned_filename = os.path.join(original_directory, "CLEANED-" + original_filename)

    with open(cleaned_filename, 'w', encoding="utf8") as f:
        f.write(str(soup.prettify()))
    return cleaned_filename
        
def browse_files():
    filename = filedialog.askopenfilename(initialdir="/", title="Select HTML File",
                                          filetypes=(("HTML files", "*.html*"), ("all files", "*.*")))
    entry.delete(0, tk.END)
    entry.insert(0, filename)
def browse_files_css():
    filename = filedialog.askopenfilename(initialdir="/", title="Select CSS File",
                                          filetypes=(("CSS files", "*.css*"), ("all files", "*.*")))
    exception_css.delete(0, tk.END)
    exception_css.insert(0, filename)
def process():
    html_file = entry.get()
    file_path = exception_css.get()
    css = read_css_from_file(file_path)
    exceptions_css = extract_classes_and_ids(css)
    exceptions = exception_entry.get().split(',')
    for exception in exceptions:
        exceptions_css.append(exception)

    value = remove_classes(html_file, exceptions_css)
    tk.messagebox.showinfo("Success", "Classes removed successfully!\nOutput saved! as "+ value)

    

#import cssutils

def extract_classes_and_ids(css):
    classes_and_ids = []

    # Parse CSS
    sheet = cssutils.parseString(css)

    # Extract class and ID selectors
    for rule in sheet:
        if rule.type == rule.STYLE_RULE:
            selectors = rule.selectorText.split(',')
            for selector in selectors:
                selector_parts = selector.strip().split()
                for part in selector_parts:
                    if part.startswith('.'):
                        class_name = part[1:]
                        classes_and_ids.append(class_name)
                    elif part.startswith('#'):
                        id_name = part[1:]
                        classes_and_ids.append(id_name)

    return classes_and_ids

def read_css_from_file(file_path):
    with open(file_path, 'r') as file:
        css = file.read()
    return css



# Create main window
root = tk.Tk()
root.title("HTML Class Remover")

# Create widgets
label = tk.Label(root, text="Select HTML File:")
label.grid(row=0, column=0)

entry = tk.Entry(root, width=50)
entry.grid(row=0, column=1)

browse_button = tk.Button(root, text="Browse", command=browse_files)
browse_button.grid(row=0, column=2)

exception_label = tk.Label(root, text="Enter classes to keep (separated by comma):")
exception_label.grid(row=1, column=0)
exception_entry = tk.Entry(root, width=50)
exception_entry.grid(row=1, column=1)

exception_css = tk.Entry(root, width=50)
exception_css.grid(row=2, column=1)
browse_button_exception = tk.Button(root, text="Browse", command=browse_files_css)
browse_button_exception.grid(row=2, column=2)

process_button = tk.Button(root, text="Process", command=process)
process_button.grid(row=3, column=1)

root.mainloop()
