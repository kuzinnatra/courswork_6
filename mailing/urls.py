from django.urls import path
from mailing.apps import MailingConfig
from mailing.views import index, ClientCreateView, ClientListView, ClientDetailView, ClientUpdateView, ClientDeleteView

app_name = MailingConfig.name
urlpatterns = [
    path('', index,),
    path('client/create/', ClientCreateView.as_view(), name='client_create'),
    path('client/list/', ClientListView.as_view(), name='client_list'),
    path('client/view/<int:pk>/', ClientDetailView.as_view(), name='client_view'),
    path('client/edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('client/delete/,<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

]