from django.shortcuts import render


# Create your views here.
def semantic(request):
    if request.method == 'POST':
        print(request.POST)
        text_review = request.POST['review']
        if text_review == ['']:
            return render(request, 'semantic/review.html')
        return render(request, 'semantic/results.html', context={'probability': 0,
                                                                'prediction': 'positive',
                                                                'text_review': text_review
                                                                })
    else:
        return render(request, 'semantic/description.html')

def thanks(request):
    print(request.POST)
    return render(request, 'semantic/thanks.html')

def review(request):
    if request.method == 'POST':
        text_review = request.POST['review']
        if len(text_review) < 15:
            return render(request, 'semantic/review.html', context={'value_field':'Введите более 15 символов...'})
        else:

            return render(request, 'semantic/results.html',context={'probability': 0,
                                                                'prediction': 'positive',
                                                                'text_review': text_review
                                                                })
    else:
        return render(request, 'semantic/review.html',context={'value_field':'Только на английском языке...'})
    # return render(request, 'semantic/review.html')