from django.urls import path
from users.views import (
    profile_view,
    profile_edit_view,
    profile_settings_view,
    profile_email_change,
    profile_email_verify,
    profile_delete_view,
)

urlpatterns = [
    path('', profile_view, name="profile"),
    path('edit/', profile_edit_view, name="profile-edit"),
    path('onboarding/', profile_edit_view, name="profile-onboarding"),
    path('settings/', profile_settings_view, name="profile-settings"),
    path('emailchange/', profile_email_change, name="profile-email-change"),
    path('emailverify/', profile_email_verify, name="profile-email-verify"),
    path('delete/', profile_delete_view, name="profile-delete"),
]
