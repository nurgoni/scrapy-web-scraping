run-detik:
	PYTHONPATH=src scrapy crawl detik -o data/news/detik.json

run-kompas:
	PYTHONPATH=src scrapy crawl kompas -o data/news/kompas.json