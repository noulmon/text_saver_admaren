from django.db.migrations import serializer
from rest_framework import status
from rest_framework.response import Response


def serializer_error_response(errors):
    return Response(
        {
            'success': False,
            'message': 'Validation Error',
            'error': serializer.errors
        },
        status=status.HTTP_400_BAD_REQUEST
    )
