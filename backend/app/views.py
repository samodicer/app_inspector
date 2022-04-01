import os
import shutil
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
        # vytvoríme objekt Analyse s id používateľa
        analyse = Analyse.objects.create(user_id= user)
        created_files = []
        # prebehneme po súboroch a pre každý vytvoríme objekt Document
        for currentFile in files:
            created = Document.objects.create(title=currentFile.name, file=currentFile, user_id = user,  analyse_id = analyse)
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
    # ako odpoveď vrátime výstup funkcie analyse
    return Response(analyse(files))

def analyse(files):
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
           "screensPerProject":{},
           "buttonsPerProject":{},
           "checkboxesPerProject":{},
           "datepickersPerProject":{},
           "imagesPerProject":{},
           "labelsPerProject":{},
           "listpickersPerProject":{},
           "listviewsPerProject":{},
           "notifiersPerProject":{},
           "passwordtextboxesPerProject":{},
           "slidersPerProject":{},
           "spinnersPerProject":{},
           "switchesPerProject":{},
           "textboxesPerProject":{},
           "timepickersPerProject":{},
           "webviewersPerProject":{},
           "horizontalArrangmentPerProject":{},
           "horizontalScrollArrangmentPerProject":{},
           "tableArrangmentPerProject":{},
           "verticalArrangmentPerProject":{},
           "verticalScrollArrangmentPerProject":{},
           "camcordersPerProject":{},
           "camerasPerProject":{},
           "imagepickersPerProject":{},
           "playersPerProject":{},
           "soundsPerProject":{},
           "soundrecordersPerProject":{},
           "speechrecognizersPerProject":{},
           "texttospeechsPerProject":{},
           "videoplayersPerProject":{},
           "yandextranslatorsPerProject":{},
           "ballsPerProject":{},
           "canvasesPerProject":{},
           "imagespritesPerProject":{},
           "circlesPerProject":{},
           "featurecollectionsPerProject":{},
           "linestringsPerProject":{},
           "mapsPerProject":{},
           "markersPerProject":{},
           "navigationsPerProject":{},
           "polygonsPerProject":{},
           "rectanglesPerProject":{},
           "accelerometerSensorsPerProject":{},
           "barcodeScannersPerProject":{},
           "barometersPerProject":{},
           "clocksPerProject":{},
           "gyroscopeSensorsPerProject":{},
           "hygrometersPerProject":{},
           "lightSensorsPerProject":{},
           "locationSensorsPerProject":{},
           "magneticFieldSensorsPerProject":{},
           "nearFieldsPerProject":{},
           "orientationSensorsPerProject":{},
           "pedometersPerProject":{},
           "proximitySensorsPerProject":{},
           "thermometersPerProject":{},
           "contactPickersPerProject":{},
           "emailPickersPerProject":{},
           "phoneCallsPerProject":{},
           "phoneNumberPickersPerProject":{},
           "sharingsPerProject":{},
           "textingsPerProject":{},
           "twittersPerProject":{},
           "cloudDbsPerProject":{},
           "filesPerProject":{},
           "tinyDbsPerProject":{},
           "tinyWebDbsPerProject":{},
           "activityStartersPerProject":{},
           "bluetoothClientsPerProject":{},
           "bluetoothServersPerProject":{},
           "serialsPerProject":{},
           "websPerProject":{},
           "nxtDrivesPerProject":{},
           "nxtColorSensorsPerProject":{},
           "nxtLightSensorsPerProject":{},
           "nxtSoundSensorsPerProject":{},
           "nxtTouchSensorsPerProject":{},
           "nxtUltrasonicSensorsPerProject":{},
           "nxtDirectCommandsPerProject":{},
           "ev3MotorsPerProject":{},
           "ev3ColorSensorsPerProject":{},
           "ev3GyroSensorsPerProject":{},
           "ev3TouchSensorsPerProject":{},
           "ev3UltrasonicSensorsPerProject":{},
           "ev3SoundsPerProject":{},
           "ev3UIsPerProject":{},
           "ev3CommandsPerProject":{},
           "firebaseDbsPerProject":{},
           }

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
    number_of_buttons = 0
    number_of_checkboxes = 0
    number_of_datepickers = 0
    number_of_images = 0
    number_of_labels = 0
    number_of_listpickers = 0
    number_of_listviews = 0
    number_of_notifiers = 0
    number_of_passwordtextboxes = 0
    number_of_sliders = 0
    number_of_spinners = 0
    number_of_switches = 0
    number_of_textboxes = 0
    number_of_timepickers = 0
    number_of_webviewers = 0
    number_of_horizontalArr = 0
    number_of_horizontalScrollArr = 0
    number_of_tableArr = 0
    number_of_verticalArr = 0
    number_of_verticalScrollArr = 0
    number_of_camcorder = 0
    number_of_cameras = 0
    number_of_imagepickers = 0
    number_of_players = 0
    number_of_sounds = 0
    number_of_soundrecorders = 0
    number_of_speechrecognizers = 0
    number_of_texttospeechs = 0
    number_of_videoplayers = 0
    number_of_yandextranslators = 0
    number_of_balls = 0
    number_of_canvases = 0
    number_of_imagesprites = 0
    number_of_circles = 0
    number_of_featurecollections = 0
    number_of_linestrings = 0
    number_of_maps = 0
    number_of_markers = 0
    number_of_navigations = 0
    number_of_polygons = 0
    number_of_rectangles = 0
    number_of_accelerometerSensors = 0
    number_of_barcodeScanners = 0
    number_of_barometers = 0
    number_of_clocks = 0
    number_of_gyroscopeSensors = 0
    number_of_hygrometers = 0
    number_of_lightSensors = 0
    number_of_locationSensors = 0
    number_of_magneticFieldSensors = 0
    number_of_nearFields = 0
    number_of_orientationSensors = 0
    number_of_pedometers = 0
    number_of_proximitySensors = 0
    number_of_thermometers = 0
    number_of_contactPickers = 0
    number_of_emailPickers = 0
    number_of_phoneCalls = 0
    number_of_phoneNumberPickers = 0
    number_of_sharings = 0
    number_of_textings = 0
    number_of_twitters = 0
    number_of_cloudDbs = 0
    number_of_files = 0
    number_of_tinyDbs = 0
    number_of_tinyWebDbs = 0
    number_of_activityStarters = 0
    number_of_bluetoothClients = 0
    number_of_bluetoothServers = 0
    number_of_serials = 0
    number_of_webs = 0
    number_of_nxtDrives = 0
    number_of_nxtColorSensors = 0
    number_of_nxtLightSensors = 0
    number_of_nxtSoundSensors = 0
    number_of_nxtTouchSensors = 0
    number_of_nxtUltrasonicSensors = 0
    number_of_nxtDirectCommands = 0
    number_of_ev3Motors = 0
    number_of_ev3ColorSensors = 0
    number_of_ev3GyroSensors = 0
    number_of_ev3TouchSensors = 0
    number_of_ev3UltrasonicSensors = 0
    number_of_ev3Sounds = 0
    number_of_ev3UIs = 0
    number_of_ev3Commands = 0
    number_of_firebaseDbs = 0

    # prebehneme po súboroch
    for file in files:
        # zadefinujeme si cesty
        if not os.path.exists("./media/unzipped_files/"):
            os.mkdir("./media/unzipped_files/")
        path = "./media/unzipped_files/"+str(file.id)
        my_dir = "./media/unzipped_files/"+str(file.id)
        my_zip = "./media/"+str(file.file)
        # odstránime rozbalený súbor (ak náhodou existuje)
        shutil.rmtree(my_dir, ignore_errors=True)
        os.mkdir(path)
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
                f = open("./media/unzipped_files/"+str(file.id)+"/Screen"+str(number)+".bky", "r", encoding="utf-8")
                # prečítame súbor
                if f.mode == "r":
                    content = f.read()
                    # vytvoríme si strom na základe ktorého môžeme vyberať uzly pomocou XPath 
                    if content:   
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
                        number_of_buttons += len(tree.xpath("//mutation[@component_type='Button']"))
                        number_of_checkboxes += len(tree.xpath("//mutation[@component_type='CheckBox']"))
                        number_of_datepickers += len(tree.xpath("//mutation[@component_type='DatePicker']"))
                        number_of_images += len(tree.xpath("//mutation[@component_type='Image']"))
                        number_of_labels += len(tree.xpath("//mutation[@component_type='Label']"))
                        number_of_listpickers += len(tree.xpath("//mutation[@component_type='ListPicker']"))
                        number_of_listviews += len(tree.xpath("//mutation[@component_type='ListView']"))
                        number_of_notifiers += len(tree.xpath("//mutation[@component_type='Notifier']"))
                        number_of_passwordtextboxes += len(tree.xpath("//mutation[@component_type='PasswordTextBox']"))
                        number_of_sliders += len(tree.xpath("//mutation[@component_type='Slider']"))
                        number_of_spinners += len(tree.xpath("//mutation[@component_type='Spinner']"))
                        number_of_switches += len(tree.xpath("//mutation[@component_type='Switch']"))
                        number_of_textboxes += len(tree.xpath("//mutation[@component_type='TextBox']"))
                        number_of_timepickers += len(tree.xpath("//mutation[@component_type='TimePicker']"))
                        number_of_webviewers += len(tree.xpath("//mutation[@component_type='WebViewer']"))
                        number_of_horizontalArr += len(tree.xpath("//mutation[@component_type='HorizontalArrangement']"))
                        number_of_horizontalScrollArr += len(tree.xpath("//mutation[@component_type='HorizontalScrollArrangement']"))
                        number_of_tableArr += len(tree.xpath("//mutation[@component_type='TableArrangement']"))
                        number_of_verticalArr += len(tree.xpath("//mutation[@component_type='VerticalArrangement']"))
                        number_of_verticalScrollArr += len(tree.xpath("//mutation[@component_type='VerticalScrollArrangement']"))
                        number_of_camcorder += len(tree.xpath("//mutation[@component_type='Camcorder']"))
                        number_of_cameras += len(tree.xpath("//mutation[@component_type='Camera']"))
                        number_of_imagepickers += len(tree.xpath("//mutation[@component_type='ImagePicker']"))
                        number_of_players += len(tree.xpath("//mutation[@component_type='Player']"))
                        number_of_sounds += len(tree.xpath("//mutation[@component_type='Sound']"))
                        number_of_soundrecorders += len(tree.xpath("//mutation[@component_type='SoundRecorder']"))
                        number_of_speechrecognizers += len(tree.xpath("//mutation[@component_type='SpeechRecognizer']"))
                        number_of_texttospeechs += len(tree.xpath("//mutation[@component_type='TextToSpeech']"))
                        number_of_videoplayers += len(tree.xpath("//mutation[@component_type='VideoPlayer']"))
                        number_of_yandextranslators += len(tree.xpath("//mutation[@component_type='YandexTranslate']"))
                        number_of_balls += len(tree.xpath("//mutation[@component_type='Ball']"))
                        number_of_canvases += len(tree.xpath("//mutation[@component_type='Canvas']"))
                        number_of_imagesprites += len(tree.xpath("//mutation[@component_type='ImageSprite']"))
                        number_of_circles += len(tree.xpath("//mutation[@component_type='Circle']"))
                        number_of_featurecollections += len(tree.xpath("//mutation[@component_type='FeatureCollection']"))
                        number_of_linestrings += len(tree.xpath("//mutation[@component_type='LineString']"))
                        number_of_maps += len(tree.xpath("//mutation[@component_type='Map']"))
                        number_of_markers += len(tree.xpath("//mutation[@component_type='Marker']"))
                        number_of_navigations += len(tree.xpath("//mutation[@component_type='Navigation']"))
                        number_of_polygons += len(tree.xpath("//mutation[@component_type='Polygon']"))
                        number_of_rectangles += len(tree.xpath("//mutation[@component_type='Rectangle']"))
                        number_of_accelerometerSensors += len(tree.xpath("//mutation[@component_type='AccelerometerSensor']"))
                        number_of_barcodeScanners += len(tree.xpath("//mutation[@component_type='BarcodeScanner']"))
                        number_of_barometers += len(tree.xpath("//mutation[@component_type='Barometer']"))
                        number_of_clocks += len(tree.xpath("//mutation[@component_type='Clock']"))
                        number_of_gyroscopeSensors += len(tree.xpath("//mutation[@component_type='GyroscopeSensor']"))
                        number_of_hygrometers += len(tree.xpath("//mutation[@component_type='Hygrometer']"))
                        number_of_lightSensors += len(tree.xpath("//mutation[@component_type='LightSensor']"))
                        number_of_locationSensors += len(tree.xpath("//mutation[@component_type='LocationSensor']"))
                        number_of_magneticFieldSensors += len(tree.xpath("//mutation[@component_type='MagneticFieldSensor']"))
                        number_of_nearFields += len(tree.xpath("//mutation[@component_type='NearField']"))
                        number_of_orientationSensors += len(tree.xpath("//mutation[@component_type='OrientationSensor']"))
                        number_of_pedometers += len(tree.xpath("//mutation[@component_type='Pedometer']"))
                        number_of_proximitySensors += len(tree.xpath("//mutation[@component_type='ProximitySensor']"))
                        number_of_thermometers += len(tree.xpath("//mutation[@component_type='Thermometer']"))
                        number_of_contactPickers += len(tree.xpath("//mutation[@component_type='ContactPicker']"))
                        number_of_emailPickers += len(tree.xpath("//mutation[@component_type='EmailPicker']"))
                        number_of_phoneCalls += len(tree.xpath("//mutation[@component_type='PhoneCall']"))
                        number_of_phoneNumberPickers += len(tree.xpath("//mutation[@component_type='PhoneNumberPicker']"))
                        number_of_sharings += len(tree.xpath("//mutation[@component_type='Sharing']"))
                        number_of_textings += len(tree.xpath("//mutation[@component_type='Texting']"))
                        number_of_twitters += len(tree.xpath("//mutation[@component_type='Twitter']"))
                        number_of_cloudDbs += len(tree.xpath("//mutation[@component_type='CloudDB']"))
                        number_of_files += len(tree.xpath("//mutation[@component_type='File']"))
                        number_of_tinyDbs += len(tree.xpath("//mutation[@component_type='TinyDB']"))
                        number_of_tinyWebDbs += len(tree.xpath("//mutation[@component_type='TinyWebDB']"))
                        number_of_activityStarters += len(tree.xpath("//mutation[@component_type='ActivityStarter']"))
                        number_of_bluetoothClients += len(tree.xpath("//mutation[@component_type='BluetoothClient']"))
                        number_of_bluetoothServers += len(tree.xpath("//mutation[@component_type='BluetoothServer']"))
                        number_of_serials += len(tree.xpath("//mutation[@component_type='Serial']"))
                        number_of_webs += len(tree.xpath("//mutation[@component_type='Web']"))
                        number_of_nxtDrives += len(tree.xpath("//mutation[@component_type='NxtDrive']"))
                        number_of_nxtColorSensors += len(tree.xpath("//mutation[@component_type='NxtColorSensor']"))
                        number_of_nxtLightSensors += len(tree.xpath("//mutation[@component_type='NxtLightSensor']"))
                        number_of_nxtSoundSensors += len(tree.xpath("//mutation[@component_type='NxtSoundSensor']"))
                        number_of_nxtTouchSensors += len(tree.xpath("//mutation[@component_type='NxtTouchSensor']"))
                        number_of_nxtUltrasonicSensors += len(tree.xpath("//mutation[@component_type='NxtUltrasonicSensor']"))
                        number_of_nxtDirectCommands += len(tree.xpath("//mutation[@component_type='NxtDirectCommands']"))
                        number_of_ev3Motors += len(tree.xpath("//mutation[@component_type='Ev3Motors']"))
                        number_of_ev3ColorSensors += len(tree.xpath("//mutation[@component_type='Ev3ColorSensor']"))
                        number_of_ev3GyroSensors += len(tree.xpath("//mutation[@component_type='Ev3GyroSensor']"))
                        number_of_ev3TouchSensors += len(tree.xpath("//mutation[@component_type='Ev3TouchSensor']"))
                        number_of_ev3UltrasonicSensors += len(tree.xpath("//mutation[@component_type='Ev3UltrasonicSensor']"))
                        number_of_ev3Sounds += len(tree.xpath("//mutation[@component_type='Ev3Sound']"))
                        number_of_ev3UIs += len(tree.xpath("//mutation[@component_type='Ev3UI']"))
                        number_of_ev3Commands += len(tree.xpath("//mutation[@component_type='Ev3Commands']"))
                        number_of_firebaseDbs += len(tree.xpath("//mutation[@component_type='FirebaseDB']"))

                    number += 1
                f.close()
            else:
                # pre každý súbor zísakme potrebné údaje
                data["blocksPerProject"][file.title] = number_of_blocks_per_project
                data["screensPerProject"][file.title] = number_of_screens_per_project
                data["buttonsPerProject"][file.title] = number_of_buttons
                data["checkboxesPerProject"][file.title] = number_of_checkboxes
                data["datepickersPerProject"][file.title] = number_of_datepickers
                data["imagesPerProject"][file.title] = number_of_images
                data["labelsPerProject"][file.title] = number_of_labels
                data["listpickersPerProject"][file.title] = number_of_listpickers
                data["listviewsPerProject"][file.title] = number_of_listviews
                data["notifiersPerProject"][file.title] = number_of_notifiers
                data["passwordtextboxesPerProject"][file.title] = number_of_passwordtextboxes
                data["slidersPerProject"][file.title] = number_of_sliders
                data["spinnersPerProject"][file.title] = number_of_spinners
                data["switchesPerProject"][file.title] = number_of_switches
                data["textboxesPerProject"][file.title] = number_of_textboxes
                data["timepickersPerProject"][file.title] = number_of_timepickers
                data["webviewersPerProject"][file.title] = number_of_webviewers
                data["horizontalArrangmentPerProject"][file.title] = number_of_horizontalArr
                data["horizontalScrollArrangmentPerProject"][file.title] = number_of_horizontalScrollArr
                data["tableArrangmentPerProject"][file.title] = number_of_tableArr
                data["verticalArrangmentPerProject"][file.title] = number_of_verticalArr
                data["verticalScrollArrangmentPerProject"][file.title] = number_of_verticalScrollArr
                data["camcordersPerProject"][file.title] = number_of_camcorder
                data["camerasPerProject"][file.title] = number_of_cameras
                data["imagepickersPerProject"][file.title] = number_of_imagepickers
                data["playersPerProject"][file.title] = number_of_players
                data["soundsPerProject"][file.title] = number_of_sounds
                data["soundrecordersPerProject"][file.title] = number_of_soundrecorders
                data["speechrecognizersPerProject"][file.title] = number_of_speechrecognizers
                data["texttospeechsPerProject"][file.title] = number_of_texttospeechs
                data["videoplayersPerProject"][file.title] = number_of_videoplayers
                data["yandextranslatorsPerProject"][file.title] = number_of_yandextranslators
                data["ballsPerProject"][file.title] = number_of_balls
                data["canvasesPerProject"][file.title] = number_of_canvases
                data["imagespritesPerProject"][file.title] = number_of_imagesprites
                data["circlesPerProject"][file.title] = number_of_circles
                data["featurecollectionsPerProject"][file.title] = number_of_featurecollections
                data["linestringsPerProject"][file.title] = number_of_linestrings
                data["mapsPerProject"][file.title] = number_of_maps
                data["markersPerProject"][file.title] = number_of_markers
                data["navigationsPerProject"][file.title] = number_of_navigations
                data["polygonsPerProject"][file.title] = number_of_polygons
                data["rectanglesPerProject"][file.title] = number_of_rectangles
                data["accelerometerSensorsPerProject"][file.title] = number_of_accelerometerSensors
                data["barcodeScannersPerProject"][file.title] = number_of_barcodeScanners
                data["barometersPerProject"][file.title] = number_of_barometers
                data["clocksPerProject"][file.title] = number_of_clocks
                data["gyroscopeSensorsPerProject"][file.title] = number_of_gyroscopeSensors
                data["hygrometersPerProject"][file.title] = number_of_hygrometers
                data["lightSensorsPerProject"][file.title] = number_of_lightSensors
                data["locationSensorsPerProject"][file.title] = number_of_locationSensors
                data["magneticFieldSensorsPerProject"][file.title] = number_of_magneticFieldSensors
                data["nearFieldsPerProject"][file.title] = number_of_nearFields
                data["orientationSensorsPerProject"][file.title] = number_of_orientationSensors
                data["pedometersPerProject"][file.title] = number_of_pedometers
                data["proximitySensorsPerProject"][file.title] = number_of_proximitySensors
                data["thermometersPerProject"][file.title] = number_of_thermometers
                data["contactPickersPerProject"][file.title] = number_of_contactPickers
                data["emailPickersPerProject"][file.title] = number_of_emailPickers
                data["phoneCallsPerProject"][file.title] = number_of_phoneCalls
                data["phoneNumberPickersPerProject"][file.title] = number_of_phoneNumberPickers
                data["sharingsPerProject"][file.title] = number_of_sharings
                data["textingsPerProject"][file.title] = number_of_textings
                data["twittersPerProject"][file.title] = number_of_twitters
                data["cloudDbsPerProject"][file.title] = number_of_cloudDbs
                data["filesPerProject"][file.title] = number_of_files
                data["tinyDbsPerProject"][file.title] = number_of_tinyDbs
                data["tinyWebDbsPerProject"][file.title] = number_of_tinyWebDbs
                data["activityStartersPerProject"][file.title] = number_of_activityStarters
                data["bluetoothClientsPerProject"][file.title] = number_of_bluetoothClients
                data["bluetoothServersPerProject"][file.title] = number_of_bluetoothServers
                data["serialsPerProject"][file.title] = number_of_serials
                data["websPerProject"][file.title] = number_of_webs
                data["nxtDrivesPerProject"][file.title] = number_of_nxtDrives 
                data["nxtLightSensorsPerProject"][file.title] = number_of_nxtLightSensors
                data["nxtColorSensorsPerProject"][file.title] = number_of_nxtColorSensors
                data["nxtSoundSensorsPerProject"][file.title] = number_of_nxtSoundSensors 
                data["nxtTouchSensorsPerProject"][file.title] = number_of_nxtTouchSensors
                data["nxtUltrasonicSensorsPerProject"][file.title] = number_of_nxtUltrasonicSensors 
                data["nxtDirectCommandsPerProject"][file.title] = number_of_nxtDirectCommands 
                data["ev3MotorsPerProject"][file.title] = number_of_ev3Motors 
                data["ev3ColorSensorsPerProject"][file.title] = number_of_ev3ColorSensors 
                data["ev3GyroSensorsPerProject"][file.title] = number_of_ev3GyroSensors 
                data["ev3TouchSensorsPerProject"][file.title] = number_of_ev3TouchSensors 
                data["ev3UltrasonicSensorsPerProject"][file.title] = number_of_ev3UltrasonicSensors 
                data["ev3SoundsPerProject"][file.title] = number_of_ev3Sounds 
                data["ev3UIsPerProject"][file.title] = number_of_ev3UIs
                data["ev3CommandsPerProject"][file.title] = number_of_ev3Commands
                data["firebaseDbsPerProject"][file.title] = number_of_firebaseDbs

                number_of_blocks_per_project = 0
                number_of_screens_per_project = 0
                number_of_buttons = 0
                number_of_checkboxes = 0
                number_of_datepickers = 0
                number_of_images = 0
                number_of_labels = 0
                number_of_listpickers = 0
                number_of_listviews = 0
                number_of_notifiers = 0
                number_of_passwordtextboxes = 0
                number_of_sliders = 0
                number_of_spinners = 0
                number_of_switches = 0
                number_of_textboxes = 0
                number_of_timepickers = 0
                number_of_webviewers = 0
                number_of_horizontalArr = 0
                number_of_horizontalScrollArr = 0
                number_of_tableArr = 0
                number_of_verticalArr = 0
                number_of_verticalScrollArr = 0
                number_of_camcorder = 0
                number_of_cameras = 0
                number_of_imagepickers = 0
                number_of_players = 0
                number_of_sounds = 0
                number_of_soundrecorders = 0
                number_of_speechrecognizers = 0
                number_of_texttospeechs = 0
                number_of_videoplayers = 0
                number_of_yandextranslators = 0
                number_of_balls = 0
                number_of_canvases = 0
                number_of_imagesprites = 0
                number_of_circles = 0
                number_of_featurecollections = 0
                number_of_linestrings = 0
                number_of_maps = 0
                number_of_markers = 0
                number_of_navigations = 0
                number_of_polygons = 0
                number_of_rectangles = 0
                number_of_accelerometerSensors = 0
                number_of_barcodeScanners = 0
                number_of_barometers = 0
                number_of_clocks = 0
                number_of_gyroscopeSensors = 0
                number_of_hygrometers = 0
                number_of_lightSensors = 0
                number_of_locationSensors = 0
                number_of_magneticFieldSensors = 0
                number_of_nearFields = 0
                number_of_orientationSensors = 0
                number_of_pedometers = 0
                number_of_proximitySensors = 0
                number_of_thermometers = 0
                number_of_contactPickers = 0
                number_of_emailPickers = 0
                number_of_phoneCalls = 0
                number_of_phoneNumberPickers = 0
                number_of_sharings = 0
                number_of_textings = 0
                number_of_twitters = 0
                number_of_cloudDbs = 0
                number_of_files = 0
                number_of_tinyDbs = 0
                number_of_tinyWebDbs = 0
                number_of_activityStarters = 0
                number_of_bluetoothClients = 0
                number_of_bluetoothServers = 0
                number_of_serials = 0
                number_of_webs = 0
                number_of_nxtDrives = 0
                number_of_nxtColorSensors = 0
                number_of_nxtLightSensors = 0
                number_of_nxtSoundSensors = 0
                number_of_nxtTouchSensors = 0
                number_of_nxtUltrasonicSensors = 0
                number_of_nxtDirectCommands = 0
                number_of_ev3Motors = 0
                number_of_ev3ColorSensors = 0
                number_of_ev3GyroSensors = 0
                number_of_ev3TouchSensors = 0
                number_of_ev3UltrasonicSensors = 0
                number_of_ev3Sounds = 0
                number_of_ev3UIs = 0
                number_of_ev3Commands = 0
                number_of_firebaseDbs = 0

                noMoreScreens = True


        noMoreScreens = False
        number = 1
        # pokiaľ sú v porjekte nejaké obrazovky
        while noMoreScreens == False:
            # zoberieme JSON súbor Screen.scm
            if os.path.isfile("./media/unzipped_files/"+str(file.id)+"/Screen"+str(number)+".scm"):
                f = open("./media/unzipped_files/"+str(file.id)+"/Screen"+str(number)+".scm", "r", encoding="utf-8")
                # prečítame súbor
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
    data['basicStats']['Average number of screens'] = round(number_of_screens / number_of_projects,1)
    data['basicStats']['Average number of blocks'] = round(number_of_blocks / number_of_projects,1)
    data['basicStats']['Average number of components'] = round(number_of_components / number_of_projects,1)
    data['basicStats']['Average number of built-in blocks'] = round((control_blocks + logic_blocks + math_blocks + text_blocks + lists_blocks + dictionaries_blocks + colors_blocks + variables_blocks + procedures_blocks + helpers_names_blocks) / number_of_projects,1)
    data['basicStats']['Average number of component blocks'] = round((event_blocks + setGet_blocks + method_blocks + componentObject_blocks + helpers_assets_blocks) / number_of_projects,1)
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


