import os
import requests
from bs4 import BeautifulSoup

# Define the URL of the website
url = "https://www.theccc.org.uk/publication/spatial-planning-for-climate-resilience-and-net-zero-cse-tcpa/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all links on the page
    links = soup.find_all("a")

    # Create a directory to save the PDFs
    os.makedirs("pdfs", exist_ok=True)

    # Loop through links and download PDFs
    for link in links:
        href = link.get("href")
        if href and href.endswith(".pdf"):
            pdf_url = href

            # Create a filename for the PDF based on the URL
            pdf_name = os.path.join("pdfs", os.path.basename(pdf_url))

            # Send a request to download the PDF
            pdf_response = requests.get(pdf_url)

            # Check if the PDF request was successful
            if pdf_response.status_code == 200:
                # Save the PDF to the specified file
                with open(pdf_name, "wb") as pdf_file:
                    pdf_file.write(pdf_response.content)
                print(f"Downloaded: {pdf_name}")
            else:
                print(f"Failed to download: {pdf_url}")

