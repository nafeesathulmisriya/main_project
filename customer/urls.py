from django.shortcuts import render
from django.urls import path
from . import views
from insurance import views as insurance_views 
from django.contrib.auth.views import LoginView
from .views import upload_claim


urlpatterns = [
    path('customerclick', views.customerclick_view,name='customerclick'),
    path('customersignup', views.customer_signup_view,name='customersignup'),
    path('customer-dashboard', views.customer_dashboard_view,name='customer-dashboard'),
    path('customerlogin', LoginView.as_view(template_name='insurance/adminlogin.html'),name='customerlogin'),
    path("upload-claim/", upload_claim, name="upload_claim"),







    path('apply-policy', views.apply_policy_view,name='apply-policy'),
    path('apply/<int:pk>', views.apply_view,name='apply'),
    path('history', views.history_view,name='history'),
    path('policy-categories/', views.customer_view_categories, name='policy-categories'),
    path('ask-question', views.ask_question_view,name='ask-question'),
    path('question-history', views.question_history_view,name='question-history'),
    path('contactus', insurance_views.contactus_view, name='contact'),
    path("contactsuc/", insurance_views.contactus_success_view, name="contactussuccess"),
    path('success-page/', views.success_view, name='success-page'), 
   


   
   
   

    path('admin-approve-claim/<int:claim_id>/', insurance_views.admin_approve_claim, name='admin-approve-claim'),
    path('admin-reject-claim/<int:claim_id>/', insurance_views.admin_reject_claim, name='admin-reject-claim'),

    path('claims/', insurance_views.claim_list, name='claim_list'),
    path('claims/add/', insurance_views.add_claim, name='add_claim'),
    path('claims/update/<int:claim_id>/', insurance_views.update_claim, name='update_claim'),
    path('claims/delete/<int:claim_id>/', insurance_views.delete_claim, name='delete_claim'),


]