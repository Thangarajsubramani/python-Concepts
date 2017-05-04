class Country(models.Model):
    name = models.CharField(max_length=30)

class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country)
    population = models.PositiveIntegerField()
    
    
    
    
 ======================================================

from django.db.models import Sum

City.objects.aggregate(Sum('population'))
{'population__sum': 970880224}  # 970,880,224


City.objects.values('country__name') \
  .annotate(country_population=Sum('population')) \
  .filter(country_population__gt=50000000) \
  .order_by('-country_population')

[
  {'country__name': u'China', 'country_population': 309898600},
  {'country__name': u'United States', 'country_population': 102537091},
  {'country__name': u'India', 'country_population': 100350602},
  {'country__name': u'Japan', 'country_population': 65372000}
]

from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    url(r'^(\d+)/vote/$', views.vote),
)
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
