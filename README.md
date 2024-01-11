URL2PDF Python Script

This Python script allows you to convert a web page to a PDF document. The script extracts the URL, opens the HTML file, finds all <img> tags, builds a dictionary containing image information, and appends each object to a list. Finally, it generates a PDF based on the collected image data.
Procedure

    Extract the URL: The script prompts the user to enter the URL of the web page they want to convert to a PDF.

    Open the index.html file: The script retrieves the HTML content from the provided URL and saves it as index.html.

    Find all <img> tags: The script parses the index.html file and locates all <img> tags within it.

    Build a dictionary: For each image found, the script creates a dictionary object with the following key-value pairs:
        img.name: The name of the image.
        src: The source URL of the image.
        desc: The image description or alt text.

    Append dictionary objects to a list: The script appends each image dictionary object to a list called dict_object.

    Build a PDF: Utilizing the collected image data, the script generates a PDF document. The document title is set as the page title extracted from the HTML file.

    Printing the URL: The script prints the URL of the web page that was converted to a PDF.

    Printing the list: The script displays the details of each image in the list:
        image_object.desc: The description or alt text of the image.
        image_object.src: The source URL of the image.

    PDF size limitation: The script checks the size of the generated PDF file. If the file size exceeds 5MB, it creates another PDF file to ensure that the size remains within the specified limit.

Note: This script requires the necessary Python libraries for HTML parsing, PDF generation, and file handling.

Feel free to customize and enhance this script according to your specific requirements.
Usage

    Ensure you have Python installed on your system.

    Install the required libraries by running the following command:

pip install <library_name>
```
Replace `<library_name>` with the actual names of the required libraries.

Run the script:
pgsql

    python url2pdf.py
    ```
    Follow the prompts to enter the URL and proceed with the conversion process.

Limitations

    The script assumes that the web page contains valid HTML markup and accessible images.
    Image formats other than <img> tags are not currently supported.
    Additional error handling and validation may be required based on specific use cases.

License

This project is licensed under the MIT License.
