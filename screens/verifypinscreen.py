from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from database import Database

db = Database()

#screen konfirmasi pin menuju diary
class VerifyDiary(Screen):

    pin = ObjectProperty(None)
    print("PIN :", db.verifypin())
    index = ''

    def submit(self):
        if self.pin.text == self.changepin(): #cek pin
            return 'diary'
        else:
            invalidpin = MDDialog(text='PIN salah',
                                  size_hint=(0.6,0.2))
            invalidpin.open() #menampilkan popup jika salah
            return 'verifydiary'

    def changepin(self): #memanggil pin dari database untuk pengecekan
        check_pin = db.verifypin()
        return check_pin

    def changeindex(self,indexs):
        self.index = indexs

    def clear(self):
        self.pin.text = '' #bersihkan pin setelah selesai


#screen konfirmasi pin menuju history
class VerifyHistory(Screen):

    pin = ObjectProperty(None)

    def submit(self):
        if self.pin.text == VerifyDiary().changepin(): #cek pin
            return 'history' #pindah ke screen history jika benar
        else:
            invalidpin = MDDialog(text='PIN salah',
                                  size_hint=(0.6,0.2))
            invalidpin.open() #menampilkan popup jika salah
            return 'verifyhistory'

    def clear(self):
        self.pin.text = ''
