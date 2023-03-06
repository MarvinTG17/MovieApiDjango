from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title= "Movie API",
        default_version= "v1",
        description= "API para recordar Django",
        terms_of_service= "https://google.com",
        contact= openapi.Contact(email="taipe.marvin17@gmail.com"),
        license= openapi.License(name="MIT")
    ),
    public= True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include('movie.urls')),
    path('users/', include('users.urls')),
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0), name='swagger-docs'),
    path('rents/', include('rent.urls')),
]
