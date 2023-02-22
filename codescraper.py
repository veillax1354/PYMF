import requests
from bs4 import BeautifulSoup

# Prompt the user to enter a website URL
url = input('Enter the website URL: ')

# Send a GET request to the URL and retrieve its content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Save the HTML content to a text file
with open('output.txt', 'w') as file:
    file.write(str(soup))
