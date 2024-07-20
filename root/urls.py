
from django.contrib import admin
from account.urls import *
from root import settings
from food import urls



from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
path('', include('account.urls')),
path('', include('food.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
