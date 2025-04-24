import scrapy

from scraper.items import NewsItem


class KompasSpider(scrapy.Spider):
    name = "kompas"
    allowed_domains = ["bola.kompas.com"]

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

    def start_requests(self):
        """
        
        """
        url = "https://bola.kompas.com/liga-inggris"

        self.logger.info(f"Requesting URL: {url}")

        yield scrapy.Request(
            url=url, 
            headers=self.headers,
            meta={
                "playwright": True,
                "playwright_include_page": True,
                "errback": self.errback
            },
            callback=self.parse,
        )

    async def errback(self, failure):
        page = failure.request.meta.get("playwright_page")
        await page.close()

    def parse(self, response):
        """
        
        """
        articles_url = response.xpath('//div[@class="latest--news mt2 clearfix"]//div[@class="article__list clearfix"]//h3/a/@href').getall()
        
        self.logger.info(f"Found {len(articles_url)} articles")

        for url in articles_url:
            yield scrapy.Request(
                url=url, 
                headers=self.headers,
                callback=self.parse_article
            )

    def parse_article(self, response):

        self.logger.info(f"Parsing article: {response.url}")

        # extract title
        title = response.css("h1.read__title::text").get()

        # extract date
        date = response.css("div.read__time::text").get().split(" - ")[-1]

        # extract author
        author = response.css("div.credit-title-nameEditor::text")[-1].get().strip()

        # extract content
        content = response.css("div.read__content p").xpath(".//text()").getall()
        content = " ".join(content[:-1])

        if title and content:
            self.logger.info(f"Successfully extracted article: {title}")

            news_item = NewsItem()
        
            news_item["url"] = response.url
            news_item["title"] = title
            news_item["publish_date"] = date
            news_item["author"] = author
            news_item["content"] = content
            news_item["source"] = "detik.com"
            
            yield news_item

        else:
            self.logger.info("Failed to extract article")
