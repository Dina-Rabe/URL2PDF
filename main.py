import requests
import os
import sys
from requests.exceptions import MissingSchema
import shutil
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

TEMP_FOLDER_NAME = './.temp'

def get_given_url():
    response = ''
    # Iterate over the command-line arguments
    for index, arg in enumerate(sys.argv):
        if arg == "--URL" and index + 1 < len(sys.argv):
            response = sys.argv[index + 1]
            break
    return response

def get_given_output_file():
    response = ''
    # Iterate over the command-line arguments
    for index, arg in enumerate(sys.argv):
        if arg == "--RESULT" and index + 1 < len(sys.argv):
            response = sys.argv[index + 1]
            break
    return response

def open_index_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if not os.path.exists(TEMP_FOLDER_NAME):
                os.mkdir(TEMP_FOLDER_NAME)
                print('here')
            with open(TEMP_FOLDER_NAME + '/index.html', 'w') as file:
                file.write(response.text)
        else:
            print("Failed to fetch the HTML content.")
    except MissingSchema:
        print("Invalid URL provided. Please include a valid scheme (e.g., 'http://' or 'https://').")
    except requests.exceptions.RequestException as e:
        print("An error occurred:", str(e))

def remove_temp_folder():
    if os.path.exists(TEMP_FOLDER_NAME):
        shutil.rmtree(TEMP_FOLDER_NAME)

def extract_img_elements(html_file):
    response = []
    with open(html_file, 'r') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        img_elements = soup.find_all('img')

        img_data = []
        for img in img_elements:
            img_attrs = img.attrs
            img_data.append(img_attrs)

        for item in img_data:
            alt_value = item.get("alt")
            src_value = item.get("src")
            temp_dict = {'alt': alt_value, 'src': src_value}
            response.append(temp_dict)
    return response


def write_pdf(data_list, output_file):
    c = canvas.Canvas(output_file, pagesize=A4)

    page_height = A4[1]  # Height of the page in points
    margin = inch  # Margin size in points
    content_height = page_height - 2 * margin  # Height available for content

    y = page_height - margin  # Initial y-coordinate

    for data in data_list:
        alt = data.get("alt")
        src = data.get("src")

        # Calculate the required space for the alt text and image
        line_height = c._leading
        image_height = 3 * inch
        required_height = line_height + image_height

        # Check if there's enough space on the current page, otherwise create a new page
        if y - required_height < margin:
            c.showPage()
            y = page_height - margin

        # Write alt value
        c.drawString(inch, y - line_height, alt)
        y -= line_height

        # Download image from the src link
        response = requests.get(src)
        image_file = f"{alt}.jpg"
        with open(image_file, "wb") as file:
            file.write(response.content)

        # Draw the image on the canvas
        c.drawImage(image_file, inch, y - 2 * inch, width=3 * inch, height=3 * inch)
        y -= image_height

        y -= line_height  # Add some space between items

    # Save the canvas as PDF
    c.save()

# Example usage
given_url = get_given_url()
output_file = get_given_output_file()
open_index_html(given_url)
img_data = extract_img_elements(TEMP_FOLDER_NAME + '/index.html')
print(len(img_data))
write_pdf(img_data, output_file)
#remove_temp_folder()