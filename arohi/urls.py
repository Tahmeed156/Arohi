from django.urls import path
from . import views

app_name = 'arohi'

urlpatterns = [
    # path('', views.order),
    # path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),

    path('', views.consumer_feed, name='consumer_feed',),
    path('feed/consumer/', views.consumer_feed, name='consumer_feed',),
    path('feed/investor/', views.investor_feed, name='investor_feed',),
    # path('feed/consumer/', views.consumer_feed, name='consumer_feed',),

]
