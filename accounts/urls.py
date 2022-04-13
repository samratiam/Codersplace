from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('coder-dashboard/', views.coder_dashboard, name="coder_dashboard"),
    path('coder-update/', views.coder_update, name="coder_update"),
    path('coder-delete/', views.coder_delete, name="coder_delete"),
    path('company-dashboard/', views.company_dashboard, name="company_dashboard"),
    # avoid views function named "logout"
    path('logout/', views.logout_user, name="logout"),
]
