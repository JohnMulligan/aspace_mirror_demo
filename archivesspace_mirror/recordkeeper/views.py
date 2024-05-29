from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from recordkeeper.models import Record
from recordkeeper.serializers import RecordSerializer


@api_view(['GET',])
def records_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)