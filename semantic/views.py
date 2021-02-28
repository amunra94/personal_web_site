from django.shortcuts import render
import re
import os
import sys

cur_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(cur_dir, 'classifier'))
import classifier


# Create your views here.
def semantic(request):
    return render(request, 'semantic/description.html')


def thanks(request):
    print(request.POST)
    return render(request, 'semantic/thanks.html')


def review(request):
    labels = {0: 'negative', 1: 'positive'}
    if request.method == 'POST':
        text_review = request.POST['review']
        print(text_review)
        matching = bool(re.match("^[а-яА-Я]*$", text_review))
        print(matching)
        if len(text_review) < 15:
            return render(request, 'semantic/review.html', context={'value_field': 'Enter more than 15 symbols...'})
        else:
            if matching:
                return render(request, 'semantic/review.html', context={'value_field': 'Enter only English letters...'})
            else:
                prediction, probability = classifier.classify(text_review)
                classifier.push_review(text_review, prediction)
                probability = round(probability,3)
                prediction_label = labels[prediction]
                return render(request, 'semantic/results.html', context={'probability': probability,
                                                                         'prediction': prediction_label,
                                                                         'text_review': text_review
                                                                         })
    else:
        return render(request, 'semantic/review.html', context={'value_field': 'Only english language...'})
        # return render(request, 'semantic/review.html')
