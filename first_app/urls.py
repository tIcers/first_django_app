from django.urls import path
from . import views

# the defaul route will be set as from first_app/ first then urlpatterns


# urlpatterns = [
#     path('sports/', views.sports_view),
#     path('finance/', views.finance_view),
# ]

urlpatterns = [
    path('<int:num_page>', views.num_page_view),
    path('<str:topic>/', views.news_view, name='topic_page'),

]
