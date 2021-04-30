from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database import Database
from verifypinscreen import VerifyDiary

db = Database()

#screen untuk menampilkan kata penyemangat
class WordScreen(Screen):
    wordtext = ObjectProperty(None)

    def showtext(self,kondisi):
        if kondisi == 'sedih':
            lbl1 = db.output_sad() #import kata dari database untuk pilihan sedih
            self.wordtext.text = lbl1
        elif kondisi == 'marah':
            lbl2 = db.output_angry() #import kata dari database untuk pilihan marah
            self.wordtext.text = lbl2
        elif kondisi == 'sakit':
            lbl3 = db.output_sick() #import kata dari database untuk pilihan sakit
            self.wordtext.text = lbl3
        else:
            lbl4 = db.output_broke() #import kata dari database untuk pilihan patah hati
            self.wordtext.text = lbl4

    def writebtn(self):
        if VerifyDiary().changepin() == None:
            return 'diary' #pindah ke diary screen bila pin belum ada
        else:
            return 'verifydiary' #pindah ke pin screen bila pin sudah ada
