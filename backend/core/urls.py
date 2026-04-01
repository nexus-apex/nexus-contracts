from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('contracts/', views.contract_list, name='contract_list'),
    path('contracts/create/', views.contract_create, name='contract_create'),
    path('contracts/<int:pk>/edit/', views.contract_edit, name='contract_edit'),
    path('contracts/<int:pk>/delete/', views.contract_delete, name='contract_delete'),
    path('parties/', views.party_list, name='party_list'),
    path('parties/create/', views.party_create, name='party_create'),
    path('parties/<int:pk>/edit/', views.party_edit, name='party_edit'),
    path('parties/<int:pk>/delete/', views.party_delete, name='party_delete'),
    path('amendments/', views.amendment_list, name='amendment_list'),
    path('amendments/create/', views.amendment_create, name='amendment_create'),
    path('amendments/<int:pk>/edit/', views.amendment_edit, name='amendment_edit'),
    path('amendments/<int:pk>/delete/', views.amendment_delete, name='amendment_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
