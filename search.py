#Imports
from whoosh.qparser import QueryParser
from whoosh.index import open_dir
from whoosh import scoring
from indexer import Indexer

class Search:

    def __init__(self, search_words):
        """with the initialization of an Object from search, the search method with the respective parameter is called"""
        self.indexdir = open_dir("indexdir")
        self.search_words = search_words
        self.results = self.search(search_words)
        
    def get_search_words(self):
        return self.search_words
    
    def get_results(self):
        return self.results
    
    def set_results(self, result_list):
        self.results = result_list

    def search(self, keys: str):
        """the search term is split into its parts and the index is searched for every term seperatly. 
        The scoring scheme is tf-idf (a popular weighting scheme).
        The result object is updated and extended with every searchterm"""
        
        qp = QueryParser("content", schema=self.indexdir.schema)
        keywords = keys.split(" ")
        results = None  
        #using with to access documents
        with self.indexdir.searcher(weighting=scoring.TF_IDF()) as searcher:
            for keyword in keywords:
                q = qp.parse(keyword)
                current_results = searcher.search(q)
                if results is None:
                    results = current_results
                else:
                    #to get to one list for the whole search term (the terms do not have to occur next to each other)
                    results.upgrade_and_extend(current_results)
            #weighting and structuring of the results (pages with all search terms should be displayed at the top, pages with a part of the search terms lower at the page)
            weighted_results = []
            for result in results:
                stored_fields = searcher.stored_fields(result.docnum)
                weighted_results.append({
                    "title": stored_fields.get("title", ""),
                    "content": stored_fields.get("content", ""),
                    "url": stored_fields.get("url", "")
                })
        #returns a list of the weighted results
        return weighted_results
