The project is about building a search engine consisting of four different parts 
1. A crawler, which is running indipendently of the search
2. An Index 
3. A query parser and search algorithm 
4. An user front end

Main Program - Searchengine:
The programm allows users to perform a search query. It uses the flask web framework for creating a web application and 
BeautifulSoup for HTML parsing. The application provides a userinterface to input search keywords and display the results.

Output:
The application results in two main views:
    The home page (app.html), which allows users to input search keywords.
    The results page (result.html), which displays search results along with contextual previews based on the input keyword.

----------------------------
Classes:

Crawler.py:
The Crawler class is designed to systematically crawl web pages starting from a specified URL. 
It retrieves links from each visited page, checks their validity, and compiles a list of URLs that can be indexed for further processing.
some important methods:
    crawl - crawls all subpages of the fixed start url and returns a list of proper URLs

Indexer.py:
The Indexer class is designed to create an index of documents from URLs using the Whoosh library. 
It retrieves content from web pages, extracts the title and body text, and stores this information in an index, 
enabling efficient searching and retrieval.

Search.py:
The Search class is designed to facilitate searching through a previously created index using the Whoosh library. 
It processes search keywords, retrieves relevant documents, and returns structured search results to the user.
some impotant methods:
    search - performs a search for documents containing a given keyword using the TFIDF scoring algorithm

----------------------------
In order to crawl and index the url again, execute refresh.py. Make sure that a folder "indexdir" exists.

----------------------------

Implemented creative Ideas or improvements:

- The user keywords for searching are displayed marked in the result page.
- A preview of each result, containing the keayword, is displayed on the result page.
- If you chose to open a link from the result page, a new tab is opened automatically.
- As a search engine extra, we implemented a tf-idf weighting sheme and if the keyword consists of several distinct words, 
then the words won't be considered as one. Instead they will be used as distinct keywords with a higher weithening if both keyword appear in one result.
