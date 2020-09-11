from rest_framework import viewsets, permissions
from api.script_manager.serialzers.script_serializer import ScriptSerializer
from api.script_manager.models import Script


class ScriptViewSet(viewsets.ModelViewSet):
    queryset = Script.objects.all().order_by('last_change')
    serializer_class = ScriptSerializer
    permission_classes = []
