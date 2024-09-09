from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
