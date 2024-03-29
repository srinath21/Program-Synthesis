"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite import views as views1
from searchApp import views
urlpatterns = [
    url(r'^$', views1.Startpage),
    #url(r'^admin/', admin.site.urls),
    url(r'^welcome/$', views1.Startpage),
    url(r'^login/$', views.LoginPage),
    url(r'^register/$', views.Register),
    url(r'^search/$',views.Search),
    url(r'^logout/$',views.Logout),
    url(r'^searchresult/$',views.SearchResult),
    url(r'^insertCode/$', views.InsertCode),
    url(r'^user/settings/$',views.Settings),
    url(r'^user/profile/$',views.Profile),
    url(r'^addcode/$',views.addCode),
    url(r'^feedback/$', views.feedback),
    url(r'^execute/$', views.Execute),
    url(r'^passchange/$', views.password),
]
