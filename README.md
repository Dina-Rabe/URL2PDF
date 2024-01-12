
livecodeserver

# URL to PDF Converter

This Python script converts images from a given URL into a PDF document. It fetches the HTML content from the URL, extracts the image elements, and generates a PDF file containing the images along with their alt text.

## Prerequisites

- Python 3.x
- requests library
- bs4 library (BeautifulSoup)
- reportlab library

## Installation

1. Clone the repository:

   git clone https://github.com/your-username/image-to-pdf-converter.git
   cd image-to-pdf-converter

    Install the required libraries using pip:
    pip install -r requirements.txt
    ```

Usage

Run the main.py file with the following command:
shell

python main.py --URL [URL] --RESULT [output_file]

Replace [URL] with the URL containing the images you want to convert, and [output_file] with the desired name of the output PDF file.

For example:
shell

python main.py --URL https://example.com/images --RESULT output.pdf

The script will download the HTML content from the given URL, extract the image elements, and generate a PDF file named output.pdf containing the images and their alt text.

Logging

The script logs the application's activities using two separate log files:

    app.log: Logs informational messages such as URL provided, output file provided, URL content downloaded, list of all images fetched successfully, PDF created, and output file generated successfully.
    
    error.log: Logs error messages such as failed to fetch the HTML content, invalid URL provided, an error occurred during the HTTP request, no image found in the URL, and temporary folder not present.

You can find the log files in the .log directory within the project folder.
License

This project is licensed under the MIT License.
basic


Feel free to customize the content and formatting of the README file according to your preferences and specific requirements.
