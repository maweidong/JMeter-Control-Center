from django.conf.urls import include
from django.urls import path
# from django.contrib import admin
# from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='jltc.index'),
    path('analyzer', include('analyzer.urls'), name='jltc.analyzer'),
    # url(r'^admin/', admin.site.urls),
    # url(r'^online/', include('online.urls')),
    # url(r'^controller/', include('controller.urls')),
    # url(r'^administrator/',
    #     include('administrator.urls')),
]
# + static(
    # settings.STATIC_URL, document_root=settings.STATIC_URL)
