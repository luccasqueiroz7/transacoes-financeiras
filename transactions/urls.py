from django.urls import path
from . import views

urlpatterns = [
    path("form/", views.form, name="form"),
    path(
        "transactions/",
        views.TransactionView.as_view(),
    ),
]
