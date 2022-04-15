from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from files.models import Files
from files.serializers import UploadFileSerializer
from rest_framework.decorators import api_view


class UploadFileViewSet(ViewSet):
    # def file_list(self, request):
    #     return Response("GET API")
    @api_view(['POST'])
    def create(self, request):
        serializer = UploadFileSerializer(data=request.data)
        file = request.FILES.get('file')
        content_type = file.content_type
        response = "{} file".format(content_type)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, response)

    # def post(self, request):
    #     serializer = UploadFileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)



    @api_view(['GET'])
    def files_list(self, request):
        files = Files.objects.all()
        serializer = UploadFileSerializer(files)
        return Response(serializer.data)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

# @api_view(('GET',))
# @permission_classes((AllowAny,))
# def load_nearest_intell(request):
#     "" "Загрузить данные
#     """
#
#     def file_iterator(file_name, chunk_size=512):
#                  # Итератор чтения файла
#         try:
#             with open(file_name, 'rb') as f:
#                 while True:
#                     data = f.read(chunk_size)
#                     if data:
#                         yield data
#                     else:
#                         break
#         except IOError as e:
#             print(e)
#
#     filename = request.GET.get('filename', None)
#          path = '' # собственный путь к файлу
#     filename = os.path.join(path, filename)
#     response = StreamingHttpResponse(file_iterator(filename))
#     response['Content-Type'] = 'application/octet-stream'
#     response['Content-Disposition'] = 'attachment;filename="{0}"'.format(nearest_filename)
#          # Обратите внимание, что если вы хотите вернуть больше параметров, вы можете добавить их в ответ, записать их в виде словаря и получить параметры в заголовках
#
#

# import requests
#
# url = 'Путь запроса API, упакованного вами'
# resp = requests.get(url)
#
# print(resp.status_code)
# headers = resp.headers  # Все переданные параметры инкапсуляции можно получить в заголовках
# filename = headers['Content-Disposition'].split('=')[-1].strip('"')
# print(filename)
# with open(filename, 'wb') as f:
#     resp.iter_content(512):
#     f.write(line) Принято здесь также должно быть получено в виде итератора, 512 зависит от размера каждой итерации чтения
