from django.urls import path
from . import views

# the defaul route will be set as from first_app/ first then urlpatterns


# urlpatterns = [
#     path('sports/', views.sports_view),
#     path('finance/', views.finance_view),
# ]

urlpatterns = [
    path('<str:topic>/', views.news_view),
    path('<int:num1>/<int:num2>', views.add_view)
]
