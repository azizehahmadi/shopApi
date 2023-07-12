from django.urls import path
from user_app.rest.views import RegisterUserView, UserLogin, \
    UserProfileView, ChangePasswordUserView, SendPasswordRestEmailView, UserPasswordRestView


urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('login/', UserLogin.as_view(), name='login-user'),
    path('profile/', UserProfileView.as_view(), name='profile-user'),
    path('change-password/', ChangePasswordUserView.as_view(), name='change-password'),
    path('send-password-rest-email/', SendPasswordRestEmailView.as_view(), name='send-password-rest-email'),
    path('user-password-rest/<uid>/<token>/', UserPasswordRestView.as_view(), name='user-password-rest'),
]
