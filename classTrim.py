import tkinter as tk
from tkinter import filedialog
from bs4 import BeautifulSoup
import os

def remove_classes(html_file, exceptions):
    with open(html_file, 'r', encoding="utf8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    for link in soup.find_all():
        if link.attrs.get('class'):
            value = ' '.join(link.attrs.get('class'))
            if value not in exceptions:
                link.attrs.pop("class", None)

        
    original_directory = os.path.dirname(html_file)
    original_filename = os.path.basename(html_file)
    cleaned_filename = os.path.join(original_directory, "cleaned-" + original_filename)

    with open(cleaned_filename, 'w', encoding="utf8") as f:
        f.write(str(soup))
    return cleaned_filename
        
def browse_files():
    filename = filedialog.askopenfilename(initialdir="/", title="Select HTML File",
                                          filetypes=(("HTML files", "*.html*"), ("all files", "*.*")))
    entry.delete(0, tk.END)
    entry.insert(0, filename)
def process():
    html_file = entry.get()
    exceptions = exception_entry.get().split(",")
    value = remove_classes(html_file, exceptions)
    tk.messagebox.showinfo("Success", "Classes removed successfully!\nOutput saved! as "+ value)

    


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

process_button = tk.Button(root, text="Process", command=process)
process_button.grid(row=2, column=1)

root.mainloop()
