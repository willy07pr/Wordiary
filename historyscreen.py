from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from database import Database

db = Database()

#screen pencarian diary
class HistoryScreen(Screen):

    searchdate = ObjectProperty(None)
    datelist = db.getdiarydate()
    #print(datelist)

    def search(self):
        if self.searchdate.text[-4:].isnumeric()==False or int(self.searchdate.text[3:5])>12:
            #menampilkan popup format tanggal tidak sesuai
            format = MDDialog(text='Format tanggal tidak sesuai',
                              size_hint=(0.7,0.2))
            format.open()
        elif self.searchdate.text in self.updatedate():
            #menampilan judul dan text diary sesuai tanggal yang diinput di screen hasil pencarian
            self.manager.get_screen('resultscreen').searchtext()
        else: #menampilkan popup bahwa data tidak ditemukan
            gaada = MDDialog(text='Data tidak ditemukan.',
                             size_hint=(0.7,0.2))
            gaada.open()

    def datechecking(self): #pengecekan tanggal
        if self.searchdate.text in self.updatedate():
            #self.searchdate.text = ''
            return 'resultscreen' #pindah ke screen hasil pencarian diary
        else:
            #self.searchdate.text = ''
            return 'history' #tetap di screen pencarian history

    def balik(self):
        return self.searchdate.text #mengembalikan nilai dari tanggal yang diinput

    def clear(self):
        self.searchdate.text = ''

    def updatedate(self):
        #cek pembaruan tanggal dari database
        return db.getdiarydate()
