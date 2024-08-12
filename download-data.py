import requests
from requests.auth import HTTPBasicAuth
import os

# Retrieve credentials from environment variables
username = os.getenv('SCREENER_USERNAME')
password = os.getenv('SCREENER_PASSWORD')

# Create a session and login
session = requests.Session()
login_url = "https://www.screener.in/login/"

payload = {
    'username': username,
    'password': password
}

# Perform login
response = session.post(login_url, data=payload)
response.raise_for_status()  # Ensure we notice bad responses

# Check if login was successful
if "Login" in response.text:
    raise Exception("Login failed. Check credentials.")

# Download the Excel file
download_url = "https://www.screener.in/excel/Reliance/"
response = session.get(download_url)
response.raise_for_status()  # Ensure we notice bad responses

with open('reliance_data.xlsx', 'wb') as file:
    file.write(response.content)
