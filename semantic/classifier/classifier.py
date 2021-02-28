import pickle
import os
from vectorizer import _vect
from database import DataBase

cur_dir = os.path.dirname(__file__)
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects//model_clf_sgd.pckl'), 'rb'))

name_db = os.path.join(cur_dir, 'reviews.sqlite3')

def classify(document):

    X = _vect.transform([document])
    y = clf.predict(X)[0]
    proba = clf.predict_proba(X).max()
    return y, proba

def train(document, y):
    X = _vect.transform([document])
    clf.partial_fit(X, [y])

def push_review(review, sentiment):
    db = DataBase(name_db=name_db, name_tab='reviews')
    db.push_review(review,sentiment)
