from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDDatePicker
from database import Database

db = Database()

#screen pencarian diary
class HistoryScreen(Screen):

    searchdate = ObjectProperty(None)
    datelist = db.getdiarydate()
    
    def on_save(self, date):
        temp_date = str(date)[8:]
        temp_month = str(date)[5:7]
        temp_year = str(date)[:4]
        self.searchdate.text = temp_date + '-' + temp_month + '-' + temp_year
        
    def opencalendar(self):
        calendar = MDDatePicker(callback=self.on_save)
        calendar.open()

    def search(self):
        if not self.searchdate.text[-4:].isnumeric() \
                or len(self.searchdate.text)!=10 \
                or int(self.searchdate.text[3:5])>12 \
                or self.searchdate.text[2:6:3] != '--':
            #menampilkan popup format tanggal tidak sesuai
            format = MDDialog(text='Format tanggal tidak sesuai',
                              size_hint=(0.7,0.2))
            format.open()
            self.clear()
        elif self.searchdate.text in self.updatedate():
            #menampilan judul dan text diary sesuai tanggal yang diinput di screen hasil pencarian
            self.manager.get_screen('resultscreen').searchtext()
        else: #menampilkan popup bahwa data tidak ditemukan
            gaada = MDDialog(text='Data tidak ditemukan.',
                             size_hint=(0.7,0.2))
            gaada.open()
            self.clear()

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
