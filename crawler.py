import requests 
from bs4 import BeautifulSoup

class Crawler:

    def __init__(self, prefix, start):
        """An crawler object crawls the web from a given start url.
        for_index_urls: list of all proper urls"""
        self.prefix = prefix # for example: 'https://vm009.rz.uos.de/crawl/'
        self.start_url = self.prefix + start #for example: start = 'index.html'
        self.for_index_urls = []

    def fix_urls(self,urls):
        """check if url (href) not empty and create a proper url starting with http
        important: may still produce not existing url"""
        prefix = self.get_prefix()
        urls_http = []

        for url in urls:
            if url and url[:4] == "http":
                urls_http.append(url)
            elif url:
                urls_http.append(prefix+url)
        return urls_http

    def get_for_index_urls(self):
        return self.for_index_urls

    def get_prefix(self):
        return self.prefix
    
    def get_start_url(self):
        return self.start_url

    def crawl(self):
        """crawls all pages with the same prefix starting from start_url 
        return list of proper urls"""
        agenda = [self.get_start_url()]
        crawled_urls = []
        for_index_urls = []
        prefix = self.get_prefix()

        while agenda:
            url = agenda.pop(0)
            not_existing_server = False

            #prevents accessing urls which are not existing on any server
            try:
                r = requests.get(url)
            except:
                not_existing_server = True

            #crawl the url if url: exists, status_code=200, prefix the same, leads to an html document 
            if not_existing_server == False and r.status_code == 200 and prefix == url[:(len(prefix))] and ("text/html" in r.headers.get('Content-Type', '')):
                 
                for_index_urls.append(url)

                #crawl: find all links to other pages by looking for href in <a>...</a>
                soup = BeautifulSoup(r.content, 'html.parser')
                new_urls = self.fix_urls([link.get('href') for link in soup.find_all('a')])

                for an_url in new_urls:
                    if an_url not in crawled_urls and an_url not in agenda:
                        agenda.append(an_url)

            crawled_urls.append(url)

        self.get_for_index_urls().extend(for_index_urls)
        print("Crawling finished.")
        return for_index_urls

        
