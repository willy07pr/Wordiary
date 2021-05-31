from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from database import Database

db = Database()

#screen membuat pin
class BuatPINScreen(Screen):

    newpin = ObjectProperty(None)
    confirmpin = ObjectProperty(None)
    pertanyaan = ObjectProperty(None)
    jawaban = ObjectProperty(None)
    aturulang = ObjectProperty(None)

    def savepin(self):
    	#jika pin kurang dari 4 digit angka
        if len(self.newpin.text) < 4 or not self.newpin.text.isdecimal(): 
            digitkurang = MDDialog(text='Harap masukkan minimal 4 digit angka.',
                             size_hint=(0.7,0.2))
            digitkurang.open()
            return 'buatpin'
        else:
            if self.newpin.text == self.confirmpin.text and self.pertanyaan.text != '' and self.jawaban.text != '':
                berhasil = MDDialog(text='PIN berhasil dibuat.',
                                    size_hint=(0.6,0.2))
                berhasil.open()
                db.deletepin() #menghapus pin sebelumnya jika sudah ada
                db.addpin(self.newpin.text, self.pertanyaan.text, self.jawaban.text) #memasukkan pin ke database
                return 'settings'
            elif self.pertanyaan.text == '' or self.jawaban.text == '':
                peringatan = MDDialog(text='Harap buat pertanyaan dan jawaban untuk lupa pin.',
                                      size_hint=(0.7,0.2))
                peringatan.open()
                return 'buatpin'
            else: #jika pin dan konfirmasinya tidak pas/sama
                tidaksama = MDDialog(text='Harap masukkan angka yang sama saat konfirmasi.',
                                 size_hint=(0.7, 0.2))
                tidaksama.open()
                return 'buatpin'

    def fill(self):
        self.pertanyaan.text = db.question()
        self.jawaban.text = db.forget()
        self.aturulang.text = "Atur ulang PIN Anda"

    def clear(self):
        self.newpin.text = ''
        self.confirmpin.text = ''

    def clearpertanyaan(self):
        self.pertanyaan.text = ''
        self.jawaban.text = ''
        self.aturulang.text = ''
