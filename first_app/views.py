from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound,Http404

# Create your views here.


# the problem is everytime i want to make new route, i have to define new route.
# so it might be smarter to create dictionary and store all them in the dict


articles = {
    'sports': 'Sports page',
    'finance': 'Finance page',
    'politics': 'Politics page'
}


def news_view(request, topic):
    try:
        result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 GENERIC ERROR") # for 404.html template.


def add_view(request, num1, num2):
    # domain.com/first_app/3/4 --> 7
    add_result = num1 + num2
    result = f"{num1}+{num2} ={add_result}"
    return HttpResponse(str(result))
