from django.conf.urls import url
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

# SET THE NAMESPACE!
app_name = 'myapp'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^user/',views.user,name='user'),
    url(r'^usermap/',views.mapuser,name='usermap'),
    url(r'^viewdata/',views.viewdata,name='viewdata'),
    url(r'^analyse/',views.dashboard,name='analyse')
]
