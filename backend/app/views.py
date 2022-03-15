import os
import shutil
from turtle import title
import zipfile
from lxml import html
import json
import shutil

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import AccessToken

from .serializers import RegisterSerializer
from .serializers import DocumentSerializer
from .serializers import AnalyseSerializer
from .serializers import UserSerializer

from .models import Document
from .models import Analyse

from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    # údaje pošleme do serializéra na validáciu
    # ak prebehne bez problémov, vytvorí sa nový objekt User
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer 

@api_view(['GET'])
def getUser(request):
    # zoberieme zaslaný prístupový token a na základe neho získame id používateľa
    access_token_obj = AccessToken(request.query_params.get('access_token'))
    user_id=access_token_obj['user_id']
    # podľa id vyberieme User objekt
    user=User.objects.get(id=user_id)
    # prekonvertujeme na JSON
    serializer = UserSerializer(user, many= False)
    # vrátime odpoveď
    return Response(serializer.data)       

@api_view(['POST'])
def uploadFile(request):
    # ak je metóda POST
    if request.method == "POST":
        # zoberieme zoznam súborov
        files = request.FILES.getlist('files')
        # zoberieme id používateľa
        # ak je id -1 nastavíme user na None
        # ak nie, získame User objekt podľa id
        uid = request.POST.get('user_id')
        if uid != "-1":
            user = User.objects.get(id=uid)
        else:
            user = None  
        # vytvoríme obejkt Analyse s id používateľa
        analyse = Analyse.objects.create(user_id= user)
        created_files = []
        # prebehneme po súboroch a pre každý vytvoríme obejkt Document
        for currentFile in files:
            created = Document.objects.create(title=currentFile.name, file=currentFile, user_id = user, analyse_id = analyse)
            created_files.append(created)
        # súbory konvertujeme na JSON
        serializer = DocumentSerializer(created_files, many=True)
        # vrátime odpoveď
        return Response(serializer.data)

@api_view(['GET'])
def getUserHistory(request):
    # zoberieme si z parametrov id používateľa
    uid= request.query_params.get('uid')
    # získame Analyse objekty podľa id používateľa, od najnovšieho po najstaršie (dátum)
    analyses = Analyse.objects.filter(user_id=uid).order_by('-date')
    data=[]
    # prebehneme po objektoch Analyse
    for analyse in analyses:
        # zísakme objekty Document prislúchajúce k Analyse obejktu
        files = Document.objects.filter(analyse_id= analyse)
        # vložíme potrebné dáta
        item = {"analyse_id": analyse.id, "date": analyse.date, "files_count": len(files), "files": []}
        # prebehneme po súboroch a pridáme ich do pola files
        for file in files:
            serializer = DocumentSerializer(file, many=False)
            item["files"].append(serializer.data)

        data.append(item)

    # prekonvertujeme na JSON
    jsonData=json.dumps(data,default=str)
    # vrátime odpoveď
    return Response(jsonData)

@api_view(['GET'])
def getAnalysedData(request):
    # zoberieme zoznam id súborov
    iDs = request.query_params.getlist('id')
    # získame Document objekty podľa id zoznamu
    files = Document.objects.filter(id__in=iDs)
    # ako odpoveď vrátime výstup funkcie analyze
    return Response(analyze(files))

