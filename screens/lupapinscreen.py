from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from database import Database

db = Database()

class LupaPin(Screen):
    jawaban = ObjectProperty(None)
    pertanyaan = ObjectProperty(None)

    def showpertanyaan(self):
        self.pertanyaan.text = db.question()

    def lupapin(self):
        if self.jawaban.text == db.forget():
            self.manager.get_screen('buatpin').fill()
            return 'buatpin'
        else:
            salah = MDDialog(text='Jawaban Anda salah.',
                             size_hint=(0.7,0.2))

    def clear(self):
        self.jawaban.text = ''