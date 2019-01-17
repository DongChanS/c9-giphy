from flask import Flask,render_template,request
import giphy

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/search',methods=["POST"])
def search():
    query = request.form['query']
    #print(query)
    search_url = giphy.make_url(query)
    parsed_dic = giphy.request_and_parse(search_url)
    images = giphy.get_images(parsed_dic)
    return render_template('search.html',images=images,query=query)