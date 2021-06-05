from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.picker import MDDatePicker
from kivymd.toast import toast
from database import Database
from historyscreen import HistoryScreen

db = Database()

#screen diary
class DiaryScreen(Screen):

    diary = ObjectProperty(None)
    date = ObjectProperty(None)
    title = ObjectProperty(None)

    def save(self): #menyimpan diary
        # jika format tidak sesuai
        if not self.date.text[-4:].isnumeric() \
                or len(self.date.text)!=10 \
                or int(self.date.text[3:5])>12 \
                or self.date.text[2:6:3] != '--':
            format = MDDialog(text='Gunakan format tanggal dd-mm-yyyy',
                              size_hint=(0.7,0.2))
            format.open()
        #jika tanggal yang diisi belum ada di database
        elif self.date.text not in HistoryScreen().updatedate():
            db.insertdiary(self.diary.text, self.date.text, self.title.text)
            self.showtoast()
        #jika tanggal yang diisi sudah ada di database
        else:
            db.deletediary(self.date.text)
            db.insertdiary(self.diary.text, self.date.text,self.title.text)
            self.showtoast()
        self.manager.get_screen('history').clear()

    def on_save(self, date):
        temp_date = str(date)[8:]
        temp_month = str(date)[5:7]
        temp_year = str(date)[:4]
        self.date.text = temp_date + '-' + temp_month + '-' + temp_year
        
    def opencalendar(self):
        calendar = MDDatePicker(callback=self.on_save)
        calendar.open()

    def showtoast(self):
        self.diary.text = ""
        self.date.text = ""
        self.title.text = ""
        toast("Diary berhasil disimpan")

    def showdata(self,text,date,title): #menampilkan tulisan dari diary yang akan di edit
        self.diary.text = text
        self.date.text = date
        self.title.text = title

    def clear(self): #membersihkan kanvas diary
        self.diary.text = ''
        self.date.text = ''
        self.title.text = ''
        self.manager.get_screen('history').clear()
