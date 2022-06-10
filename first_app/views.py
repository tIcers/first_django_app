from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.

def simple_view(request):
    return render(request, 'first_app/example.html')  # render something to .html file

# the problem is everytime i want to make new route, i have to define new route.
# so it might be smarter to create dictionary and store all them in the dict


# articles = {
#     'sports': 'Sports page',
#     'finance': 'Finance page',
#     'politics': 'Politics page'
# }
#
#
# def news_view(request, topic):
#     try:
#         result = articles[topic]
#         return HttpResponse(articles[topic])
#     except:
#         raise Http404("404 GENERIC ERROR")  # for 404.html template.
#
#
# def add_view(request, num1, num2):
#     # domain.com/first_app/3/4 --> 7
#     add_result = num1 + num2
#     result = f"{num1}+{num2} ={add_result}"
#     return HttpResponse(str(result))
#
#
# # domain.com/first_app/0 --> domain.com/first_app/sports
# def num_page_view(request, num_page):
#     topics_list = list(articles.keys())  # ['sports','finance','politics']
#
#     topic = topics_list[num_page]
#
#     # webpage = reverse('topic_page', args=[topic])
#     return HttpResponseRedirect(reverse('topic_page', args=[topic]))
#
#
#     # response = redirect('/first_app/<str:topics>')
#     # return HttpResponse(response)
