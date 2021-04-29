from django.urls import path


from . import views

urlpatterns = [
    path('loans/', views.LoanListView.as_view(), name='app_loan_list'),
    path('loans/refresh', views.loan_refresh),
    path('loans/config/import', views.import_loan_config)
]
