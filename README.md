# News and Product Scraper

This project is a web scraping application built using the Scrapy framework. It is designed to scrape both news articles and product information from various websites. The scraped data is stored in JSON format for further analysis or processing.

## Features

- **News Scraper**: Extracts details such as URL, title, publish date, author, content, and source from news websites.
- **Product Scraper**: Extracts details such as URL, title, price, image URL, rating, and description from e-commerce websites.
- **Configurable Settings**: Includes customizable Scrapy settings for crawling behavior.
- **Data Storage**: Saves scraped data in JSON format for easy access and processing.

## Project Structure
```
scraper/ 
├── data/               # Directory for storing scraped data 
│ └── news/             # JSON files for news data 
├── src/                # Source code for the scraper 
│ ├── scraper/          # Scrapy project directory 
│ │ ├── config/         # Configuration files 
│ │ │ └── settings.py   # Scrapy settings 
│ │ ├── items/          # Item definitions 
│ │ │ ├── news.py       # News item model 
│ │ │ ├── products.py   # Product item model 
│ │ │ └── __init__.py   # Item module initializer 
├── tests/              # Placeholder for tests 
├── scrapy.cfg          # Scrapy project configuration 
├── requirements.txt    # Python dependencies 
├── makefile            # Commands to run scrapers 
└── README.md           # Project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/news-scraper.git
   cd news-scraper
   ```

2. Create a virtual environment and activate it:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
## Usage
Running the Scrapers
Use the makefile to run specific scrapers:

- Run the Detik news scraper:
    ```bash
    make run-detik
    ```
- Run the Kompas news scraper:
    ```bash
    make run-kompas
    ```

The scraped data will be saved in the `data/news/` directory as JSON files.

Customizing Scrapers:
- Modify the item definitions in `src/scraper/items/` to add or remove fields.
- Update Scrapy settings in `src/scraper/config/settings.py` to adjust crawling behavior.

## Dependencies

The project uses the following Python libraries:

- `Scrapy`: For web scraping.
- `beautifulsoup4`: For parsing HTML content.
- `playwright` and `scrapy-playwright`: For handling dynamic web pages.
- `pandas`: For data manipulation (optional).

Refer to the `requirements.txt` file for the full list of dependencies.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## What's Next?

Here are some ideas for future improvements and features:

1. **Add More Scrapers**: Expand the project to include scrapers for additional news websites or e-commerce platforms.
2. **Database Integration**: Store scraped data in a database (e.g., PostgreSQL, MongoDB) for better scalability and querying.
3. **Data Analysis**: Implement scripts or tools to analyze the scraped data, such as sentiment analysis for news articles or price trend analysis for products.
4. **Web Interface**: Build a web-based dashboard to visualize and manage the scraped data.
5. **Error Handling**: Improve error handling and logging to make the scrapers more robust.
6. **Scheduler**: Integrate a task scheduler (e.g., Celery, Cron) to automate periodic scraping.
7. **API Integration**: Provide an API to access the scraped data programmatically.

Feel free to contribute by implementing any of these features or suggesting new ones!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

