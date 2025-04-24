import scrapy


class ProductItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    image_url = scrapy.Field()
    rating = scrapy.Field()
    description = scrapy.Field()
