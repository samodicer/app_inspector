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
    data= {"builtInBlocks": {}, "componentBlocks": {}}
    number_of_blocks = 0
    control_blocks = 0
    logic_blocks = 0
    math_blocks = 0
    text_blocks = 0
    lists_blocks = 0
    colors_blocks = 0
    variables_blocks = 0
    procedures_blocks = 0
    event_blocks = 0
    setGet_blocks = 0
    method_blocks = 0
    componentObject_blocks = 0
    helpersAssets_blocks = 0

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

        #number_of_blocks = number_of_blocks + len(tree.xpath("//block[@type ='component_event']"))

        # built-in blocks
        control_blocks += len(tree.xpath("//block[contains(@type,'control')]"))
        logic_blocks += len(tree.xpath("//block[contains(@type,'logic')]"))
        math_blocks += len(tree.xpath("//block[contains(@type,'math')]"))
        text_blocks += len(tree.xpath("//block[contains(@type,'text')]"))
        lists_blocks += len(tree.xpath("//block[contains(@type,'lists')]"))
        colors_blocks += len(tree.xpath("//block[contains(@type,'color')]"))
        variables_blocks += len(tree.xpath("//block[contains(@type,'lexical_variable') or contains(@type,'local_declaration')]"))
        procedures_blocks += len(tree.xpath("//block[contains(@type,'procedures')]"))

        #component blocks
        event_blocks += len(tree.xpath("//block[contains(@type,'component_event')]"))
        setGet_blocks += len(tree.xpath("//block[contains(@type,'component_set_get')]"))
        method_blocks += len(tree.xpath("//block[contains(@type,'component_method')]"))
        componentObject_blocks += len(tree.xpath("//block[contains(@type,'component_component_block')]"))
        helpersAssets_blocks += len(tree.xpath("//block[contains(@type,'helpers_assets')]"))

    #data['builtInBlocks']['number_of_blocks'] = number_of_blocks
    data['builtInBlocks']['control_blocks'] = control_blocks
    data['builtInBlocks']['logic_blocks'] = logic_blocks
    data['builtInBlocks']['math_blocks'] = math_blocks
    data['builtInBlocks']['text_blocks'] = text_blocks
    data['builtInBlocks']['lists_blocks'] = lists_blocks
    data['builtInBlocks']['colors_blocks'] = colors_blocks
    data['builtInBlocks']['variables_blocks'] = variables_blocks
    data['builtInBlocks']['procedures_blocks'] = procedures_blocks
    data['componentBlocks']['event_blocks'] = event_blocks
    data['componentBlocks']['setGet_blocks'] = setGet_blocks
    data['componentBlocks']['method_blocks'] = method_blocks
    data['componentBlocks']['componentObject_blocks'] = componentObject_blocks
    data['componentBlocks']['helpersAssets_blocks'] = helpersAssets_blocks


    return [data]

