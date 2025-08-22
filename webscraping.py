import requests
from bs4 import BeautifulSoup
import pandas as pd
import time 
import os 
import re
from urllib.parse import urljoin

#request and parse the page 
BASE_URL = "https://books.toscrape.com/"
rating_dict = {'One':1, 'Two': 2, 'Three':3, 'Four':4, 'Five':5}

def scrape_page(url):
    """ Scrape a single page and extract all books' data on it. """
    response = requests.get(url)
    response.raise_for_status()
    
    # 2. Parse the downloaded page's HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # 3. Find all the book containers (each book is an ,article. tag with a specific class)
    books = soup.find_all('article', class_='product_pod')

    # 4. Prepare a list to collect each books' info
    book_list= []

    # 5. Loop over each book container to extract data 
    for book in books:
        img_rel_url = book.find('img')['src']
        img_url = urljoin(BASE_URL, img_rel_url)
        
        #extract title from the alt attribute of the img tag
        title = book.find('img')['alt']

        #extract price text, remove the '£'and convert to float for numeric use
        price_text = book.find('p', class_='price_color').text
        match = re.search(r'\d+\.\d+', price_text)  # Extract digits with decimal number
        if match:
            price = float(match.group())
        else:
            price = 0.0  # Default fallback if not found


        #extract rating from the star-rating class 
        rating_class = book.find('p', class_='star-rating')['class'][1]
        rating = rating_dict.get(rating_class, 0) 

        #Append all extracted data into a dictionary and add to list
        book_list.append({
            'Image URL': img_url,
            'Title': title,
            'Price': price,
            'Rating': rating
        })

        # Return both the data on the page, and the entire parsed content (for navigation)
    return book_list, soup
    

def scrape_all_pages():
        """Scrape all pages by following 'Next' button and save data in an Excel file."""
        all_pages_data = []
        current_url = BASE_URL

        page_number =1 

        while True:
            print(f"Scarping page {page_number}: {current_url}")

            #Scrape the current page 
            book_data, soup = scrape_page(current_url)
            all_pages_data.append(book_data)
            
            #Find the 'Next' button, if it exists
            next_button = soup.find('li', class_='next')
            if next_button:
                next_relative_url = next_button.find('a')['href']
                current_url = urljoin(current_url, next_relative_url)
                page_number += 1
            else:
                print("No next page found. Finished scraping all pages.")
                break
                
        # Save all collected data into one Excel file with one sheet per page
        with pd.ExcelWriter('book_scaped.xlsx', engine='openpyxl') as writer:
            for i, page_data in enumerate(all_pages_data):
                 df = pd.DataFrame(page_data)
                 df.to_excel(writer, sheet_name= f'Page {i+1}', index=False)

        print("Scraping complete. Data saved to 'books_scraped.xlsx' ")
     
def automate_scraping(interval_minutes=5):
    """Run scraping every interval_minutes repeatedly."""
    print(f"Starting automation: scraping every {interval_minutes} minutes.")

    try:
         while True:
              scrape_all_pages()
              print(f"Waiting for {interval_minutes} minutes...")
              time.sleep(interval_minutes * 60)

    except KeyboardInterrupt:
         print("Automation stopped by user.")


if __name__ == '__main__':
     automate_scraping(interval_minutes=5)