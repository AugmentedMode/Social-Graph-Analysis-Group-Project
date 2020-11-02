from flask import Flask, render_template, request, flash, session, redirect, url_for
import gensim
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    with open('ingred_list.pkl', 'rb') as f:
        ingred_list = pickle.load(f)
    return render_template('home.html', ingred_list=ingred_list)


@app.route('/model')
def model():
    model = gensim.models.Word2Vec.load("model.model")
    results = model.wv.most_similar('romain lettuc')
    recommended_ingredients = [x[0] for x in results]

    return recommended_ingredients