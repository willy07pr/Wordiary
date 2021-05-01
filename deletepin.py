from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from verifypinscreen import VerifyDiary
from database import Database

db = Database()

#screen hapus pin
class HapusPINScreen(Screen):

    pin = ObjectProperty(None)

    def hapus(self):
        #jika pin yang diisi sudah sesuai
        if self.pin.text == VerifyDiary().changepin():
            self.manager.get_screen('buatpin').clearpertanyaan()
            db.deletepin() #menghapus pin dari database
            berhasilhapus = MDDialog(text='PIN Anda telah terhapus.',
                                     size_hint=(0.6,0.2))
            berhasilhapus.open()
            return 'settings'
        else:
            invalidpin = MDDialog(text='PIN salah',
                                  size_hint=(0.6, 0.2))
            invalidpin.open() #tampilkan popup jika pin salah
            return 'hapuspin'

    def clear(self):
        self.pin.text = ''
