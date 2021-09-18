# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import MapCompose, TakeFirst, Identity, Join
from w3lib.html import remove_tags
import unicodedata
def cleaning(html_text):
    z=remove_tags(html_text)
    y = ' '.join(z.split())
    return y

class CasesItem(scrapy.Item):
     content = scrapy.Field(input_processor=MapCompose(cleaning), output_processor=Identity())

     