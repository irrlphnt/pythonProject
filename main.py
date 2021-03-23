import logging
import os
import pandas as pd
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
import csv
from googlesearch import search

logging.getLogger('scrapy').propagate = False


def get_urls(tag, n, language):
    urls = [url for url in search(tag, stop=n, lang=language)][:n]
    return urls


search_term = input("Please enter your search terms: ")
number_of_results = int(input("Please specify how many results you need: "))
file_name = str(search_term + ".csv")
# search_language = str(input("Please specify your search language. 'en' is te default") or "en")

with open(file_name, mode='w') as results_file:
    for url in (get_urls(search_term, number_of_results , 'en')):
        results_file.writelines(url + "\n")

#print(get_urls(search_term, number_of_results , 'en'))
