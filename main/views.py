from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serialiazers import OperationSerializer, WalletSerializer
from .models import Wallet
from django.db.models import F



class OperationView(generics.GenericAPIView):
    serializer_class = OperationSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, wallet_uuid):
        serializer: OperationSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data["amount"]
        match serializer.validated_data["operation_type"]:
            case "DEPOSIT":
                Wallet.objects.filter(pk=wallet_uuid).update(balance=F('balance') + amount)
            case "WITHDRAW":
                Wallet.objects.filter(pk=wallet_uuid).update(balance=F('balance') - amount)
            case _:
                return Response({'error': 'Invalid operations'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            wallet: Wallet = Wallet.objects.get(pk=wallet_uuid)
        except Exception as e:
            return Response({'error': 'Wallet not found'}, status=status.HTTP_400_BAD_REQUEST)
        wallet_json = WalletSerializer(wallet).data
        return Response(data=wallet_json, status=status.HTTP_200_OK)


class WalletView(generics.GenericAPIView):
    def get(self, request, wallet_uuid):
        try:
            wallet: Wallet = Wallet.objects.get(pk=wallet_uuid)
            return Response(data={"balance": wallet.balance}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Wallet not found'}, status=status.HTTP_400_BAD_REQUEST)




