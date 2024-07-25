from django.urls import path
from .views import *

urlpatterns = [
        path('', home, name='home') 
#     path('register/',register, name='register'),
#     path('login/', login_view, name='login'),
#     path('logout/', logout_view, name='logout'),
#     path('societies/', societies, name='societies'),
#     path('societies/<int:society_id>/', society_detail, name='society_detail'),
#     path('notices/', notices, name='notices'),
#     path('events/', events, name='event')

]