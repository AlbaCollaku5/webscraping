# Book Scraper

A Python web scraper to collect book information from [Books to Scrape](https://books.toscrape.com/), a sandbox website for practicing web scraping.

---

## Project Description

This project scrapes book details including:

- Book Title
- Price (in GBP)
- Star Rating
- Image URL

from all pages on the site, following pagination automatically.

The scraped data is saved into an Excel file (`books_scraped.xlsx`) with one sheet per page.

The scraper runs repeatedly every 5 minutes (configurable) until manually stopped.

---

## Features

- Uses `requests` to fetch webpage content
- Parses HTML with `BeautifulSoup`
- Extracts and cleans price and rating data robustly using regular expressions
- Handles pagination safely with proper URL joining (`urllib.parse.urljoin`)
- Saves data in a clean Excel file with multiple sheets using `pandas` and `openpyxl`
- Automation loop with delay and error handling
- Graceful exit on user interrupt (Ctrl+C)

---

## Installation

1. Clone the repository or download the script.
2. Install dependencies (recommended in a virtual environment):




---

## Usage

Run the scraper from the command line:



It will:

- Start scraping all pages from the site
- Save all collected data to `books_scraped.xlsx`
- Wait 5 minutes and repeat
- To stop, press `Ctrl + C`

---

## Code structure

- `scrape_page(url)`: Scrapes book data from a single page.
- `scrape_all_pages()`: Iterates through all pages by following "Next" buttons and saves data.
- `automate_scraping(interval_minutes)`: Runs scraping repeatedly with a delay.

---

## Dependencies

- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`
- `openpyxl`

---

## License

This project is for educational use only. The target website is a sandbox practice site and no scraping is performed on real or protected websites.

---

## References

- [Books to Scrape](https://books.toscrape.com/)
- BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Requests library: https://requests.readthedocs.io/
- Pandas documentation: https://pandas.pydata.org/docs/
- Openpyxl documentation: https://openpyxl.readthedocs.io/

---

## Author

Alba Collaku

---