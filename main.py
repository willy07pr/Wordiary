from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from database import Database
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
import webbrowser

#import seluruh screen
from mainscreen import MainScreen
from wordscreen import WordScreen
from songscreen import SongReferences
from diaryscreen import DiaryScreen
from historyscreen import HistoryScreen
from resultscreen import ResultScreen
from settingscreen import SettingScreen
from createpin import BuatPINScreen
from changepin import GantiPINScreen
from deletepin import HapusPINScreen
from verifypinscreen import VerifyDiary, VerifyHistory
from lupapinscreen import LupaPin

#atur ukuran/size dari window
Window.size = (360,640)

db = Database() #sambungkan koneksi database

#tampilan bar naviagasi
class ContentNavigationDrawer(BoxLayout):
    nav_drawer = ObjectProperty(None)
    sm = ObjectProperty(None)


    def diary(self):
        if VerifyDiary().changepin() == None:
            return 'diary' #pindah ke diary screen bila pin belum ada
        else:
            return 'verifydiary' #pindah ke verify pin screen bila pin sudah ada

    def history(self):
        if VerifyDiary().changepin() == None:
            return 'history' #pindah ke history screen bila pin belum ada
        else:
            return 'verifyhistory' #pindah ke pin screen bila pin sudah ada

    def aboutus(self): #membuka websites dari developer
        webbrowser.open('https://sites.google.com/view/wordiary/home',
                        new=2, autoraise=True)


#membuat screen manager
sm = ScreenManager()
screens = [MainScreen(name='main'), WordScreen(name='word'),
           DiaryScreen(name='diary'), HistoryScreen(name='history'),
           VerifyHistory(name='verifyhistory'), ResultScreen(name='resultscreen'),
           VerifyDiary(name='verifydiary'), SongReferences(name='reflagu'),
           SettingScreen(name='settings'), BuatPINScreen(name='buatpin'),
           GantiPINScreen(name='gantipin'), HapusPINScreen(name='hapuspin'), LupaPin(name='lupapin')]
#tambahkan setiap screen ke dalam widget
for screen in screens:
    sm.add_widget(screen)

#menginisialisasi app
class WordiaryApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue" #warna utama tampilan
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Dark" #tema
        return Builder.load_file('md.kv') #load file kv

    def on_pause(self):
        return True #memungkinkan pause saat app berjalan

    def on_stop(self):
        #tutup koneksi database saat app berhenti
        db.close()

#menjalankan app
WordiaryApp().run()


#semangat gais
