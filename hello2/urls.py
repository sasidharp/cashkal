from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'user.views.home', name='home'),
    url(r'^home', 'user.views.home', name='home'),
    url(r'^logout', 'user.views.logout1', name='logout1'),
    url(r'^cash/', 'user.views.cash', name='cash'),
    url(r'^list/', 'user.views.cashlist', name='cashlist'),
    url(r'^alist/', 'user.views.actuallist', name='cashlist'),
    url(r'^calen/', 'user.views.calendar', name='calendar'),
    url(r'^calop/', 'user.views.calenoption', name='option'),
    url(r'^categories/', 'user.views.categories', name='categories'),
#     url(r'^payment/', 'user.views.payment', name='cash'),
#     url(r'^types/', 'user.views.types', name='cash'),
#     url(r'^categ/', 'user.views.newcateg', name='newcateg'),
    url(r'^categ/', 'user.views.corrections', name='newcateg'),
    url(r'^actuals/', 'user.views.cashactuals', name='cashactuals'),
    url(r'^convert/', 'user.views.convertactual', name='convertactual'),
    url(r'^launcher/', 'user.views.launcher', name='launcher'),
    url(r'^events/', 'user.views.events', name='events'),
    url(r'^addcateg/', 'user.views.addcateg', name='addcateg'),
    url(r'^chartdata/', 'user.views.overallchartdata', name='overallchartdata'),
    url(r'^chartdataout/', 'user.views.overallchartdata_out', name='overallchartdata'),
    url(r'^chartactual/', 'user.views.overallchartactual', name='overallchartactual'),
    url(r'^chartactualout/', 'user.views.overallchartactual_out', name='overallchartactual'),
    url(r'^trend/', 'user.views.trend', name='trend'),
    url(r'^cashflow/', 'user.views.chartbydirection', name='chartbydirection'),
    
    url(r'^pie/', 'user.views.pie', name='pie'),
    url(r'^report/', 'user.views.report', name='report'),
    url(r'^register/', 'user.views.register', name='register'),
 
    url(r'^contact/', 'user.views.contact', name='contact'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    