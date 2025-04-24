import scrapy


class NewsItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    publish_date = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    source = scrapy.Field()
