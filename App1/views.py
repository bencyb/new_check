from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Authentication

@api_view(['POST'])
@authentication_classes([TokenAuthentication]) 
@permission_classes([IsAuthenticated])  
def webhook_callback(request):
    submission_data = {
        "submission_id": 123,
        "test_result": "passed",
        "timestamp": "2023-08-04T12:34:56"
    }
    response_data = {
        "message": "Webhook received successfully.",
        "submission_data": submission_data
    }
    return Response(response_data, status=status.HTTP_200_OK)
















