from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.lang import Builder
from menu_prices import PRICES
import csv
import threading
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.recycleview import RecycleView

Builder.load_file("views/menu_screen/menu_screen.kv")
Builder.load_file("views/sign_in/sign_in.kv")
Builder.load_file("views/drinks_screen/drinks_screen.kv")
Builder.load_file("views/retail_screen/retail_screen.kv")
Builder.load_file("views/food_screen/food_screen.kv")
Builder.load_file("views/reciept_screen/reciept_screen.kv")
Builder.load_file("views/screen_six/screen_six.kv")
Builder.load_file("views/snacks_screen/snacks_screen.kv")
Builder.load_file("views/start_count_screen/start_count_screen.kv")
Builder.load_file("views/acounts_receivable_screen/acounts_receivable_screen.kv")
Builder.load_file("views/hub_screen/hub_screen.kv")
Builder.load_file("views/payment_method/payment_method.kv")
Builder.load_file("views/choose_item/choose_item.kv")
Builder.load_file("views/chips_screen/chips_screen.kv")
Builder.load_file("views/candy_screen/candy_screen.kv")
Builder.load_file("views/combos_screen/combos_screen.kv")
Builder.load_file("views/gatorade_bar_screen/gatorade_bar_screen.kv")
Builder.load_file("views/pastry_screen/pastry_screen.kv")
Builder.load_file("views/island_snacks_screen/island_snacks_screen.kv")

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class AcountsReceivableScreen(Screen):
    def __init__(self, **kwargs):
        super(AcountsReceivableScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class DrinksScreen(Screen):
    def __init__(self, **kwargs):
        super(DrinksScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class HubScreen(Screen):
    def __init__(self, **kwargs):
        super(HubScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.selected_building_number_list = []
    
    def add_to_call_list(self):

        # scrape the data from the UI
        building_number = self.ids.building_number.text

        # create the listview string
        text_string = f'{building_number}'
        list_view_string = {"text": text_string}

        # add the listview string to the listview string list
        self.selected_building_number_list.append(list_view_string)

        # update the UI listview
        self.ids.calls_listview.update_list_view(self.selected_building_number_list)

    def add_to_accepted_call_list(self):

        # scrape the data from the UI
        building_number = self.ids.building_number.text
        self.ids.accepted_calls_listview.update_list_view(self.selected_building_number_list)

        # loop thru call_list
        for i in range(len(self.selected_building_number_list)):

            # check: is building number in list?
            if building_number in self.selected_building_number_list[i]["text"]:
                # yes: remove it
                self.selected_building_number_list.remove(self.selected_building_number_list[i])
        
            self.ids.calls_listview.update_list_view(self.selected_building_number_list)
        

class RetailScreen(Screen):
    def __init__(self, **kwargs):
        super(RetailScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class FoodScreen(Screen):
    def __init__(self, **kwargs):
        super(FoodScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class RecieptScreen(Screen):
    def __init__(self, **kwargs):
        super(RecieptScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class SixthScreen(Screen):
    def __init__(self, **kwargs):
        super(SixthScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class Sign_In(Screen):
    def __init__(self, **kwargs):
        super(Sign_In, self).__init__(**kwargs)
        self.app = App.get_running_app()


class SnacksScreen(Screen):
    def __init__(self, **kwargs):
        super(SnacksScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class Payment_Method(Screen):
    def __init__(self, **kwargs):
        super(Payment_Method, self).__init__(**kwargs)
        self.app = App.get_running_app()


class Chips_Screen(Screen):
    def __init__(self, **kwargs):
        super(Chips_Screen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class Candy_Screen(Screen):
    def __init__(self, **kwargs):
        super(Candy_Screen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class Combos_Screen(Screen):
    def __init__(self, **kwargs):
        super(Combos_Screen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class Gatorade_Bar_Screen(Screen):
    def __init__(self, **kwargs):
        super(Gatorade_Bar_Screen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class Island_Snacks_Screen(Screen):
    def __init__(self, **kwargs):
        super(Island_Snacks_Screen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class Pastry_Screen(Screen):
    def __init__(self, **kwargs):
        super(Pastry_Screen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class Choose_Item(Screen):
    def __init__(self, **kwargs):
        super(Choose_Item, self).__init__(**kwargs)
        self.app = App.get_running_app()


class Start_Count_Screen(Screen):

    products_list = [
        'candy',
        'nesquick',
        'red bull',
        'gatorade',
        'monster',
        'water',
        'soda',
        'arizona',
        'v8',
        'langers',
        'star bucks',
        'bang',
        'electrolit',
        'mnt dew',
        'coconut water',
        '5 hour',
        'breakfast',
        'burrito',
        'xl burrito',
        'calzone',
        'big chicken',
        'pbj',
        'brats',
        'F & R',
        'tuna',
        'parfait',
        'pastry',
        'chips',
        'el sabroso',
        'combos',
        'soups',
        'island snacks',
        'SF seeds',
        'pop tarts',
        'takis',
        'fruit snacks',
        'fruit cups',
        'gum',
        'g bar',
        'ciggs',
        'grizzly',
        'stokers',
        'lighters',
        'chapstick',
    ]
    def __init__(self, **kwargs):
        super(Start_Count_Screen, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.selected_product_list = []

        # # init the product store dictionary - all zeros
        # product_store = list(PRICES.keys())
        # empty_list = [0*len(product_store)]
        # self.store_dictionary = dict(zip(product_store, empty_list))

    def add_to_listview(self):

        # scrape the data from the UI
        selected_product = self.ids.product_dropdown.ids.btn.text
        product_count = self.ids.product_count.text

        # create the listview string
        text_string = f'{selected_product}  -  {product_count}'
        list_view_string = {"text": text_string}

        # add the listview string to the listview string list
        self.selected_product_list.append(list_view_string)

        # update the UI listview
        self.ids.product_listview.update_list_view(self.selected_product_list)

    def clear_screen(self):
        '''
            Method to clear the screen and elements
        '''

        print(f'-- Clearing Screen --\n')

        # clear the dropdown
        product_dropdown = self.ids.product_dropdown
        product_dropdown.set_button_text('Select Product')

        # clear the textinput
        text_input = self.ids.product_count
        text_input.text = ''

        # clear the listview
        self.selected_product_list = []

        # update the UI listview
        self.ids.product_listview.update_list_view(self.selected_product_list)

    def populate_dropdown(self):
        print(f'Populating the dropdown \n')

        dropdown = self.ids.product_dropdown.ids.dropdown
        dropdown.clear_widgets()

        for product in self.products_list:
            button = Button(text=product, size_hint_y=None, size_hint_x=1, height="42dp")
            button.bind(on_release=lambda product: self.product_dropdown_selected(dropdown, product))
            dropdown.add_widget(button)

    def product_dropdown_selected(self, dropdown, product):
        self.selected_product = None

        #  set the dropdown text
        dropdown.select(product.text)

    def update_start_count_in_store(self):
        '''
            Method to submit the data to a csv

            returns : none
        '''

        # loop thru list
        for product in self.selected_product_list:

            print(f'This is the product: \n{product}')

            text = product["text"]
            product_name, count = text.split("  -  ")
            product_name = product_name.replace(" ", "_")

            # update the start count for the product in the dictionary
            self.app.root.product_store[product_name][3] = int(count)


class MyScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.product_store = {}
        self.visa_total = 0
        self.mastercard_total = 0  
        self.cash_total = 0 
        self.americanexpress_total = 0 
        self.discover_total = 0 
        self.comp_count = 0
        self.na_count = 0   
        self.ranch_SF_total = 0 
        self.reg_SF_total = 0 
        
        for product, price in list(PRICES.items()):
            # product_store = [ price, current, total, start, remaining ]
            self.product_store[product] = [price, 0, 0, 0,0]


        # TODO - create the email server object
        # self.email_server = EmailServer()

        self.running_total = 0
        self.accounts_receivable_total = 0
        self.start_count_total = ""

    def add_to_item(self, product_name, button):

        product_name = product_name.replace(" ", "_")

        # copy old data from store
        _, count, old_total, _ ,_ = self.product_store[product_name]

        #update product store dictionary values
        self.product_store[product_name][1] += 1
        self.product_store[product_name][2] += 1
        self.product_store[product_name][3] -= 1
        self.product_store[product_name][4] = self.product_store[product_name][3]

        # updating running totals from dictionary values
        self.running_total += self.product_store[product_name][0]
        self.accounts_receivable_total += self.product_store[product_name][0] 

        # update the running total label for each page
        self.update_all_screen_totals()
        self.acounts_receivable_total()
        self.update_receipt_item(product_name)
        
        #switch screens to the menu
        self.app.root.switch_screen('_menu_screen_')
        
    def minus_to_item(self, product_name):
        product_name = product_name.replace(" ", "_")
        # check: is the item count already 0
        if self.product_store[product_name][1] < 1:
            return

        # copy old data from store
        _, count, old_total, _ , remaining_total = self.product_store[product_name]
        self.product_store[product_name][1] -= 1
        self.product_store[product_name][2] -= 1
        self.product_store[product_name][3] += 1
        self.product_store[product_name][4] = self.product_store[product_name][3]
        self.running_total -= self.product_store[product_name][0]
        self.accounts_receivable_total -= self.product_store[product_name][0] 


        # update the running total label for each page
        self.update_all_screen_totals()
        self.acounts_receivable_total()
        self.update_receipt_item(product_name)
        print(f'Updated Item: \n{self.product_store[product_name]}')

    def comp(self):
        self.accounts_receivable_total -= self.running_total 
        self.ids.acounts_receivable_screen.ids.running_total.text = '$' + str(self.running_total)
        self.running_total = 0
        self.update_all_screen_totals()
        self.update_reciept_screen_counts()

    def add_to_total(self, button_name):
        self.running_total += PRICES[button_name.lower()]
        self.update_all_screen_totals()

    def snacks_screen_selected(self):
        self.app.root.switch_screen('_snacks_screen_')

    def switch_screen(self, screen_name):
        self.current = screen_name

    def drinks_screen_selected(self):
        self.app.root.switch_screen('_drinks_screen_')

    def hub_screen_selected(self):
        self.app.root.switch_screen('_hub_screen_')
    
    def add_to_visa(self):
        self.visa_total += self.running_total
        self.ids.payment_method.ids.visa_total.text = '$' + str(self.visa_total)
        self.running_total = 0
        self.update_all_screen_totals()
        self.update_reciept_screen_counts()
        self.app.root.switch_screen('_menu_screen_')

    def add_to_mastercard(self):
        self.mastercard_total += self.running_total
        self.ids.payment_method.ids.MasterCard_total.text = '$' + str(self.mastercard_total)
        self.running_total = 0
        self.update_all_screen_totals()
        self.update_reciept_screen_counts()
        self.app.root.switch_screen('_menu_screen_')

    def add_to_cash(self):
        self.cash_total += self.running_total
        self.ids.payment_method.ids.cash_total.text = '$' + str(self.cash_total)
        self.running_total = 0
        self.update_all_screen_totals()
        self.update_reciept_screen_counts()
        self.app.root.switch_screen('_menu_screen_')

    def add_to_americanexpress(self):
        self.americanexpress_total += self.running_total
        self.ids.payment_method.ids.AmericanExpress_total.text = '$' + str(self.americanexpress_total)
        self.running_total = 0
        self.update_all_screen_totals()
        self.update_reciept_screen_counts()
        self.app.root.switch_screen('_menu_screen_')

    def add_to_discover(self):
        self.discover_total += self.running_total
        self.ids.payment_method.ids.Discover_total.text = '$' + str(self.discover_total)
        self.running_total = 0
        self.update_all_screen_totals()
        self.update_reciept_screen_counts()
        self.app.root.switch_screen('_menu_screen_')

    def comfirm_payment(self):
        self.app.root.switch_screen('_payment_method_')
    
    def acounts_receivable_screen_selected(self):
        self.app.root.switch_screen('_acounts_receivable_screen_')

    def retail_screen_selected(self):
        self.app.root.switch_screen('_retail_screen_')

    def food_screen_selected(self):
        self.app.root.switch_screen('_food_screen_')

    def receipt_screen_selected(self):
        self.app.root.switch_screen('_reciept_screen_')
    
    def routelogs_screen_selected(self):
        self.app.root.switch_screen('_sixth_screen_')
    
    def DIR_screen_selected(self):
        self.app.root.switch_screen('_menu_screen_')
    
    def start_count_screen_selected(self):
        self.app.root.ids.start_count_screen.populate_dropdown()
        self.app.root.switch_screen('_start_count_screen_')

    def user_page_screen_selected(self):
        self.app.root.switch_screen('_sign_in_')

    def update_all_screen_totals(self):
        self.ids.snacks_screen.ids.running_total.text = '$' + str(self.running_total)
        self.ids.drinks_screen.ids.running_total.text = '$ ' + str(self.running_total)
        self.ids.retail_screen.ids.running_total.text = '$ ' + str(self.running_total)
        self.ids.food_screen.ids.running_total.text = '$ ' + str(self.running_total)
        self.ids.reciept_screen.ids.running_total.text = '$ ' + str(self.running_total)
    
    def acounts_receivable_total(self):

        self.ids.acounts_receivable_screen.ids.running_total.text = '$ ' + str(self.accounts_receivable_total)

    def update_receipt_item(self, product_name):
        product_count = self.product_store[product_name][1] 
        product_total = float(self.product_store[product_name][0]) * float(self.product_store[product_name][1])
        old_total = str(self.product_store[product_name][2])

        # get list of keys, search for index of product
        key_list = list(self.ids.reciept_screen.ids)

        self.ids.reciept_screen.ids[f'{product_name}_count'].text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)
        self.ids.acounts_receivable_screen.ids[f'acount_{product_name}_count'].text = f' {product_name}:\n ' + str(self.product_store[product_name][2]) + ' = '+ str(self.product_store[product_name][2]*self.product_store[product_name][0]) + f'\n{self.product_store[product_name][4]}'

    def update_reciept_screen_counts(self):
        # update the product store dictionary counts
        key_list = list(self.product_store.keys())

        for i in key_list:
            self.product_store[i][1] = 0
            product_store_key = f"{i}_count"
            self.ids.reciept_screen.ids[product_store_key].text = ''

#############

    def choose_SF_selected(self):
        self.app.root.switch_screen('_choose_item_')

    def chips_screen_selected(self):
        self.app.root.switch_screen('_chips_screen_')

    def candy_screen_selected(self):
        self.app.root.switch_screen('_candy_screen_')

    def combos_screen_selected(self):
        self.app.root.switch_screen('_combos_screen_')

    def gatorade_bar_screen_selected(self):
        self.app.root.switch_screen('_gatorade_bar_screen_')

    def pastry_screen_selected(self):
        self.app.root.switch_screen('_pastry_screen_')
    
    def island_snacks_screen_selected(self):
        self.app.root.switch_screen('_island_snacks_screen_')
    

###########
class SwitchingScreenApp(App):

    def build(self):
        return MyScreenManager()


class ImageButton(Button):
    pass


class Item(BoxLayout, Label):
    def __init__(self, **kwargs):
        super(Item, self).__init__(**kwargs)


class ProductListView(RecycleView):
    def __init__(self, **kwargs):
        super(ProductListView, self).__init__(**kwargs)
        self.data = []

    def update_list_view(self, new_product_list):
        self.data = []
        self.data = new_product_list


class CallsListView(RecycleView):
    def __init__(self, **kwargs):
        super(CallsListView, self).__init__(**kwargs)
        self.data = []

    def update_list_view(self, new_product_list):
        self.data = []
        self.data = new_product_list


class AcceptedCallsListView(RecycleView):
    def __init__(self, **kwargs):
        super(AcceptedCallsListView, self).__init__(**kwargs)
        self.data = []

    def update_list_view(self, new_product_list):
        self.data = []
        self.data = new_product_list


class ProductDropdown(BoxLayout):
    selected_product = None

    def __init__(self, **kwargs):
        super(ProductDropdown, self).__init__(**kwargs)
        self.app = App.get_running_app()

    def set_button_text(self, text):
        if self.ids.btn:
            # set the button text
            self.ids.btn.text = text
        return

    def select_program(self, text):

        # save the progam locally
        self.selected_product = text

        # set the button text
        self.set_button_text(text)

    def get_selected_program(self):
        return self.selected_product


if __name__ == "__main__":
    SwitchingScreenApp().run()