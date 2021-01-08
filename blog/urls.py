"""blog URL Configuration

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
from django.urls import path,include

from article import views

from django.conf import settings
from django.conf.urls.static import static
#from article.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    #Url_for da index diye kullanacağız.
    #path('',index,name="index"),
    path('',views.index,name="index"),
    #path('about/',views.about,name="detail"),
    #path('articles/deneme1/',views.about,name="detail"),
    #path('articles/',include("article.urls")),

    #dinamik url
    path('dashboard/<int:id>',views.dashboard,name="dashboard"),

    #Articleslı url gelince çalıştıracak
    path('articles/',include("article.urls")),

    #Burası ana URL diğer urllerde tanımladıklarımızı buraya gösteriyoruz.
    path('user/',include("user.urls")),
    #Bu şekilde tanımlayarak user/login user/logout user/register yukarıdaki halde tanımlamış olduk.

    path('about',views.about,name="about"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
