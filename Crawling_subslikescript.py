from typing import Iterable

import scrapy
from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

# Define the spider class inheriting from CrawlSpider for rule-based crawling
class TranscriptsSpider(CrawlSpider):

    # Name of the spider
    name = "transcripts"

    # Domain restriction to avoid crawling outside subslikescript.com
    allowed_domains = ["subslikescript.com"]
    #start_urls = ["https://subslikescript.com/movies_letter-X"]

    # Custom settings for the spider
    custom_settings = {
        'DOWNLOAD_DELAY': 0.5,  # # Sets a download delay of 0.5 seconds to prevent overwhelming the server
    }

    # User agent to mimic a browser, which helps avoid getting blocked
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'

    # Start the crawling process by requesting the first page with movies starting with 'X'
    def start_requests(self):
        yield scrapy.Request(url='https://subslikescript.com/movies_letter-X',
                             headers={'user-agent':self.user_agent})

    # Rules for link extraction and crawling
    # Rule 1: Extract links to individual movie pages and call parse_item to scrape data
    # Rule 2: Handle pagination by following the 'next' page link
    rules = (Rule(LinkExtractor(restrict_xpaths=("//ul[contains(@class,'scripts-list')]//li/a")), callback="parse_item", follow=True, process_request='set_user_agent'),
             Rule(LinkExtractor(restrict_xpaths=("(//a[@rel='next'])[1]")), process_request='set_user_agent')) # Pagination

    # Method to ensure each request has the custom user agent
    def set_user_agent(self, request, spider):
        request.headers['User-Agent']=self.user_agent
        return request

    # Method to parse and extract the required information from each movie page
    def parse_item(self, response):
        # Extracting the main article section containing the movie data
        article = response.xpath("//article[contains(@class,'main-article')]")

        # Yield a dictionary containing the scraped data (title, plot, transcript, and URL)
        yield{
            'title':article.xpath("./h1/text()").get(),
            'plot':article.xpath("./p/text()").get(),
            'transcript':article.xpath("./div[contains(@class,'full-script')]/text()").getall(),
            'url':response.url
        }
