"""ourchat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from ourchat_app import views
from ourchat import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_view),
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('chat/create', views.create_chat_view),
    path('chat/<int:chat_id>', views.chat_view),
    path('chat/<int:chat_id>/invite', views.chat_invite_view),
    path('chat/<int:chat_id>/members', views.chat_members_view),
    path('chat/<int:chat_id>/kick', views.chat_kick_view),
    path('chat/<int:chat_id>/updates', views.chat_updates_view),
    path('register', views.register_view),
    path('chats', views.chats_view),
    path('user/<str:username>', views.userpage_view),
]
