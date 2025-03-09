from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse

# Health check for root URL
def home_view(request):
    return JsonResponse({"message": "Backend is working!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include the API app's URLs
    path('', home_view),                # Added this to handle root URL
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
