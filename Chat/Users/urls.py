from django.urls import path
from Users.views import *

urlpatterns = [
    path('',profile_view,name="profile"),
    path('edit/',profile_edit_view,name="profile-edit"),
    path('settings/',settings_view,name='settings'),
    path('emailchange/',profile_emailchange,name="profile-emailchange"),
    path('email_verify/',profile_email_verify,name='profile_email_verify'),
    path('account_delete/',account_delete,name='account_delete'),
]
