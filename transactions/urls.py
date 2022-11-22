from django.urls import path
from . import views

# from transactions.views import form

urlpatterns = [
    path("form/", views.form, name="form"),
    path(
        "transactions/",
        views.TransactionView.as_view(),
    ),
]
