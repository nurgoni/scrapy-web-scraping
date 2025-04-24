import scrapy

from scraper.items import NewsItem


class DetikSpider(scrapy.Spider):
    name = "detik"
    allowed_domains = ["www.detik.com"]

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

    def __init__(
            self, 
            keywords: str = None,
            num_articles: int = 5,
            *args, 
            **kwargs
        ):
        """
        
        """
        super().__init__(*args, **kwargs)
        self.keywords = str(keywords)
        self.num_articles = int(num_articles)

    def start_requests(self):
        """
        
        """
        
        if not self.keywords:
            self.logger.error("No keywords provided")
            return
        
        keywords = self.keywords.split(",")
        for keyword in keywords:
            url = f"https://www.detik.com/search/searchall?query={keyword.strip()}"

            self.logger.info(f"Requesting URL: {url}")
            self.logger.info(f"start request for keyword: {keyword.strip()}")

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
    
    async def errback(self, failure):
        page = failure.request.meta.get("playwright_page")
        await page.close()
    
    def parse_search(self, response):
        """
        
        """
        self.logger.info(f"Parsing search results from {response.url}")
        articles = response.css("article.list-content__item")

        for article in articles:
            link = article.css("div.media__text h3.media__title a::attr(href)").get()
            if not link:
                self.logger.warning(f"No link found for article: {article}")
                continue
                
            title = article.css("div.media__text h3.media__title a::text").get()
            date = article.css("div.media__date span::attr(title)").get()

            yield scrapy.Request(
                url=link,
                headers=self.headers,
                meta={
                    "title": title,
                    "date": date,
                },
                callback=self.parse_article,
            )
    
    def parse_article(self, response):
        """
        
        """
        title = response.meta.get("title")
        date = response.meta.get("date")

        author = response.css("div.detail__author::text").get()

        contents = response.css("div.detail__body-text.itp_bodycontent p::text").getall()
        if not contents:
            self.logger.warning(f"No content found for article: {response.url}")
            contents = "No content available"
        else:
            contents = [content.strip() for content in contents if content.strip() != "SCROLL TO CONTINUE WITH CONTENT"]
            contents = " ".join(contents)

        news_item = NewsItem()
        
        news_item["url"] = response.url
        news_item["title"] = title
        news_item["publish_date"] = date
        news_item["author"] = author
        news_item["content"] = contents
        news_item["source"] = "detik.com"
        
        yield news_item
