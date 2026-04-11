from django.urls import path
from .views import login_page, signup_page, signup, api_login

urlpatterns = [
    path('', login_page, name='login_page'),
    path('signup/', signup_page, name='signup_page'),
    path('do-signup/', signup, name='do_signup'),
    path('do-login/', api_login, name='do_login'),   
]

# from django.urls import path
# from .views import login_page, signup_page, signup, api_login

# urlpatterns = [
#     path('', login_page, name='login_page'),
#     path('signup/', signup_page, name='signup_page'),
#     path('login/', api_login, name='do_login'),
#     path('do-signup/', signup, name='do_signup'),
#     path('do-login/', api_login, name='do_login'),
# ]