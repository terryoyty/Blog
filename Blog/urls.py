"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('app/', include('app.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views import static
from Blog.settings.common import MEDIA_ROOT
from app.plugins import UploadQiniuyunView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 媒体文件路由
    re_path(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),

    path('', include('app.urls')),
    path('', include('comments.urls')),

    # mdeditor内置本地上传路由
    # path('mdeditor/', include('mdeditor.urls')),
    # mdeditor配置七牛云上传路由
    path('mdeditor/uploads/', UploadQiniuyunView.as_view(), name='uploads'),

    path('search/', include('haystack.urls')),


]
