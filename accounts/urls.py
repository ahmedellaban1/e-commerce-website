from django.urls import path
from .views import profile_details, update_profile, signup_view
app_name = 'accounts'
urlpatterns = [
    path('register/', signup_view, name='sign-up'),
    path('profile', profile_details, name='profile-details'),
    path('profile/edit', update_profile, name='update-profile'),

]
