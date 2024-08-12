# import requests
# from bs4 import BeautifulSoup
# import os

# # Retrieve credentials from environment variables
# username = os.getenv('SCREENER_USERNAME')
# password = os.getenv('SCREENER_PASSWORD')

# # Create a session
# session = requests.Session()

# # Define URLs
# login_url = "https://www.screener.in/login/"
# download_url = "https://www.screener.in/excel/Reliance/"

# # Fetch the login page to get the CSRF token
# response = session.get(login_url)
# response.raise_for_status()  # Ensure we notice bad responses

# # Parse the HTML to extract the CSRF token
# soup = BeautifulSoup(response.text, 'html.parser')
# csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

# # Prepare payload and headers
# payload = {
#     'username': username,
#     'password': password,
#     'csrfmiddlewaretoken': csrf_token
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Referer': login_url,
#     'Content-Type': 'application/x-www-form-urlencoded'
# }

# # Perform login
# response = session.post(login_url, data=payload, headers=headers)
# response.raise_for_status()  # Ensure we notice bad responses

# # Check if login was successful
# if response.status_code == 403 or "Login" in response.text:
#     print("Login failed. Response content:")
#     print(response.text)
#     raise Exception("Login failed. Check credentials or CSRF token handling.")

# # Download the Excel file
# response = session.get(download_url)
# response.raise_for_status()  # Ensure we notice bad responses

# # Save the Excel file
# with open('reliance_data.xlsx', 'wb') as file:
#     file.write(response.content)





import requests
from bs4 import BeautifulSoup
import os
import subprocess

# Fetch credentials from Vault
def fetch_from_vault(secret_path, field_name):
    # Retrieve the secret field from Vault
    result = subprocess.run(
        ['vault', 'kv', 'get', '-field=' + field_name, secret_path],
        capture_output=True, text=True, check=True
    )
    return result.stdout.strip()

# Retrieve credentials from Vault
username = fetch_from_vault('secret/myapp', 'username')
password = fetch_from_vault('secret/myapp', 'password')

# Create a session
session = requests.Session()

# Define URLs
login_url = "https://www.screener.in/login/"
download_url = "https://www.screener.in/excel/Reliance/"

# Fetch the login page to get the CSRF token
response = session.get(login_url)
response.raise_for_status()  # Ensure we notice bad responses

# Parse the HTML to extract the CSRF token
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

# Prepare payload and headers
payload = {
    'username': username,
    'password': password,
    'csrfmiddlewaretoken': csrf_token
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': login_url,
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Perform login
response = session.post(login_url, data=payload, headers=headers)
response.raise_for_status()  # Ensure we notice bad responses

# Check if login was successful
if response.status_code == 403 or "Login" in response.text:
    print("Login failed. Response content:")
    print(response.text)
    raise Exception("Login failed. Check credentials or CSRF token handling.")

# Download the Excel file
response = session.get(download_url)
response.raise_for_status()  # Ensure we notice bad responses

# Save the Excel file
with open('reliance_data.xlsx', 'wb') as file:
    file.write(response.content)






















# import requests
# from bs4 import BeautifulSoup
# import os

# # Retrieve credentials from environment variables
# username = os.getenv('SCREENER_USERNAME')
# password = os.getenv('SCREENER_PASSWORD')

# # Create a session
# session = requests.Session()

# # Define URLs
# login_url = "https://www.screener.in/login/"
# download_url = "https://www.screener.in/excel/Reliance/"

# # Fetch the login page to get the CSRF token
# response = session.get(login_url)
# response.raise_for_status()  # Ensure we notice bad responses

# # Parse the HTML to extract the CSRF token
# soup = BeautifulSoup(response.text, 'html.parser')
# csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

# # Prepare payload and headers
# payload = {
#     'username': username,
#     'password': password,
#     'csrfmiddlewaretoken': csrf_token
# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Referer': login_url,
#     'Content-Type': 'application/x-www-form-urlencoded'
# }

# # Perform login
# response = session.post(login_url, data=payload, headers=headers)
# response.raise_for_status()  # Ensure we notice bad responses

# # Check if login was successful
# if response.status_code == 403 or "Login" in response.text:
#     print("Login failed. Response content:")
#     print(response.text)
#     raise Exception("Login failed. Check credentials or CSRF token handling.")

# # Download the Excel file
# response = session.get(download_url)
# response.raise_for_status()  # Ensure we notice bad responses

# # Save the Excel file
# with open('reliance_data.xlsx', 'wb') as file:
#     file.write(response.content)





























# import requests
# from requests.auth import HTTPBasicAuth
# import os

# # Retrieve credentials from environment variables
# username = os.getenv('SCREENER_USERNAME')
# password = os.getenv('SCREENER_PASSWORD')

# # Create a session and login
# session = requests.Session()
# login_url = "https://www.screener.in/login/"

# payload = {
#     'username': username,
#     'password': password,
#     'csrfmiddlewaretoken': ''  # If CSRF token is required, fetch it from the login page first

# }

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Referer': 'https://www.screener.in/login/',
#     'Content-Type': 'application/x-www-form-urlencoded'
# }

# # Optionally, get the CSRF token if required (many websites need this)
# response = session.get(login_url, headers=headers)
# if 'csrftoken' in response.cookies:
#     payload['csrfmiddlewaretoken'] = response.cookies['csrftoken']


# # response = session.post(login_url, data=payload, headers=headers)
# # Perform login with headers
# response = session.post(login_url, data=payload, headers=headers)
# response.raise_for_status()  # Ensure we notice bad responses





# # Check if login was successful
# if "Login" in response.text or response.status_code != 200:
#     print("Login failed. Response content:")
#     print(response.text)
#     raise Exception("Login failed. Check credentials.")

# # Download the Excel file
# download_url = "https://www.screener.in/excel/Reliance/"
# response = session.get(download_url)
# response.raise_for_status()  # Ensure we notice bad responses

# with open('reliance_data.xlsx', 'wb') as file:
#     file.write(response.content)



























# Perform login
# response = session.post(login_url, data=payload)
# if response.status_code == 403:
#     print("403 Forbidden: ", response.text)
#     raise HTTPError(f"403 Forbidden: {response.text}")

# if response.status_code != 200:
#     print(f"Failed to login. Status code: {response.status_code}")
#     print(f"Response text: {response.text}")
#     response.raise_for_status()  # Ensure we notice bad responses
