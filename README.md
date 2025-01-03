Product Price Scraper
This is a Python-based web scraping project that collects product information (name and price) from various online stores. It supports scraping from several popular Ukrainian e-commerce websites, including Comfy, CTRS, Rozetka, Moyo, and Foxtrot. The scraped data is then stored in a SQLite database for easy access and analysis.

Features:
Web Scraping: Extract product names and prices from the provided product page URLs.
Database Integration: Store the collected data in a SQLite database, organized by store names (e.g., Comfy, CTRS, Rozetka).
Time Tracking: The system automatically records the date and time when the data is scraped.
Flexible Headers: The project uses a dictionary of headers to customize the requests for each e-commerce site, ensuring compatibility and reliable access.
Data Storage: Uses SQLite for efficient data storage, with tables created for each store.
User Interaction: The program allows users to input a product URL, identify the corresponding store, and store the scraped data into the appropriate database table.
Technologies:
Python 3: The project is built using Python 3 with the requests, BeautifulSoup, and sqlite3 libraries.
SQLite: A lightweight database for storing scraped data.
Web Scraping Libraries: BeautifulSoup for parsing HTML and requests for making HTTP requests.
Setup:
Clone the repository.
Install the required dependencies using:
Копіювати код
pip install requests beautifulsoup4
Run the program.py file to start scraping by entering a product URL from one of the supported stores.
Supported Stores:
Comfy
CTRS
Rozetka
Moyo
Foxtrot
