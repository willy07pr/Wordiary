from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from database import Database
import webbrowser

db = Database()

#screen referensi lagu
class SongReferences(Screen):
    
    textlagu = ObjectProperty(None)
    link = ''

    def song(self): #membuka link youtube dari rekomendasi lagu
        webbrowser.open(self.link, new=1, autoraise=True)

    def showsong(self,kondisi):
        if kondisi == 'sedih':
            global judul1
            judul1=db.sadsong()
            self.textlagu.text = judul1[1] #menampilkan rekomendasi lagu untuk pilihan sedih
        elif kondisi == 'marah':
            global judul2
            judul2 = db.angrysong()
            self.textlagu.text = judul2[1] #menampilkan rekomendasi lagu untuk pilihan marah
        elif kondisi == 'sakit':
            global judul3
            judul3 = db.sicksong()
            self.textlagu.text = judul3[1] #menampilkan rekomendasi lagu untuk pilihan sakit
        else:
            global judul4
            judul4 = db.brokensong()
            self.textlagu.text = judul4[1] #menampilkan rekomendasi lagu untuk pilihan patah hati

    def showlink(self,kondisi): #untuk menyesuaikan lagu dengan link
        if kondisi == 'sedih':
            self.link = judul1[0]
        elif kondisi == 'marah':
            self.link = judul2[0]
        elif kondisi == 'sakit':
            self.link = judul3[0]
        else:
            self.link = judul4[0]
