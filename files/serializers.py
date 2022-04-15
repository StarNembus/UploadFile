from rest_framework.serializers import Serializer, FileField


class UploadFileSerializer(Serializer):
    file = FileField()

    class Meta:
        fields = '__all__'




