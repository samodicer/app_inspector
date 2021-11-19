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
    data= {"builtInBlocks": {}, "componentBlocks": {}, "componentBlocksCategories": {}, "userInterfaceComponentBlocks": {}}
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
    userInterface = 0
    layout = 0
    media = 0
    drawingAndAnimation = 0
    maps = 0
    sensors = 0
    social = 0
    storage = 0
    connectivity = 0
    legoMindstorms = 0
    experimental = 0
    buttons = 0
    checkboxes = 0
    datePickers = 0
    images = 0
    labels = 0
    listPickers = 0
    listViews = 0
    notifiers = 0
    passwordTextBoxes = 0
    sliders = 0
    spinners = 0
    switches = 0
    textBoxes = 0
    timePickers = 0
    webViewers = 0

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

        #design components
        userInterface += len(tree.xpath("//mutation[@component_type='Button']"))
        userInterface += len(tree.xpath("//mutation[@component_type='CheckBox']"))
        userInterface += len(tree.xpath("//mutation[@component_type='DatePicker']"))
        userInterface += len(tree.xpath("//mutation[@component_type='Image']"))
        userInterface += len(tree.xpath("//mutation[@component_type='Label']"))
        userInterface += len(tree.xpath("//mutation[@component_type='ListPicker']"))
        userInterface += len(tree.xpath("//mutation[@component_type='ListView']"))
        userInterface += len(tree.xpath("//mutation[@component_type='Notifier']"))
        userInterface += len(tree.xpath("//mutation[@component_type='PasswordTextBox']"))
        userInterface += len(tree.xpath("//mutation[@component_type='Slider']"))
        userInterface += len(tree.xpath("//mutation[@component_type='Spinner']"))
        userInterface += len(tree.xpath("//mutation[@component_type='Switch']"))
        userInterface += len(tree.xpath("//mutation[@component_type='TextBox']"))
        userInterface += len(tree.xpath("//mutation[@component_type='TimePicker']"))
        userInterface += len(tree.xpath("//mutation[@component_type='WebViewer']"))
        layout += len(tree.xpath("//mutation[@component_type='HorizontalArrangement']"))
        layout += len(tree.xpath("//mutation[@component_type='HorizontalScrollArrangement']"))
        layout += len(tree.xpath("//mutation[@component_type='TableArrangement']"))
        layout += len(tree.xpath("//mutation[@component_type='VerticalArrangement']"))
        layout += len(tree.xpath("//mutation[@component_type='VerticalScrollArrangement']"))
        media += len(tree.xpath("//mutation[@component_type='Camcorder']"))
        media += len(tree.xpath("//mutation[@component_type='Camera']"))
        media += len(tree.xpath("//mutation[@component_type='ImagePicker']"))
        media += len(tree.xpath("//mutation[@component_type='Player']"))
        media += len(tree.xpath("//mutation[@component_type='Sound']"))
        media += len(tree.xpath("//mutation[@component_type='SoundRecorder']"))
        media += len(tree.xpath("//mutation[@component_type='SpeechRecognizer']"))
        media += len(tree.xpath("//mutation[@component_type='TextToSpeech']"))
        media += len(tree.xpath("//mutation[@component_type='VideoPlayer']"))
        media += len(tree.xpath("//mutation[@component_type='YandexTranslate']"))
        drawingAndAnimation += len(tree.xpath("//mutation[@component_type='Ball']"))
        drawingAndAnimation += len(tree.xpath("//mutation[@component_type='Canvas']"))
        drawingAndAnimation += len(tree.xpath("//mutation[@component_type='ImageSprite']"))
        maps += len(tree.xpath("//mutation[@component_type='Circle']"))
        maps += len(tree.xpath("//mutation[@component_type='FeatureCollection']"))
        maps += len(tree.xpath("//mutation[@component_type='LineString']"))
        maps += len(tree.xpath("//mutation[@component_type='Map']"))
        maps += len(tree.xpath("//mutation[@component_type='Marker']"))
        maps += len(tree.xpath("//mutation[@component_type='Navigation']"))
        maps += len(tree.xpath("//mutation[@component_type='Polygon']"))
        maps += len(tree.xpath("//mutation[@component_type='Rectangle']"))
        sensors += len(tree.xpath("//mutation[@component_type='AccelerometerSensor']"))
        sensors += len(tree.xpath("//mutation[@component_type='BarcodeScanner']"))
        sensors += len(tree.xpath("//mutation[@component_type='Barometer']"))
        sensors += len(tree.xpath("//mutation[@component_type='Clock']"))
        sensors += len(tree.xpath("//mutation[@component_type='GyroscopeSensor']"))
        sensors += len(tree.xpath("//mutation[@component_type='Hygrometer']"))
        sensors += len(tree.xpath("//mutation[@component_type='LightSensor']"))
        sensors += len(tree.xpath("//mutation[@component_type='LocationSensor']"))
        sensors += len(tree.xpath("//mutation[@component_type='MagneticFieldSensor']"))
        sensors += len(tree.xpath("//mutation[@component_type='NearField']"))
        sensors += len(tree.xpath("//mutation[@component_type='OrientationSensor']"))
        sensors += len(tree.xpath("//mutation[@component_type='Pedometer']"))
        sensors += len(tree.xpath("//mutation[@component_type='ProximitySensor']"))
        sensors += len(tree.xpath("//mutation[@component_type='Thermometer']"))
        social += len(tree.xpath("//mutation[@component_type='ContactPicker']"))
        social += len(tree.xpath("//mutation[@component_type='EmailPicker']"))
        social += len(tree.xpath("//mutation[@component_type='PhoneCall']"))
        social += len(tree.xpath("//mutation[@component_type='PhoneNumberPicker']"))
        social += len(tree.xpath("//mutation[@component_type='Sharing']"))
        social += len(tree.xpath("//mutation[@component_type='Texting']"))
        social += len(tree.xpath("//mutation[@component_type='Twitter']"))
        storage += len(tree.xpath("//mutation[@component_type='CloudDB']"))
        storage += len(tree.xpath("//mutation[@component_type='File']"))
        storage += len(tree.xpath("//mutation[@component_type='TinyDB']"))
        storage += len(tree.xpath("//mutation[@component_type='TinyWebDB']"))
        connectivity += len(tree.xpath("//mutation[@component_type='ActivityStarter']"))
        connectivity += len(tree.xpath("//mutation[@component_type='BluetoothClient']"))
        connectivity += len(tree.xpath("//mutation[@component_type='BluetoothServer']"))
        connectivity += len(tree.xpath("//mutation[@component_type='Serial']"))
        connectivity += len(tree.xpath("//mutation[@component_type='Web']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='NxtDrive']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='NxtColorSensor']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='NxtLightSensor']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='NxtSoundSensor']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='NxtTouchSensor']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='NxtUltrasonicSensor']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='NxtDirectCommands']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='Ev3Motors']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='Ev3ColorSensor']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='Ev3GyroSensor']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='Ev3TouchSensor']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='Ev3UltrasonicSensor']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='Ev3Sound']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='Ev3UI']"))
        legoMindstorms += len(tree.xpath("//mutation[@component_type='Ev3Commands']"))
        experimental += len(tree.xpath("//mutation[@component_type='FirebaseDB']"))

        #user inferface components block
        buttons += len(tree.xpath("//mutation[@component_type='Button']"))
        print('buttons:', buttons)
        checkboxes += len(tree.xpath("//mutation[@component_type='CheckBox']"))
        print('checkboxes:', checkboxes)
        datePickers += len(tree.xpath("//mutation[@component_type='DatePicker']"))
        images += len(tree.xpath("//mutation[@component_type='Image']"))
        labels += len(tree.xpath("//mutation[@component_type='Label']"))
        listPickers += len(tree.xpath("//mutation[@component_type='ListPicker']"))
        listViews += len(tree.xpath("//mutation[@component_type='ListView']"))
        notifiers += len(tree.xpath("//mutation[@component_type='Notifier']"))
        passwordTextBoxes += len(tree.xpath("//mutation[@component_type='PasswordTextBox']"))
        sliders += len(tree.xpath("//mutation[@component_type='Slider']"))
        spinners += len(tree.xpath("//mutation[@component_type='Spinner']"))
        switches += len(tree.xpath("//mutation[@component_type='Switch']"))
        textBoxes += len(tree.xpath("//mutation[@component_type='TextBox']"))
        timePickers += len(tree.xpath("//mutation[@component_type='TimePicker']"))
        webViewers += len(tree.xpath("//mutation[@component_type='WebViewer']"))

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
    data['componentBlocksCategories']['user_interface'] = userInterface
    data['componentBlocksCategories']['layout'] = layout
    data['componentBlocksCategories']['media'] = media
    data['componentBlocksCategories']['drawing_and_animation'] = drawingAndAnimation
    data['componentBlocksCategories']['maps'] = maps
    data['componentBlocksCategories']['sensors'] = sensors
    data['componentBlocksCategories']['social'] = social
    data['componentBlocksCategories']['storage'] = storage
    data['componentBlocksCategories']['connectivity'] =  connectivity
    data['componentBlocksCategories']['lego_mindstorms'] =  legoMindstorms
    data['componentBlocksCategories']['experimental'] =  experimental
    data['userInterfaceComponentBlocks']['buttons'] =  buttons
    data['userInterfaceComponentBlocks']['checkboxes'] =  checkboxes
    data['userInterfaceComponentBlocks']['date_pickers'] =  datePickers
    data['userInterfaceComponentBlocks']['images'] =  images
    data['userInterfaceComponentBlocks']['labels'] =  labels
    data['userInterfaceComponentBlocks']['list_pickers'] =  listPickers
    data['userInterfaceComponentBlocks']['listViews'] =  listViews
    data['userInterfaceComponentBlocks']['notifiers'] =  notifiers
    data['userInterfaceComponentBlocks']['password_text_boxes'] =  passwordTextBoxes
    data['userInterfaceComponentBlocks']['sliders'] =  sliders
    data['userInterfaceComponentBlocks']['spinners'] =  spinners
    data['userInterfaceComponentBlocks']['switches'] =  switches
    data['userInterfaceComponentBlocks']['text_boxes'] =  textBoxes
    data['userInterfaceComponentBlocks']['time_pickers'] =  timePickers
    data['userInterfaceComponentBlocks']['web_viewers'] =  webViewers


    return [data]

