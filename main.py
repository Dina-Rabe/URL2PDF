import requests
import os
import sys
from requests.exceptions import MissingSchema
import shutil
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import logging

TEMP_FOLDER_NAME = './.temp'
error_log = logging.getLogger('ERROR_LOG')
error_log.setLevel(logging.ERROR)
error_log_file = logging.FileHandler('.log/error.log')
error_log_file.setLevel(logging.ERROR)
error_log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
error_log_file.setFormatter(error_log_format)
error_log.addHandler(error_log_file)

info_log = logging.getLogger('INFO_LOG')
info_log.setLevel(logging.INFO)
info_log_file = logging.FileHandler('.log/app.log')
info_log_file.setLevel(logging.INFO)
info_log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
info_log_file.setFormatter(info_log_format)
info_log.addHandler(info_log_file)

def get_given_url():
    response = ''
    for index, arg in enumerate(sys.argv):
        if arg == "--URL" and index + 1 < len(sys.argv):
            response = sys.argv[index + 1]
            break
    if response == '':
        raise ValueError("URL not provided.")
    else:
        info_log.info("URL provided")
    return response

def get_given_output_file():
    response = ''
    for index, arg in enumerate(sys.argv):
        if arg == "--RESULT" and index + 1 < len(sys.argv):
            response = sys.argv[index + 1]
            break
    if response == '':
        raise ValueError("Output file not provided.")
    else:
        info_log.info("Output file provided")
    return response

def open_index_html(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if not os.path.exists(TEMP_FOLDER_NAME):
                os.mkdir(TEMP_FOLDER_NAME)
            with open(TEMP_FOLDER_NAME + '/index.html', 'w') as file:
                file.write(response.text)
            info_log.info("URL Content Downloaded!")
        else:
            error_log.error("Failed to fetch the HTML content.")
    except MissingSchema:
        error_log.error("Invalid URL provided. Please include a valid scheme (e.g., 'http://' or 'https://').")
    except requests.exceptions.RequestException as e:
        error_log.error("An error occurred:", str(e))

def remove_temp_folder():
    if os.path.exists(TEMP_FOLDER_NAME):
        shutil.rmtree(TEMP_FOLDER_NAME)
        info_log.info("TEMP FOLDER removed!")
    else:
        error_log.error("TEMP FOLDER Not present!")

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
        if response == '':
            raise ValueError("No image in this URL!")
        else:
            info_log.info("List of all image fetched successfully!")
    return response


def write_pdf(data_list, output_file):
    c = canvas.Canvas(output_file, pagesize=A4)
    page_height = A4[1]
    margin = inch
    y = page_height - margin

    for data in data_list:
        alt = data.get("alt")
        src = data.get("src")
        line_height = c._leading
        image_height = 3 * inch
        required_height = line_height + image_height
        if y - required_height < margin:
            c.showPage()
            y = page_height - margin
        c.setFont("Helvetica-Bold", 24)
        string_width = c.stringWidth(alt, "Helvetica-Bold", 24)
        x = (A4[0] - string_width) / 2
        c.drawString(x, y - line_height, alt)
        y -= line_height
        response = requests.get(src)
        image_file = f".temp/{alt}.jpg"
        with open(image_file, "wb") as file:
            file.write(response.content)
        c.drawImage(image_file, x, y - line_height - image_height, width=3 * inch, height=3 * inch)
        y -= required_height  
    c.save()
    info_log.info("PDF created!")
    

def main():
    try:
        given_url = get_given_url()
        output_file = get_given_output_file()        
    except ValueError as error:
        error_log.error(str(error))
        sys.exit()
    open_index_html(given_url)
    try:
        img_data = extract_img_elements(TEMP_FOLDER_NAME + '/index.html')
    except ValueError as error:
        error_log.error(str(error))
        sys.exit()
    write_pdf(img_data, output_file)
    remove_temp_folder()
    info_log.info(output_file + " generated successfully!")

if __name__ == "__main__":
    main()