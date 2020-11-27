from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    # accounts를 이미 작성하고 넘어왔기 때문에 accounts/signup 이라고 친 것임
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout', logout, name='logout'),
]