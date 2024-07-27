# HTML and CSS Cleaning Tool

### Description

The **HTML and CSS Cleaning Tool** is a Python application designed to efficiently strip unnecessary CSS classes and IDs from HTML files, streamlining web documents for improved performance and readability. Built using `tkinter` for the GUI, `BeautifulSoup` for HTML parsing, and `cssutils` for CSS parsing, this tool allows users to select HTML and CSS files, specify exceptions for classes and IDs to retain, and outputs a cleaned-up version of the HTML file.

### Features

- **Intuitive GUI**: Developed using `tkinter`, the application offers a user-friendly interface for selecting files and entering exceptions.
- **HTML Parsing**: Utilizes `BeautifulSoup` to process and clean HTML content, removing unwanted classes and IDs while preserving specified exceptions.
- **CSS Integration**: Leverages `cssutils` to extract CSS selectors, ensuring that only essential styles are maintained according to the chosen CSS file.
- **Custom Exceptions**: Users can specify exceptions for classes and IDs, providing flexibility in the cleaning process.
- **Output**: Generates a new, cleaned HTML file with redundant classes and IDs removed, enhancing document clarity and load times.

### How It Works

1. **Select HTML File**: Use the "Browse" button to choose an HTML file for processing.
2. **Select CSS File**: Optionally, select a CSS file to specify which classes and IDs should be retained.
3. **Enter Exceptions**: Input any additional classes or IDs to keep, separated by commas.
4. **Process**: Click "Process" to clean the HTML file. The application will remove unnecessary classes and IDs based on the selected CSS file and specified exceptions.
5. **Output**: A new, cleaned HTML file is saved in the same directory, prefixed with "CLEANED-".

### Installation and Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/spiritualsquad/cleaningHTMLandCSS.git
   cd cleaningHTMLandCSS
   ```

2. **Install Dependencies**:
   ```bash
   pip install beautifulsoup4 cssutils
   ```

3. **Run the Application**:
   ```bash
   python classTrim.py
   ```

4. **Follow the GUI Instructions** to select files, input exceptions, and process the HTML.

### Code Overview

- **`remove_classes(html_file, exceptions)`**: Cleans the HTML file by removing any classes or IDs not included in the exceptions list.
- **`browse_files()` & `browse_files_css()`**: Handle file selection dialogs for HTML and CSS files.
- **`process()`**: Orchestrates the cleaning process, applying the class and ID removal logic, and outputs the cleaned HTML.

### Example Usage

1. **Selecting Files**: Use the interface to browse and select your HTML and CSS files.
2. **Entering Exceptions**: Add any classes or IDs you want to retain, separated by commas, in the exception field.
3. **Processing**: Hit the "Process" button to generate a cleaned HTML file with unwanted attributes removed.


### Contributer - [Arsh Jassal].(https://github.com/arsh-jassal)
