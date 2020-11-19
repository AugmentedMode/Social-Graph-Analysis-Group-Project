from flask import Flask, render_template, request, flash, session, redirect, url_for
import gensim
import pickle

app = Flask(__name__)

with open('static/models/ingred_list.pkl', 'rb') as f:
        ingred_list = pickle.load(f)

with open('static/models/cook_book_v2.pkl', 'rb') as f:
    cook_book_v2 = pickle.load(f)

with open('static/models/cuisine_obj.pkl', 'rb') as f:
    cuisines = pickle.load(f)

@app.route('/')
def home():
    return render_template('home.html', ingred_list=ingred_list, cook_book_v2=cook_book_v2, cuisines=cuisines)


@app.route('/api/<string:ingedient>')
def model(ingedient):
    
    model = gensim.models.Word2Vec.load("static/models/model.model")
    results = model.wv.most_similar(ingedient)
    recommended_ingredients = [x[0] for x in results]
    return render_template('ingredient.html', ingedient=ingedient,
                            recommended_ingredients=recommended_ingredients, 
                            cook_book_v2=cook_book_v2)