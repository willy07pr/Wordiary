from kivy.uix.screenmanager import Screen
from kivymd.uix.dialog import MDDialog
from database import Database
from verifypinscreen import VerifyDiary

db = Database()

#screen pengaturan pin
class SettingScreen(Screen):

    def buatpin(self):
        # cek apakah pin sudah ada atau belum
        if VerifyDiary().changepin() == None:
            return 'buatpin' #pindah ke screen buat pin bila pin belum ada
        else:
            sudahbuatpin = MDDialog(
                text='Anda sudah membuat PIN sebelumnya.\nAnda dapat melakukan opsi Ganti PIN atau Hapus PIN.',
                                    size_hint=(0.7,0.2))
            sudahbuatpin.open()
            return 'settings' #tetap di screen pengaturan bila pin sudah ada

    def gantipin(self):
        # cek apakah pin sudah ada atau belum
        if VerifyDiary().changepin() != None:
            return 'gantipin' #pindah ke screen ganti pin bila pin sudah ada
        else:
            belumbuatpin = MDDialog(
                text='Anda belum membuat PIN sebelumnya.\nAnda dapat melakukan opsi Buat PIN.',
                                    size_hint=(0.7,0.2))
            belumbuatpin.open()
            return 'settings' #tetap di screen pengaturan bila pin belum ada

    def hapuspin(self):
        # cek apakah pin sudah ada atau belum
        if VerifyDiary().changepin() != None:
            return 'hapuspin' #pindah ke screen hapus pin bila pin sudah ada
        else:
            belumbuatpin = MDDialog(
                text='Anda belum membuat PIN sebelumnya.\nAnda'
                     ' dapat melakukan opsi Buat PIN.',
                                    size_hint=(0.7, 0.2))
            belumbuatpin.open()
            return 'settings' #tetap di screen pengaturan bila pin belum ada

    def lupapin(self):
        self.manager.get_screen('lupapin').showpertanyaan()
