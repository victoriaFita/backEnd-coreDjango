from rest_framework import mixins, parsers, viewsets
from rest_framework.permissions import AllowAny

from uploader.models import Document, Image
from uploader.serializers import DocumentUploadSerializer, ImageUploadSerializer, ImageSerializer


class CreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    pass


class DocumentUploadViewSet(CreateViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]


class ImageUploadViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageUploadSerializer
    parser_classes = [parsers.FormParser, parsers.MultiPartParser]
    permission_classes = [AllowAny]
    http_method_names = ['post', 'put', 'get', 'head', 'options']

def get_serializer_class(self):
    if self.action == 'create':
        return ImageUploadSerializer
    return ImageSerializer


    