from indexer import Indexer
from crawler import Crawler

"""executing this file will crawl the provided url and index it (again);
make sure that a folder 'indexdir' exists!"""

crawler1 = Crawler("https://cogsci-journal.uni-osnabrueck.de/","")
liste = crawler1.crawl()

indexer1 = Indexer()
indexer1.index_documents(liste)

print("Crawling and Indexing finished.")

