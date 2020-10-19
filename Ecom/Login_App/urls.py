from django.urls import path
from Login_App import views

app_name = "Login_App"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_, name='login'),
    path('logout/',views.logOut,name='logout'),
    path('profile/',views.edit_profile,name='profile'),

]
