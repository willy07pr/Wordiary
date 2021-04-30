from kivy.uix.screenmanager import Screen

class MainScreen(Screen):

    #menampilkan kata penyemangat untuk pilihan sedih
    def output1(self):
        self.manager.get_screen('word').showtext('sedih')
        self.manager.get_screen('reflagu').showsong('sedih')
        self.manager.get_screen('reflagu').showlink('sedih')

    #menampilkan kata penyemangat untuk pilihan marah
    def output2(self):
        self.manager.get_screen('word').showtext('marah')
        self.manager.get_screen('reflagu').showsong('marah')
        self.manager.get_screen('reflagu').showlink('marah')

    #menampilkan kata penyemangat untuk pilihan sakit
    def output3(self):
        self.manager.get_screen('word').showtext('sakit')
        self.manager.get_screen('reflagu').showsong('sakit')
        self.manager.get_screen('reflagu').showlink('sakit')

    #menampilkan kata penyemangat untuk pilihan patah hati
    def output4(self):
        self.manager.get_screen('word').showtext('patah hati')
        self.manager.get_screen('reflagu').showsong('patah hati')
        self.manager.get_screen('reflagu').showlink('patah hati')
