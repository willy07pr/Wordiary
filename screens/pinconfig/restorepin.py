from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from database import Database

db = Database()

#scren untuk lupa pin
class LupaPin(Screen):

    jawaban = ObjectProperty(None)
    pertanyaan = ObjectProperty(None)

    def showpertanyaan(self):
        #menampilkan pertanyaan yang sesuai saat membuat pin
        self.pertanyaan.text = db.question()

    def lupapin(self):
        if self.jawaban.text.lower() == db.forget().lower():
            self.manager.get_screen('buatpin').fill()
            return 'buatpin' #jika jawaban sesuai, arahkan untuk membuat pin ulang
        else:
            salah = MDDialog(text='Jawaban Anda salah.',
                             size_hint=(0.7,0.2))
            salah.open() #tampilkan popup jika jawaban tidak sesuai
            return 'lupapin'

    def clear(self):
        self.jawaban.text = ''
