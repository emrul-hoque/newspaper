from django.urls import path
from .views import SignUpView
from .views import logout_view


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('users/logout/', logout_view, name='logout'),
]