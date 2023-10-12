import cs
import requests
from bs4 import BeautifulSoup



def scrape_justdial(keyword, location, num_pages):
    base_url = f"https://www.justdial.com/{location}/{keyword}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }


    results = []


    for page in range(1, num_pages + 1):
        url = f"{base_url}/page-{page}"


        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")


        # Find all listings on the page
        listings = soup.find_all("li", class_="jsx-8019251d22823f16 results_listing_container")


        for listing in listings:
            result = {}
            print(listing)


            # Extract information from each listing
            title_element = listing.find("span", class_="lng_cont_name")
            if title_element:
                result["Title"] = title_element.text.strip()
            else:
                result["Title"] = ""


            address_element = listing.find("span", class_="cont_fl_addr")
            if address_element:
                result["Address"] = address_element.text.strip()
            else:
                result["Address"] = ""


            phone_element = listing.find("p", class_="contact-info")
            if phone_element:
                result["Phone"] = phone_element.text.strip()
            else:
                result["Phone"] = ""


            results.append(result)


    return results


# Example usage
keyword = "restaurants"
location = "Mumbai"
num_pages = 3


results = scrape_justdial(keyword, location, num_pages)


# Export the data to a CSV file
filename = f"{keyword}_{location}_results.csv"
fieldnames = ["Title", "Address", "Phone"]


with open(filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(results)


print(f"Data scraped successfully and saved to {filename}.")
