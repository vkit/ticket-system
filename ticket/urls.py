from django.conf.urls import url
from .import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^test/$', views.TestingView.as_view(), name='test'),
    url(r'^pdf/$', views.GenerateView.as_view(), name='pdf'),
    url(r'^list/$', views.TicketView.as_view(), name='list'),
    url(r'^pending/$', views.PendingStatusView.as_view(), name='pending'),
    url(r'^solved/$', views.SolvedStatusView.as_view(), name='solved'),
    url(r'^closed/$', views.ClosedStatusView.as_view(), name='closed'),
    url(r'^(?P<pk>\d+)/detail/$', views.TicketDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.TicketupdateView.as_view(),
        name='update'),
    url(r'^(?P<pk>\d+)/comment/$', views.TicketCommentView.as_view(),
        name='comment'),
    url(r'^$', 'django.contrib.auth.views.login',
        {'template_name': 'base1.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'base.html'}, name='logout'),
    url(r'^register/$', CreateView.as_view(template_name='registration/register.html',form_class=UserCreationForm, success_url='/ticket/'), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)