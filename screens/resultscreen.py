from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database import Database

db = Database()

#screen hasil pencarian diary
class ResultScreen(Screen):

    diarytext = ObjectProperty(None)
    title = ObjectProperty(None)

    def searchtext(self): #menampilkan diary yang telah dibuat sesuai tanggal yang diinput
        self.title.text = db.searchtitle(self.manager.get_screen('history').balik())
        self.diarytext.text = db.searchdiary(self.manager.get_screen('history').balik())

    def edit(self): #pindah ke diary screen dengan mode edit
        self.manager.get_screen('diary').showdata(self.diarytext.text,
                                                  self.manager.get_screen('history').balik(),
                                                  self.title.text)

    def clear(self):
        #membersihkan text pencarian
        self.manager.get_screen('history').clear()

