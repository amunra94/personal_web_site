from sklearn.feature_extraction.text import HashingVectorizer
import re
import os
import pickle


_curr_dir = os.path.dirname(__file__)

STOP_WORDS = pickle.load(open(os.path.join(_curr_dir,'pkl_objects','stopwords.pckl'), 'rb'))

def tokenizer(text):
    text = re.sub('<[^>]*>', '', text)
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text.lower())
    text = re.sub('[\W]+', ' ', text.lower()) + ' '.join(emoticons).replace('-', '')
    tokenized = [word for word in text.split() if word not in STOP_WORDS]
    return tokenized

_vect = HashingVectorizer(decode_error='ignore',
                          n_features=2**21,
                          preprocessor=None,
                          tokenizer=tokenizer)