import scrapy
from ..items import CasesItem
from scrapy.loader import ItemLoader



class CastesSpider(scrapy.Spider):
    name = 'castes'
    page_number=50
    allowed_domains =  ['kenyalaw.org']
    start_urls = ['http://kenyalaw.org/caselaw/cases/classes/2/']

    custom_settings={
        'DOWNLOAD_DELAY':2,
        'USER_AGENT': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    }

    def parse(self, response):
        for url in response.xpath('//a[@class=" show-more pull-right"]/@href'):
            yield response.follow(url.get(), callback=self.parse_content)

        #scrape all the pages
        # next_page = response.css('li.next a::attr("href")').get()
        # if next_page is not None:
        #    yield response.follow(next_page, callback=self.parse)    
        
        # scrape first 10 pages
        next_page = 'http://kenyalaw.org/caselaw/cases/classes/2/'+ str(CastesSpider.page_number) + '/'
        if CastesSpider.page_number <= 450:
            CastesSpider.page_number += 50
            yield response.follow(next_page, callback=self.parse)


    def parse_content(self, response):
        l=ItemLoader(item = CasesItem(), selector=response)

        l.add_css('content','div.case_content')       
            
        yield l.load_item()        
              
       