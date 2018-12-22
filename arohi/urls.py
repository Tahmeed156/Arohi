from django.urls import path
from . import views

app_name = 'arohi'

urlpatterns = [
    # path('', views.order),

    path('', views.home, name='home_page',),

    path('contact', views.contact, name='contact_page'),

    path('feed/', views.feed, name='feed'),
    path('feed/<int:page>', views.feed, name='feed'),
    # path('feed/consumer/', views.consumer_feed, name='consumer_feed',),
    # path('feed/consumer/<int:page>', views.consumer_feed, name='consumer_feed',),
    # path('feed/investor/', views.investor_feed, name='investor_feed',),
    # path('feed/investor/<int:page>', views.investor_feed, name='investor_feed',),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.sign_up, name='signup'),


    path('dashboard/', views.dashboard, name='dashboard'),
    # path('dashboard/consumer', views.dashboard_consumer, name='consumer_dashboard'),
    # path('dashboard/investor', views.dashboard_investor, name='investor_dashboard'),
    # path('dashboard/entrepreneur', views.dashboard_entrepreneur, name='entrepreneur_dashboard'),

    path('product/add', views.add_product, name='add_product'),
    path('product/buy', views.buy_product, name='buy_product'),

    path('profiles/consumer', views.profile_consumer, name='profile_consumer'),
    path('profiles/entrepreneur', views.profile_entrepreneur, name='profile_entrepreneur'),
    path('profiles/investor', views.profile_investor, name='profile_investor'),
]
