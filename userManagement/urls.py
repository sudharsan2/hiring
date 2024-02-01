
from django.urls import path
from .views import RegistrationView, LoginView, GetAllUsersView, GetAllRolesView,add_user_roles
urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('signin/', LoginView.as_view(), name='login'),
    path('getAllUsers/', GetAllUsersView.as_view(), name='getAllUsers'),
    path('getAllRoles/', GetAllRolesView.as_view(), name='getAllRoles'),
    path('addUserRoles/',add_user_roles.as_view(), name = 'adduseroles')
]
