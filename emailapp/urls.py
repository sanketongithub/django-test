from django.contrib.auth.decorators import login_required
from django.urls import path

from emailapp.views import OrderListJson
from . import views

urlpatterns = [

path('',views.index, name="index"),
path('send-email',views.home, name='send-email'),
path('funtest',views.funtest, name='funtest'),
path('email-form',views.emailform, name='emailform'),

path('form',views.load_form),
path('data_test',views.data_test),
#path(r'^my/datatable/data/$', login_required(OrderListJson.as_view()), name='order_list_json'),
#path(r'^my/datatable/data/$', OrderListJson.as_view(), name='order_list_json'),
path('view_testing',OrderListJson.as_view()),
#path(r'^ajax_calls/search/', views.autocompleteModel),

]