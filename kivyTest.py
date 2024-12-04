from kivy.app import App
from kivy.lang import Builder

class HelloWorldApp(App):
    def build(self):
        return Builder.load_file("main.kv")
    
HelloWorldApp().run()

#orientation can be vertical or horizontal
#labels are for text
#textinput is for text. hint_text is preview text
#button is for button. onpress is onpress
#checkbox CheckBox id: check_box active: True Label: text:"Check me"
#slider Slider