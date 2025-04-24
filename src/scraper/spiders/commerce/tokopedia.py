import scrapy


class TokpedSpider(scrapy.Spider):
    name = "tokped"
    allowed_domains = ["www.tokopedia.com"]

    custom_settings = {
        "ROBOTSTXT_OBEY": False,
        "HTTPERROR_ALLOWED_CODES": [403]
    }

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
    }

    def __init__(self, keyword: str=None):
        """
        
        """
        super().__init__()
        self.keyword = str(keyword)

    async def errback(self, failure):
        page = failure.request.meta.get("playwright_page")
        await page.close()
        
    def start_requests(self):
        """

        """
        if not self.keyword:
            self.logger.error("No keyword provided")
            return

        keyword = self.keyword.strip().replace(" ", "%20")
        url = f"https://www.tokopedia.com/search?st=&q={keyword}&srp_component_id=02.01.00.00&srp_page_id=&srp_page_title=&navsource="

        self.logger.info(f"Requesting URL: {url}")

        yield scrapy.Request(
            url=url, 
            headers=self.headers,
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "errback": self.errback
            },
            callback=self.parse_search,
        )

    def parse_search(self, response):
        """
        
        """
        self.logger.info(f"Parsing search results for keyword: {self.keyword}")

        
