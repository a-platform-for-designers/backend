from rest_framework import viewsets

from api.serializers.language_serializers import LanguageSerializer
from job.models import Language


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()