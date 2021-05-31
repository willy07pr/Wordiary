import webbrowser
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, SlideTransition
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from database import Database

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
from restorepin import LupaPin

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
class ScreenManagement(ScreenManager):

    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__()
        Window.bind(on_keyboard=self.on_key)

    #membuat konfigurasi tombol back pada android
    def on_key(self, window, key, *args):
        if key == 27:
            if self.current_screen.name == 'main':
                return False #keluar dari app
            elif self.current_screen.name == 'word':
                #pindah ke main screen
                self.transition = SlideTransition(direction='right')
                self.current = 'main'
                return True #app tetap berjalan
            elif self.current_screen.name == 'reflagu':
                return True #app tetap berjalan
            elif self.current_screen.name == 'diary':
                #pindah ke main screen
                self.transition = SlideTransition(direction='right')
                self.current = 'main'
                return True #app tetap berjalan
            elif self.current_screen.name == 'resultscreen':
                #pindah ke history screen
                self.transition = SlideTransition(direction='right')
                self.current = 'history'
                return True #app tetap berjalan
            elif self.current_screen.name in ['buatpin','gantipin','hapuspin','lupapin']:
                #pindah ke settings screen
                self.transition = SlideTransition(direction='right')
                self.current = 'settings'
                return True #app tetap berjalan
            elif self.current_screen.name in ['verifydiary','verifyhistory']:
                #pindah ke main screen
                self.transition = SlideTransition(direction='right')
                self.current = 'main'
                return True #app tetap berjalan

#menginisialisasi app
class WordiaryApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Blue" #warna utama tampilan
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Dark" #tema
        return Builder.load_file('main.kv') #load file kv

    def on_pause(self):
        return True #memungkinkan pause saat app berjalan

    def on_stop(self):
        #tutup koneksi database saat app berhenti
        db.close()

#menjalankan app
WordiaryApp().run()
