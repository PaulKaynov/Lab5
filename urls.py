from django.conf.urls import url, include
from django.contrib import admin
from Lab5.views import HotelsView, HotelView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hotels/$', HotelsView.as_view()),
    url(r'^hotel/(?P<id>\d+)$', HotelView.as_view(), name='hotel_url')
]

