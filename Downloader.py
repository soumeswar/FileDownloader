import requests
import os

def download_file(url, destination):
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(destination), exist_ok=True)  # Create directory if it doesn't exist
        with open(destination, 'wb') as f:
            f.write(response.content)
        print("Downloaded Successfully!")
    else:
        print("Download Failed Unexpectedly!")

url = input("[*] Enter the URL to download: ")
url_extension = url.split('.')[-1]
destination = input("[&] Choose a filename (would place the file in the folder which this program is on) or write the directory where to save the file: ")

# Check if the destination is a directory or a filename
if os.path.isdir(destination):
    destination = os.path.join(destination, f"downloaded_file.{url_extension}")
elif '.' not in destination:
    destination = os.path.join(destination, f"downloaded_file.{url_extension}")

download_file(url, destination)
