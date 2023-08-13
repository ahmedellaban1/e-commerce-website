from django.urls import path
from .views import profile_details, update_profile
app_name = 'accounts'
urlpatterns = [
    path('profile', profile_details, name='profile-details'),
    path('profile/edit', update_profile, name='update-profile'),

]
