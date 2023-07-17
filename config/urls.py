from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    
    # Admin
    path('admin/', admin.site.urls),
    
    # User model
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Local apps
    # Create patterns to accounts and api, then uncomment!
    #path('accounts/', include('accounts.urls')),
    path('', include('api.urls')),
    
]
