from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from verifypinscreen import VerifyDiary
from database import Database

db = Database()

#screen ganti pin
class GantiPINScreen(Screen):

    pin = ObjectProperty(None)

    def ganti(self):
        #jika pin yang diisi sesuai
        if VerifyDiary().changepin() == self.pin.text:
            self.pin.text = ''
            return 'buatpin' #pindah ke screen buat pin
        #jika pin yang diisi tidak sesuai
        else:
            invalidpin = MDDialog(text='PIN salah',
                                  size_hint=(0.6, 0.2))
            invalidpin.open()
            self.pin.text = ''
            return 'gantipin' #tetap di screen ganti pin

    def clear(self):
        self.pin.text = ''
