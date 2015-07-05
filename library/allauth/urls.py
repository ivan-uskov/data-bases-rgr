from django.conf.urls import url, patterns, include


urlpatterns = [
    url(r'', include('allauth.account.urls'))
]