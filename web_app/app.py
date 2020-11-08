from flask import Flask, render_template, request, flash, session, redirect, url_for
import gensim
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    with open('static/models/ingred_list.pkl', 'rb') as f:
        ingred_list = pickle.load(f)
    return render_template('home.html', ingred_list=ingred_list)


@app.route('/api/<string:ingedient>')
def model(ingedient):
    
    model = gensim.models.Word2Vec.load("static/models/model.model")
    results = model.wv.most_similar(ingedient)
    recommended_ingredients = [x[0] for x in results]
    return render_template('ingredient.html', ingedient=ingedient,
                            recommended_ingredients=recommended_ingredients)