def analyze(files):
    # inicializácia premenných
    data= {"basicStats":{},
           "builtInBlocks": {},
           "componentBlocks": {},
           "componentBlocksCategories": {},
           "userInterfaceComponentBlocks": {},
           "drawingAndAnimationComponentBlocks":{},
           "storageAndExperimentalComponentBlocks":{},
           "controlBlocksTypes": {},
           "procedureBlocksTypes":{}, 
           "blocksPerProject":{},
           "componentsPerProject":{}, 
           "screensPerProject":{}}
    number_of_blocks = 0
    number_of_components = 0
    number_of_projects = len(files)
    number_of_screens = 0
    number_of_blocks_per_project = 0
    number_of_components_per_project = 0
    number_of_screens_per_project = 0
    control_blocks = 0
    logic_blocks = 0
    math_blocks = 0
    text_blocks = 0
    lists_blocks = 0
    dictionaries_blocks = 0
    colors_blocks = 0
    variables_blocks = 0
    procedures_blocks = 0
    helpers_names_blocks = 0
    event_blocks = 0
    setGet_blocks = 0
    method_blocks = 0
    componentObject_blocks = 0
    helpers_assets_blocks = 0
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
    conditional = 0
    loop = 0
    screen = 0
    procNoReturn = 0
    procWithReturn = 0
    canvas = 0
    imageSprite = 0
    ball = 0
    cloudDb = 0
    storageFile = 0
    tinyDb = 0
    tinyWebDb = 0
    firebaseDb = 0
    # prebehneme po súboroch
    for file in files:
        # zadefinujeme si cesty
        path = "./media/unzipped_files/"+str(file.id)
        os.mkdir(path)
        my_dir = "./media/unzipped_files/"+str(file.id)
        my_zip = "./media/"+str(file.file)
        # rozbalíme súbor
        with zipfile.ZipFile(my_zip) as zip_file:
            for member in zip_file.namelist():
                filename = os.path.basename(member)
                # preskočiť adresáre
                if not filename:
                    continue
                # skopírujeme súbor (zísakný z extrakcie zipfile)
                source = zip_file.open(member)
                target = open(os.path.join(my_dir, filename), "wb")
                with source, target:
                    shutil.copyfileobj(source, target)
        noMoreScreens = False
        number = 1
        # pokiaľ sú v porjekte nejaké obrazovky
        while noMoreScreens == False:
            # zoberieme XML súbor Screen.bky
            if os.path.isfile("./media/unzipped_files/"+str(file.id)+"/Screen"+str(number)+".bky"):
                f = open("./media/unzipped_files/"+str(file.id)+"/Screen"+str(number)+".bky", "r")
                # prečítame súbor
                if f.mode == "r":
                    content = f.read()
                    # vytvoríme si strom na základe ktorého môžeme vyberať uzly pomocou XPath 
                    tree = html.fromstring(content)
                    #basic stats
                    number_of_blocks += len(tree.xpath("//block"))
                    number_of_screens += 1
                    #built-in blocks
                    control_blocks += len(tree.xpath("//block[contains(@type,'control')]"))
                    logic_blocks += len(tree.xpath("//block[contains(@type,'logic')]"))
                    math_blocks += len(tree.xpath("//block[contains(@type,'math')]"))
                    text_blocks += len(tree.xpath("//block[contains(@type,'text')]"))
                    lists_blocks += len(tree.xpath("//block[contains(@type,'lists')]"))
                    dictionaries_blocks += len(tree.xpath("//block[contains(@type,'dictionaries')]"))
                    colors_blocks += len(tree.xpath("//block[contains(@type,'color')]"))
                    variables_blocks += len(tree.xpath("//block[contains(@type,'lexical_variable') or contains(@type,'local_declaration') or contains(@type,'global_declaration')]"))
                    procedures_blocks += len(tree.xpath("//block[contains(@type,'procedures')]"))
                    helpers_names_blocks += len(tree.xpath("//block[contains(@type,'helpers_screen_names')]"))
                    #component blocks
                    event_blocks += len(tree.xpath("//block[contains(@type,'component_event')]"))
                    setGet_blocks += len(tree.xpath("//block[contains(@type,'component_set_get')]"))
                    method_blocks += len(tree.xpath("//block[contains(@type,'component_method')]"))
                    componentObject_blocks += len(tree.xpath("//block[contains(@type,'component_component_block')]"))
                    helpers_assets_blocks += len(tree.xpath("//block[contains(@type,'helpers_assets')]"))
                    helpers_assets_blocks += len(tree.xpath("//block[contains(@type,'helpers_dropdown')]"))
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
                    #user inferface component blocks
                    buttons += len(tree.xpath("//mutation[@component_type='Button']"))
                    checkboxes += len(tree.xpath("//mutation[@component_type='CheckBox']"))
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
                    #drawing and animation component blocks
                    canvas += len(tree.xpath("//mutation[@component_type='Canvas']"))
                    imageSprite += len(tree.xpath("//mutation[@component_type='ImageSprite']"))
                    ball += len(tree.xpath("//mutation[@component_type='Ball']"))
                    #storage and experimental component blocks
                    cloudDb += len(tree.xpath("//mutation[@component_type='CloudDB']"))
                    storageFile += len(tree.xpath("//mutation[@component_type='File']"))
                    tinyDb += len(tree.xpath("//mutation[@component_type='TinyDB']"))
                    tinyWebDb += len(tree.xpath("//mutation[@component_type='TinyWebDB']"))
                    firebaseDb += len(tree.xpath("//mutation[@component_type='FirebaseDB']"))
                    #control blocks types
                    conditional += len(tree.xpath("//block[@type='controls_if']"))
                    conditional += len(tree.xpath("//block[@type='controls_choose']"))
                    loop += len(tree.xpath("//block[@type='controls_forRange']"))
                    loop += len(tree.xpath("//block[@type='controls_forEach']"))
                    loop += len(tree.xpath("//block[@type='controls_for_each_dict']"))
                    loop += len(tree.xpath("//block[@type='controls_while']"))
                    screen += len(tree.xpath("//block[@type='controls_openAnotherScreen']"))
                    screen += len(tree.xpath("//block[@type='controls_openAnotherScreenWithStartValue']"))
                    screen += len(tree.xpath("//block[@type='controls_getStartValue']"))
                    screen += len(tree.xpath("//block[@type='controls_closeScreen']"))
                    screen += len(tree.xpath("//block[@type='controls_closeScreenWithValue']"))
                    screen += len(tree.xpath("//block[@type='controls_getPlainStartText']"))
                    screen += len(tree.xpath("//block[@type='controls_closeScreenWithPlainText']"))
                    #procedure blocks types
                    procNoReturn += len(tree.xpath("//block[@type='procedures_defnoreturn']"))
                    procWithReturn += len(tree.xpath("//block[@type='procedures_defreturn']"))
                    #per project
                    number_of_blocks_per_project += len(tree.xpath("//block"))
                    number_of_screens_per_project += 1
                    number += 1
                f.close()
            else:
                # pre každý súbor zísakme potrebné údaje
                data["blocksPerProject"][file.title] = number_of_blocks_per_project
                data["screensPerProject"][file.title] = number_of_screens_per_project
                number_of_blocks_per_project = 0
                number_of_screens_per_project = 0
                noMoreScreens = True


        noMoreScreens = False
        number = 1
        # pokiaľ sú v porjekte nejaké obrazovky
        while noMoreScreens == False:
            # zoberieme JSON súbor Screen.scm
            if os.path.isfile("./media/unzipped_files/"+str(file.id)+"/Screen"+str(number)+".scm"):
                f = open("./media/unzipped_files/"+str(file.id)+"/Screen"+str(number)+".scm", "r")
                # prečítame śubor
                if f.mode == "r":
                    content = f.read()
                    #basic stats
                    number_of_components += content.count("Uuid")-1
                    #per project
                    number_of_components_per_project += content.count("Uuid")-1    
                f.close()
                number += 1 
            else:
                # pre každý súbor zísakme potrebné údaje
                data["componentsPerProject"][file.title] = number_of_components_per_project
                number_of_components_per_project = 0
                noMoreScreens = True

    # odstránieme rozbalené súbory
    for file in files:
        my_dir = "./media/unzipped_files/"+str(file.id)
        shutil.rmtree(my_dir, ignore_errors=True)

    # vložíme výsledné hodnoty do data, ktoré vrátime ako odpoveď
    data['basicStats']['Number of projects'] = number_of_projects
    data['basicStats']['Number of screens'] = number_of_screens
    data['basicStats']['Number of blocks'] = number_of_blocks
    data['basicStats']['Number of components'] = number_of_components
    data['basicStats']['Number of built-in blocks'] = control_blocks + logic_blocks + math_blocks + text_blocks + lists_blocks + dictionaries_blocks + colors_blocks + variables_blocks + procedures_blocks + helpers_names_blocks
    data['basicStats']['Number of component blocks'] = event_blocks + setGet_blocks + method_blocks + componentObject_blocks + helpers_assets_blocks
    data['builtInBlocks']['Control blocks'] = control_blocks
    data['builtInBlocks']['Logic blocks'] = logic_blocks
    data['builtInBlocks']['Math blocks'] = math_blocks
    data['builtInBlocks']['Text blocks'] = text_blocks
    data['builtInBlocks']['Lists blocks'] = lists_blocks
    data['builtInBlocks']['Dictionaries blocks'] = dictionaries_blocks
    data['builtInBlocks']['Colors blocks'] = colors_blocks
    data['builtInBlocks']['Variables blocks'] = variables_blocks
    data['builtInBlocks']['Procedures blocks'] = procedures_blocks
    data['builtInBlocks']['Helpers blocks'] = helpers_names_blocks
    data['componentBlocks']['Event blocks'] = event_blocks
    data['componentBlocks']['Set and get blocks'] = setGet_blocks
    data['componentBlocks']['Method blocks'] = method_blocks
    data['componentBlocks']['Component object blocks'] = componentObject_blocks
    data['componentBlocks']['Helpers blocks'] = helpers_assets_blocks
    data['componentBlocksCategories']['User interface'] = userInterface
    data['componentBlocksCategories']['Layout'] = layout
    data['componentBlocksCategories']['Media'] = media
    data['componentBlocksCategories']['Drawing and animation'] = drawingAndAnimation
    data['componentBlocksCategories']['Maps'] = maps
    data['componentBlocksCategories']['Sensors'] = sensors
    data['componentBlocksCategories']['Social'] = social
    data['componentBlocksCategories']['Storage'] = storage
    data['componentBlocksCategories']['Connectivity'] =  connectivity
    data['componentBlocksCategories']['Lego Mindstorms'] =  legoMindstorms
    data['componentBlocksCategories']['Experimental'] =  experimental
    data['userInterfaceComponentBlocks']['Buttons'] =  buttons
    data['userInterfaceComponentBlocks']['Checkboxes'] =  checkboxes
    data['userInterfaceComponentBlocks']['Date pickers'] =  datePickers
    data['userInterfaceComponentBlocks']['Images'] =  images
    data['userInterfaceComponentBlocks']['Labels'] =  labels
    data['userInterfaceComponentBlocks']['List pickers'] =  listPickers
    data['userInterfaceComponentBlocks']['List views'] =  listViews
    data['userInterfaceComponentBlocks']['Notifiers'] =  notifiers
    data['userInterfaceComponentBlocks']['Password text boxes'] =  passwordTextBoxes
    data['userInterfaceComponentBlocks']['Sliders'] =  sliders
    data['userInterfaceComponentBlocks']['Spinners'] =  spinners
    data['userInterfaceComponentBlocks']['Switches'] =  switches
    data['userInterfaceComponentBlocks']['Text boxes'] =  textBoxes
    data['userInterfaceComponentBlocks']['Time pickers'] =  timePickers
    data['userInterfaceComponentBlocks']['Web viewers'] =  webViewers
    data['drawingAndAnimationComponentBlocks']['Canvas'] =  canvas
    data['drawingAndAnimationComponentBlocks']['Image Sprite'] =  imageSprite
    data['drawingAndAnimationComponentBlocks']['Ball'] =  ball
    data['storageAndExperimentalComponentBlocks']['CloudDB'] =  cloudDb
    data['storageAndExperimentalComponentBlocks']['File'] =  storageFile
    data['storageAndExperimentalComponentBlocks']['TinyDB'] =  tinyDb
    data['storageAndExperimentalComponentBlocks']['TinyWebDB'] =  tinyWebDb
    data['storageAndExperimentalComponentBlocks']['FirebaseDB'] =  firebaseDb
    data['controlBlocksTypes']['Conditional'] =  conditional
    data['controlBlocksTypes']['Loop'] =  loop
    data['controlBlocksTypes']['Screen'] =  screen
    data['procedureBlocksTypes']['Without return'] =  procNoReturn
    data['procedureBlocksTypes']['With return'] =  procWithReturn

    return [data]


