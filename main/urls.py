from django.urls import path
from .views import OperationView, WalletView

# <uuid:item_uuid>
urlpatterns = [
    path("<uuid:wallet_uuid>/operation", OperationView.as_view()),
    path("<uuid:wallet_uuid>", WalletView.as_view()),
]