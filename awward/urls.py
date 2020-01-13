from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$',views.index,name='index'),
    url('^today/$',views.projects_today,name='projectToday'),
    url('^profile/$',views.profile,name='profile'),
    url(r'^project/(\d+)',views.project,name='project'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_projects,name = 'pastprojects'),
    url(r'^ajax/projectsletter/$', views.projectsletter, name='projectsletter'),
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',
        views.MerchDescription.as_view())

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

