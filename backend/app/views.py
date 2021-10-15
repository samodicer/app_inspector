import os
import shutil
import zipfile
from lxml import html
import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Document
from .serializers import DocumentSerializer

@api_view(['POST'])
def uploadFile(request):
    #file = request.data['file']
    #title = request.data['title']
    files = request.FILES.getlist('files')
    created_files = []
    for currentFile in files:
        created = Document.objects.create(title=currentFile.name, file=currentFile)
        created_files.append(created)

    #created = Document.objects.create(title=title, file=file)
    serializer = DocumentSerializer(created_files, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFiles(request):
    files = Document.objects.all()
    serializer = DocumentSerializer(files, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFileById(request, pk):
    files = Document.objects.get(id=pk)
    serializer = DocumentSerializer(files, many=False)
    analyze(files.id, files.file)
    return Response(serializer.data)

@api_view(['GET'])
def getFileData(request, pk):
    files = Document.objects.get(id=pk)
    return Response(analyze(files.id, files.file))

@api_view(['GET'])
def getFilesData(request):
    iDs = request.query_params.getlist('id')
    files = Document.objects.filter(id__in=iDs)
    #serializer = DocumentSerializer(objects, many=True)
    return Response(analyze(files))

def analyze(files):
    data = {}
    number_of_blocks = 0
    for file in files:
        path = "./media/unzipped_files/"+str(file.id)
        print('path:', path)
        os.mkdir(path)
        my_dir = "./media/unzipped_files/"+str(file.id)
        my_zip = "./media/"+str(file.file)

        with zipfile.ZipFile(my_zip) as zip_file:
            for member in zip_file.namelist():
                filename = os.path.basename(member)
                # skip directories
                if not filename:
                    continue

                # copy file (taken from zipfile's extract)
                source = zip_file.open(member)
                target = open(os.path.join(my_dir, filename), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)

        f = open("./media/unzipped_files/"+str(file.id)+"/Screen1.bky", "r")
        if f.mode == "r":
            content = f.read()
            print(content)

        '''tree = html.fromstring(content)
        number_of_blocks = len(tree.xpath("//block[@type ='component_event']"))
        print("Number of blocks:", number_of_blocks)
        components = list(dict.fromkeys(tree.xpath("//field[@name ='COMPONENT_SELECTOR']/text()")))
        print("Used components:", components)
        events = tree.xpath("//mutation/@event_name")
        print("Used events:", events)
        methods = tree.xpath("//mutation/@method_name")
        print("Used methods:", methods)
        parameters=tree.xpath("//eventparam/@name")
        print("Used parameters:", parameters)
        sets = len(tree.xpath("//mutation[@set_or_get = 'set']"))
        print("Number of setters:", sets)
        gets = len(tree.xpath("//mutation[@set_or_get = 'get']"))
        print("Number of getters:", gets)

        data = {}
        data['id'] = file.id
        data['number_of_blocks'] = number_of_blocks
        data['components'] = components
        data['methods'] = methods
        data['sets'] = sets
        data['gets'] = gets
        data['parameters'] = parameters
        #json_data = json.dumps(data)'''
        tree = html.fromstring(content)
        number_of_blocks = number_of_blocks + len(tree.xpath("//block[@type ='component_event']"))

    data['number_of_blocks'] = number_of_blocks

    return [data]

