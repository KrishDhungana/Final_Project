import scrapy
import csv
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from webscrape import LogReader

class spider_three(scrapy.Spider):
## First Read through our dataset and select the url's
    name = 'spider_three'

    def start_requests(self):
        csv_file_path = './datasets/phishing_dataset.csv'
        with open(csv_file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                url = row[0]
                yield scrapy.Request(url=url, callback=self.parse)

## Scrape the URL IP address
    def parse(self, response):
        ip_address = response.json().get('origin')
        self.log(ip_address)

def run_spider_three(self):
    process = CrawlerProcess(get_project_settings())
    process.crawl(spider_three)
    process.start()
    process.stop()