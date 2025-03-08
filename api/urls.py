from django.urls import path
from .views import RegisterView, LoginView, ProtectedView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import SaveHealthDataView  # ✅ Correct class-based import


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('protected/', ProtectedView.as_view(), name='protected'),
    path("save-health-data/", SaveHealthDataView.as_view(), name="save_health_data"),  # ✅ Fix: Use class-based view
]

