from django.urls import path, include
from django.views.generic.base import RedirectView
from django.contrib import admin
from django.urls import include, re_path

admin.autodiscover()

import hello.views
import sign.views
# Author: Yuan Chen
# Version: 2020.07.29

app_name = 'main'  # here for namespacing of urls.
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)
urlpatterns = [

    #admin
    path('admin/', admin.site.urls),
    # path("", include('guest3.urls')),
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("register/", hello.views.register, name="register"),
    path("logout", hello.views.logout_request, name="logout"),
    path("login", hello.views.login_request, name="login"),
    path("all-building", hello.views.allbuilding, name="all-building"),
    path("newman-library", hello.views.newmanlibrary, name="newman-library"),
    path("togresson-hall", hello.views.togressonhall, name="togresson-hall"),
    path("mcbryde-hall", hello.views.mcbrydehall, name="mcbryde-hall"),
    re_path(r'^favicon\.ico$', favicon_view),
    path("about", hello.views.about, name="about"),
    path("faq", hello.views.faq, name="faq"),
    path("privacy-policy", hello.views.privacy, name="privacy-policy"),
    

    # api
    path('api/', include('api.urls')),
    path('guest/', include('guest3.urls')),
    # sign
    path('index/', sign.views.index),
    # path('', sign.views.index),
    path('accounts/login/',  sign.views.index),
    path('login_action/',  sign.views.login_action),
    path('event_manage/',  sign.views.event_manage),
    path('add_event/',  sign.views.add_event),
    path('guest_manage/',  sign.views.guest_manage),
    path('add_guest/',  sign.views.add_guest),
    path('search_name/',  sign.views.search_name),
    path('search_phone/',  sign.views.search_phone),
    path('sign_index/<int:event_id>/',  sign.views.sign_index),
    #path('sign_index2/<int:event_id>/', views.sign_index2),
    path('sign_index_action/<int:event_id>/',  sign.views.sign_index_action),
    path('logout/',  sign.views.logout),
]
