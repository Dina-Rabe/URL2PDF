# Web Scraping and PDF Generation

This project is a Python script that performs web scraping on a given URL, extracts image elements from the HTML content, and generates a PDF document with the images and their alt text.

## Prerequisites

- Python 3.x
- pip package manager

## Installation

1. Clone the repository:
git clone https://github.com/Dina-Rabe/URL2PDF.git


2. Navigate to the project directory:

cd your-repository


3. Install the required dependencies:

pip install -r requirements.txt


## Usage

1. Run the main.py script with the following command:

python main.py --URL <url> --RESULT <output_file.pdf>

Replace `<url>` with the target URL from which you want to extract images, and `<output_file.pdf>` with the desired name of the generated PDF file.

2. The script will fetch the HTML content, save it to a temporary folder, extract the image elements, and generate a PDF file with the images and their alt text.

3. Once the script finishes executing, you will find the generated PDF file in the current directory.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

