from django.urls import path
from . import views
app_name = 'accounts'


urlpatterns = [
    path('profile',views.profile , name = 'profile'),
    path('profile/edit',views.edit_profile , name = 'profile_edit'),
    path('signup',views.signup , name = 'signup'),


]
