
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include, reverse

from rest_framework import routers

from ads import views
from users.views import LocationViewSet

router = routers.SimpleRouter()
router.register(r'location', LocationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('cat/', views.CategoryView.as_view()),
    path('cat/<int:pk>', views.CategoryDetailView.as_view()),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view()),
    path('ad/', views.AdView.as_view()),
    path('ad/<int:pk>', views.AdDetailView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image', views.AdUploadImageView.as_view()),
    path('user/', include('users.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
