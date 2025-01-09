from whoosh.index import create_in, open_dir
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import *
from bs4 import BeautifulSoup
import requests 

class Indexer:

    # Initializes the indexer, sets up the schema with fields for title, content, and URL, and creates a writer for adding documents to the index.
    def __init__(self):
        self.schema = Schema(title=TEXT(stored=True), content=TEXT(stored = True), url = ID(stored = True))
        self.ix = create_in("indexdir", self.schema)
        self.writer = self.ix.writer()

    
    # Fetches content from a list of URLs, parses the HTML to extract the title and text, and adds these as documents to the index if valid data is present.
    def index_documents(self,urls):
        for url in urls:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            content = soup.get_text(" ", strip=True)

            if soup.title and content and url:
                self.writer.add_document(title=str(soup.title.string), content = content, url = url)

        self.writer.commit()
        print("Indexing finished")
    # Retrieves and prints all indexed documents from the searcher to display stored fields.
    def display(self):   
        with open_dir("indexdir").searcher() as searcher:
            for doc in searcher.all_stored_fields():
                print(doc)
    
    

