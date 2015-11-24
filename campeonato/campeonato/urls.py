from django.conf.urls import patterns, include, url
from django.contrib import admin

from campeonatoapp.views import IndexView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'loginsocial.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url('', include('social.apps.django_app.urls', namespace= 'social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view()),
    url(r'^salir/$', 'campeonatoapp.views.LogOut'),
    url(r'^index/', 'campeonatoapp.views.inde'),
    url(r'^jugador/', 'campeonatoapp.views.jugad'),    
    url(r'^equipo/', 'campeonatoapp.views.equip'),
    url(r'^campeonato/', 'campeonatoapp.views.campeonat'),

)
