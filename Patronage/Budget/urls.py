from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bjp-chart', views.bjpchart, name='bjpchart'),
    path('ncp-chart', views.ncpchart),
    path('bengaluru_bjp', views.bengaluru_bjp),
    path('kolkata_bjp', views.kolkata_bjp),
    path('hyderabad_bjp', views.hyderabad_bjp),
    path('mumbai_bjp', views.mumbai_bjp),
    path('delhi_bjp', views.delhi_bjp),
    path('bengaluru_ncp', views.bengaluru_ncp),
    path('kolkata_ncp', views.kolkata_ncp),
    path('hyderabad_ncp', views.hyderabad_ncp),
    path('mumbai_ncp', views.mumbai_ncp),
    path('delhi_ncp', views.delhi_ncp),
    path('mine', views.mine),
    path('blog', views.blog)

]