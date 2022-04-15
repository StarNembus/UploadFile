from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from .views import UploadFileViewSet

urlpatterns = [

    path('files_list/', UploadFileViewSet.as_view()),

]
