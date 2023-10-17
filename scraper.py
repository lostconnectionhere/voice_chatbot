import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to the website
url = "https://www.amsterdam.nl/burgerzaken/"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find and extract specific elements from the page
    # Example: Find all links (anchor tags) on the page
    # links = soup.find_all("a")
#     paragraphs = soup.find_all('p')
    
#     # Print the links
# #     for link in links:
# #         print(link.get("href"))

# # else:
# #     print(f"Failed to retrieve the page. Status code: {response.status_code}")

#     for paragraph in paragraphs:
#             print(paragraph.get_text())

# else:
#     print("Failed to retrieve the webpage. Status code:", response.status_code)

 # Extract and print text from <h2> elements with class "blok-titel small-titel"
    h2_elements = soup.find_all('h2', class_='blok-titel small-titel')
    # Iterate through <h2> elements and extract text from each
    for h2 in h2_elements:
        h2_text = h2.get_text()
        print("Hoofdonderwerp:")
        print(h2_text)

        # Find and extract <ul> elements within the current <h2> element
        ul_elements = h2.find_next('ul', class_='links')

        # Extract text from <ul> elements and print
        ul_text = ul_elements.get_text() if ul_elements else ""
        print("Subonderwerp:")
        print(ul_text)

else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)