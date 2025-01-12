#Importe
from flask import Flask, request, render_template
from flask import send_from_directory
from search import Search
from bs4 import BeautifulSoup
import traceback
app = Flask(__name__) # Create a Flask web application instance

@app.errorhandler(500)
def internal_error(exception):
   return "<pre>"+traceback.format_exc()+"</pre>"

# Define the main page route, rendering the app.html template
@app.route('/')
def start():
    return render_template('app.html')

#result page with remplate result.html
@app.route('/result')
def result():
    search_word = request.args["keyword"] 
    search1 = Search(search_word)
    results = search1.get_results() 
    preview = []
    words = []

    # Extend the list to deal with several cases of which the user could write the keyword.
    for result in results:
        words = search_word.split(" ")
        il = len(words)
        for i in range(0,il):
            words.append(words[i][0].upper()+words[i][1:].lower())
        word_place = -1
        i = 0
        # Exteact the words that should be displayed in the preview of the side
        while word_place < 0 and i < len(words):
            first = words[i]
            word_place = result["content"].find(first)
            i += 1


        
        # Building individual previews for each result.
        first_place = word_place
        last_place = len(result["content"])
        if word_place -170 > 0:
            first_place = word_place - 170
        if word_place + 170 < len(result["content"]):
            last_place = word_place +170
        preview.append(result["content"][first_place:last_place])
    
    # Replace the keywords with html code that markes the the keywords
    for word in words:
        for i in range(len(preview)):
            preview[i] = preview[i].replace(word, f'<mark>{word}</mark>')
    return render_template('result.html', word=search_word, results=results, preview = preview)

