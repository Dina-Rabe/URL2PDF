import requests
import webbrowser

def open_index_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('index.html', 'w') as file:
            file.write(response.text)
        webbrowser.open('index.html')
    else:
        print("Failed to fetch the HTML content.")

# Example usage
url = 'https://www.example.com'  # Replace with the desired URL
open_index_html(url)