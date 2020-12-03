from kivy.app import App
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from menu_prices import PRICES

Builder.load_file("views/screen_one/screen_one.kv")
Builder.load_file("views/screen_two/screen_two.kv")
Builder.load_file("views/screen_three/screen_three.kv")
Builder.load_file("views/screen_four/screen_four.kv")

class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super(FirstScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class SecondScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class ThirdScreen(Screen):
    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class FourthScreen(Screen):
    def __init__(self, **kwargs):
        super(FourthScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class MyScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.running_total = 0

    def add_to_total(self, button_name):
        self.running_total += PRICES[button_name.lower()]
        self.update_all_screen_totals()

    def snacks_screen_selected(self):
        self.app.root.switch_screen('_first_screen_')

    def switch_screen(self, screen_name):
        self.current = screen_name

    def drinks_screen_selected(self):
        self.app.root.switch_screen('_second_screen_')
    
    def reset_running_total(self):
        self.running_total = 0
        self.update_all_screen_totals()
    
    def retail_screen_selected(self):
        self.app.root.switch_screen('_third_screen_')
    
    def food_screen_selected(self):
        self.app.root.switch_screen('_fourth_screen_')

    def receipt_screen_selected(self):
        self.app.root.switch_screen('_fifth_screen_')

    def update_all_screen_totals(self):
        self.ids.first_screen.ids.running_total.text = '$' + str(self.running_total)
        self.ids.second_screen.ids.running_total.text = '$ ' + str(self.running_total)
        self.ids.third_screen.ids.running_total.text = '$ ' + str(self.running_total)
        self.ids.fourth_screen.ids.running_total.text = '$ ' + str(self.running_total)

class SwitchingScreenApp(App):

    def build(self):
        return MyScreenManager()


if __name__ == "__main__":
    SwitchingScreenApp().run()