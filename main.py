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

from email_server import EmailServer

Builder.load_file("views/menu_screen/menu_screen.kv")
Builder.load_file("views/drinks_screen/drinks_screen.kv")
Builder.load_file("views/retail_screen/retail_screen.kv")
Builder.load_file("views/food_screen/food_screen.kv")
Builder.load_file("views/reciept_screen/reciept_screen.kv")
Builder.load_file("views/screen_six/screen_six.kv")
Builder.load_file("views/snacks_screen/snacks_screen.kv")
Builder.load_file("views/start_count_screen/start_count_screen.kv")
 
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class DrinksScreen(Screen):
    def __init__(self, **kwargs):
        super(DrinksScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


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


class SnacksScreen(Screen):
    def __init__(self, **kwargs):
        super(SnacksScreen, self).__init__(**kwargs)
        self.app = App.get_running_app()


class Start_Count_Screen(Screen):

    products_list = [
        'candy',
        'nesquick',
        'red bull',
        'gatorade',
        'monster',
        'brisk',
        'water',
        'soda',
        'arizona',
        'v8',
        'langers',
        'body armor',
        'star bucks',
        'raze',
        'bang',
        'electro life',
        'coconut water',
        '5 hour',
        'breakfast',
        'small burrito',
        'large burrito',
        'calzone',
        'big chicken',
        'pbj',
        'brats',
        'fresh and ready',
        'tuna',
        'parfait',
        'pastry',
        'chips',
        'el sabroso',
        'combos',
        'soups',
        'island snacks',
        'sun flower seeds',
        'pop tart',
        'takis',
        'fruit snacks',
        'gum',
        'gatorade bars',
        'ciggs',
        'grizzly',
        'stokers',
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
        
        # start of adding to the csv

        # start of adding to the csv

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

    def submit_to_csv(self):

        # loop thru list
        for product in self.selected_product_list:

            print(f'This is the product: \n{product}')

            text = product["text"]
            product_name, count = text.split("  -  ")
            self.app.root.product_store[product_name][3] = int(count)

        print(f'This is the Dictionary: \n{self.app.root.product_store}')


class MyScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.app = App.get_running_app()
        self.product_store = {}

        for product, price in list(PRICES.items()):
            # product_store = [ price, current, total, start ]
            self.product_store[product] = [price, 0, 0, 0]


        # create the email server object
        self.email_server = EmailServer()

        self.running_total = 0

        self.start_count_total = ""

    def get_data(self):
        totals = ['start count' , 'amount sold']

        # TODO - do some stuff


        self.write_to_file(totals)

        self.DIR_screen_selected()

        self.trigger_send_email()

    def write_to_file(self, data):
        col_names = ['Start_count' , 'Total_sold']
        
        # candy = [self.start_candy_total , self.candy_total]
        # pastry = [self.start_pastry_total , self.pastry_total]
        # chips = [self.start_chips_total , self.chips_total]
        # el_sabroso = [self.start_el_sabroso_total , self.el_sabroso_total]
        # combos = [self.start_combos_total , self.combos_total]
        # soups = self.start_soups_total , [self.soups_total]
        # island_snacks = self.start_island_snacks_total , [self.island_snacks_total]
        # sun_flower_seeds = [self.start_sun_flower_seeds_total , self.sun_flower_seeds_total]
        # pop_tarts = [self.start_pop_tarts_total , self.pop_tarts_total]
        # takis = [self.start_takis_total , self.takis_total]
        # fruit_snacks = [self.start_fruit_snacks_total , self.fruit_snacks_total]
        # fruit_cups = [self.start_fruit_cups_total , self.fruit_cups_total]
        # gum = [self.start_gum_total , self.gum_total]
        # gatorade_bar = [self.start_gatorade_bar_total , self.gatorade_bar_total]
        # breakfast = [self.start_breakfast_total , self.breakfast_total]
        # small_burrito = [self.start_small_burrito_total , self.small_burrito_total]
        # large_burrito = [self.start_large_burrito_total , self.large_burrito_total]
        # calzone = [self.start_calzone_total , self.calzone_total]
        # big_chicken = [self.start_big_chicken_total , self.big_chicken_total]
        # pbj = [self.start_pbj_total , self.pbj_total]
        # brats = [self.start_brats_total , self.brats_total]
        # fresh_and_ready = [self.start_fresh_and_ready_total , self.fresh_and_ready_total]
        # tuna = [self.start_tuna_total , self.tuna_total]
        # parfait = [self.start_parfait_total , self.parfait_total]
        # nesquick = [self.start_nesquick_total , self.nesquick_total]
        # red_bull = [self.start_red_bull_total , self.red_bull_total]
        # gatorade = [self.start_gatorade_total , self.gatorade_total]
        # monster = [self.start_monster_total , self.monster_total]
        # brisk = [self.start_brisk_total , self.brisk_total]
        # water = [self.start_water_total , self.water_total]
        # soda = [self.start_soda_total , self.soda_total]
        # arizona = [self.start_arizona_total , self.arizona_total]
        # v8 = [self.start_v8_total , self.v8_total]
        # langers = [self.start_langers_total , self.langers_total]
        # body_armor = [self.start_body_armor_total , self.body_armor_total]
        # star_bucks = [self.start_star_bucks_total , self.star_bucks_total]
        # raze = [self.start_raze_total , self.raze_total]
        # bang = [self.start_bang_total , self.bang_total]
        # electro_life = [self.start_electro_life_total , self.electro_life_total]
        # coconut_water = [self.start_coconut_water_total , self.coconut_water_total]
        # five_hour = [self.start_five_hour_total , self.five_hour_total]
        # ciggs = [self.start_ciggs_total , self.ciggs_total]
        # grizzly = [self.start_grizzly_total , self.grizzly_total]
        # stokers = [self.start_stokers_total , self.stokers_total]
        # lighters = [self.start_lighters_total , self.lighters_total]
        # chapstick = [self.start_chapstick_total , self.chapstick_total]
        
        # name of csv file 
        filename = "my_total_sales.csv"

        # writing to csv file 
        with open(filename, 'w') as csvfile:

            # creating a csv writer object 
            csvwriter = csv.writer(csvfile)

            print("Praoduct STroesd")
            print(self.product_store)
            print()

            # loop thru dictionary store
            for product in self.product_store.items():
                print(product)
                name, stuff = product

                print(stuff)
                to_row = list((name, stuff[2], stuff[3]))
                # writing the product info to csv
                csvwriter.writerow(to_row)

            # # writing the column names 
            # csvwriter.writerow(col_names)
            # csvwriter.writerow(candy)           
            # csvwriter.writerow(nesquick) 
            # csvwriter.writerow(red_bull) 
            # csvwriter.writerow(gatorade) 
            # csvwriter.writerow(monster) 
            # csvwriter.writerow(brisk) 
            # csvwriter.writerow(water) 
            # csvwriter.writerow(soda)
            # csvwriter.writerow(arizona )
            # csvwriter.writerow(v8  )
            # csvwriter.writerow(langers)
            # csvwriter.writerow(body_armor )
            # csvwriter.writerow(star_bucks )
            # csvwriter.writerow(raze )
            # csvwriter.writerow(bang )
            # csvwriter.writerow(electro_life )
            # csvwriter.writerow(coconut_water)
            # csvwriter.writerow(five_hour )
            # csvwriter.writerow(breakfast )
            # csvwriter.writerow(small_burrito ) 
            # csvwriter.writerow(large_burrito )
            # csvwriter.writerow(calzone )
            # csvwriter.writerow(big_chicken )
            # csvwriter.writerow(pbj )
            # csvwriter.writerow(brats)
            # csvwriter.writerow(fresh_and_ready)
            # csvwriter.writerow(tuna)
            # csvwriter.writerow(parfait)
            # csvwriter.writerow(pastry) 
            # csvwriter.writerow(chips )
            # csvwriter.writerow(el_sabroso)
            # csvwriter.writerow(combos)
            # csvwriter.writerow(soups) 
            # csvwriter.writerow(island_snacks)
            # csvwriter.writerow(sun_flower_seeds) 
            # csvwriter.writerow(pop_tarts) 
            # csvwriter.writerow(takis) 
            # csvwriter.writerow(fruit_snacks) 
            # csvwriter.writerow(fruit_cups) 
            # csvwriter.writerow(gum)
            # csvwriter.writerow(gatorade_bar)
            # csvwriter.writerow(ciggs )
            # csvwriter.writerow(grizzly ) 
            # csvwriter.writerow(stokers )
            # csvwriter.writerow(lighters )
            # csvwriter.writerow(chapstick ) 
    
    def add_to_item(self, product_name):
        # copy old data from store
        _, old_count, old_total, _ = self.product_store[product_name]

        self.product_store[product_name][1] += 1
        self.product_store[product_name][2] += 1
        self.running_total += self.product_store[product_name][0]

        # update the running total label for each page
        self.update_all_screen_totals()
        self.update_receipt_item(product_name)

    def update_receipt_item(self, product_name):
        product_count = self.product_store[product_name][1] 
        product_total = float(self.product_store[product_name][0]) * float(self.product_store[product_name][1]) 

        if product_name == 'candy':
            self.ids.reciept_screen.ids.candy_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'pastry':
            self.ids.reciept_screen.ids.pastry_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'chips':
            self.ids.reciept_screen.ids.chips_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'el sabroso':
            self.ids.reciept_screen.ids.el_sabroso_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'combos':
            self.ids.reciept_screen.ids.combos_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'soups':
            self.ids.reciept_screen.ids.soups_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'island snacks':
            self.ids.reciept_screen.ids.island_snacks_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'sun flower seeds':
            self.ids.reciept_screen.ids.sun_flower_seeds_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'pop tarts':
            self.ids.reciept_screen.ids.pop_tarts_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)
        
        elif product_name == 'takis':
            self.ids.reciept_screen.ids.takis_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'fruit snacks':
            self.ids.reciept_screen.ids.fruit_snacks_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'fruit cups':
            self.ids.reciept_screen.ids.fruit_cups_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)


        elif product_name == 'gum':
            self.ids.reciept_screen.ids.gum_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'gatorade bar':
            self.ids.reciept_screen.ids.gatorade_bar_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'nesquick':
            self.ids.reciept_screen.ids.nesquick_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'red bull':
            self.ids.reciept_screen.ids.red_bull_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'gatorade':
            self.ids.reciept_screen.ids.gatorade_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'monster':
            self.ids.reciept_screen.ids.monster_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'brisk':
            self.ids.reciept_screen.ids.brisk_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)


        elif product_name == 'water':
            self.ids.reciept_screen.ids.water_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'soda':
            self.ids.reciept_screen.ids.soda_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'arizona':
            self.ids.reciept_screen.ids.arizona_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'v8':
            self.ids.reciept_screen.ids.v8_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'langers':
            self.ids.reciept_screen.ids.langers_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'body armor':
            self.ids.reciept_screen.ids.body_armor_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'star bucks':
            self.ids.reciept_screen.ids.star_bucks_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'raze':
            self.ids.reciept_screen.ids.raze_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'bang':
            self.ids.reciept_screen.ids.bang_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'electro life':
            self.ids.reciept_screen.ids.electro_life_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'coconut water':
            self.ids.reciept_screen.ids.coconut_water_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == '5 hour':
            self.ids.reciept_screen.ids.five_hour_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'breakfast':
            self.ids.reciept_screen.ids.breakfast_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'small burrito':
            self.ids.reciept_screen.ids.small_burrito_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'large burrito':
            self.ids.reciept_screen.ids.large_burrito_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'calzone':
            self.ids.reciept_screen.ids.calzone_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'big chicken':
            self.ids.reciept_screen.ids.big_chicken_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'pbj':
            self.ids.reciept_screen.ids.pbj_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'brats':
            self.ids.reciept_screen.ids.brats_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'fresh & ready':
            self.ids.reciept_screen.ids.fresh_and_ready_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'tuna':
            self.ids.reciept_screen.ids.tuna_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'parfait':
            self.ids.reciept_screen.ids.parfait_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'ciggs':
            self.ids.reciept_screen.ids.ciggs_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'grizzly':
            self.ids.reciept_screen.ids.grizzly_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'stokers':
            self.ids.reciept_screen.ids.stokers_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'lighters':
            self.ids.reciept_screen.ids.lighters_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

        elif product_name == 'chapstick':
            self.ids.reciept_screen.ids.chapstick_count.text = f' {product_name}:\n ' + str(product_count) + ' = '+ str(product_total)

    def minus_to_item(self, product_name):
        # check: is the item count already 0
        if self.product_store[product_name][1] < 1:
            return

        # copy old data from store
        _, old_count, old_total, _ = self.product_store[product_name]

        self.product_store[product_name][1] -= 1
        self.product_store[product_name][2] -= 1
        self.running_total -= self.product_store[product_name][0]

        # update the running total label for each page
        self.update_all_screen_totals()
        self.update_receipt_item(product_name)
        print(f'Updated Item: \n{self.product_store[product_name]}')

    def add_to_total(self, button_name):
        self.running_total += PRICES[button_name.lower()]
        self.update_all_screen_totals()

    def snacks_screen_selected(self):
        self.app.root.switch_screen('_snacks_screen_')

    def switch_screen(self, screen_name):
        self.current = screen_name

    def drinks_screen_selected(self):
        self.app.root.switch_screen('_drinks_screen_')
    
    def reset_running_total(self):
        self.running_total = 0
        self.update_all_screen_totals()
        self.update_reciept_screen_counts()
    
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
    
    def trigger_send_email(self):
        try:
            print('-- Sending Email --\n')
            
            # single threading
            self.app.root.email_server.send_email()
            
            # TODO - multi-threading
            # threading.Thread(target=self.app.root.email_server.send_email).start()

            print(f'\nSuccess!!')
        except Exception as e:
            print(f'Error: \n{e}')
            return

    def update_all_screen_totals(self):
        self.ids.snacks_screen.ids.running_total.text = '$' + str(self.running_total)
        self.ids.drinks_screen.ids.running_total.text = '$ ' + str(self.running_total)
        self.ids.retail_screen.ids.running_total.text = '$ ' + str(self.running_total)
        self.ids.food_screen.ids.running_total.text = '$ ' + str(self.running_total)
        self.ids.reciept_screen.ids.running_total.text = '$ ' + str(self.running_total)
    
    def update_reciept_screen_counts(self):
        self.candy_count = 0
        self.pastry_count = 0
        self.chips_count = 0
        self.el_sabroso_count = 0
        self.combos_count = 0
        self.soups_count = 0
        self.island_snacks_count = 0
        self.sun_flower_seeds_count = 0
        self.pop_tarts_count = 0
        self.takis_count = 0
        self.fruit_snacks_count = 0
        self.fruit_cups_count = 0
        self.gum_count = 0
        self.gatorade_bar_count = 0
        self.nesquick_count = 0
        self.red_bull_count = 0
        self.gatorade_count = 0
        self.monster_count = 0
        self.brisk_count = 0
        self.water_count = 0
        self.soda_count = 0
        self.arizona_count = 0
        self.v8_count = 0
        self.langers_count = 0
        self.body_armor_count = 0
        self.star_bucks_count = 0
        self.raze_count = 0
        self.bang_count = 0
        self.electro_life_count = 0
        self.coconut_water_count = 0
        self.five_hour_count = 0
        self.breakfast_count = 0
        self.small_burrito_count = 0
        self.large_burrito_count = 0
        self.calzone_count = 0
        self.big_chicken_count = 0
        self.pbj_count = 0
        self.brats_count = 0
        self.fresh_and_ready_count = 0
        self.tuna_count = 0
        self.parfait_count = 0
        self.ciggs_count = 0
        self.grizzly_count = 0
        self.stokers_count = 0
        self.lighters_count = 0
        self.chapstick_count = 0   
        self.ids.reciept_screen.ids.candy_count.text = ''
        self.ids.reciept_screen.ids.pastry_count.text = ' '
        self.ids.reciept_screen.ids.chips_count.text = ' ' 
        self.ids.reciept_screen.ids.el_sabroso_count.text = ' ' 
        self.ids.reciept_screen.ids.combos_count.text = ' '
        self.ids.reciept_screen.ids.soups_count.text = ' ' 
        self.ids.reciept_screen.ids.island_snacks_count.text = ' ' 
        self.ids.reciept_screen.ids.sun_flower_seeds_count.text = ''
        self.ids.reciept_screen.ids.pop_tarts_count.text = ' '
        self.ids.reciept_screen.ids.takis_count.text = ' ' 
        self.ids.reciept_screen.ids.fruit_snacks_count.text = ' ' 
        self.ids.reciept_screen.ids.fruit_cups_count.text = ' ' 
        self.ids.reciept_screen.ids.gum_count.text = ' '
        self.ids.reciept_screen.ids.gatorade_bar_count.text = ' ' 
        self.ids.reciept_screen.ids.nesquick_count.text = ' '
        self.ids.reciept_screen.ids.red_bull_count.text = ''
        self.ids.reciept_screen.ids.gatorade_count.text = ' '
        self.ids.reciept_screen.ids.monster_count.text = ' ' 
        self.ids.reciept_screen.ids.brisk_count.text = ' ' 
        self.ids.reciept_screen.ids.water_count.text = ' '
        self.ids.reciept_screen.ids.soda_count.text = ' ' 
        self.ids.reciept_screen.ids.arizona_count.text = ' '
        self.ids.reciept_screen.ids.v8_count.text = ''
        self.ids.reciept_screen.ids.langers_count.text = ' '
        self.ids.reciept_screen.ids.body_armor_count.text = ' ' 
        self.ids.reciept_screen.ids.star_bucks_count.text = ' '
        self.ids.reciept_screen.ids.raze_count.text = ' ' 
        self.ids.reciept_screen.ids.bang_count.text = ' '
        self.ids.reciept_screen.ids.electro_life_count.text = ' ' 
        self.ids.reciept_screen.ids.coconut_water_count.text = ' ' 
        self.ids.reciept_screen.ids.five_hour_count.text = ''
        self.ids.reciept_screen.ids.breakfast_count.text = ' '
        self.ids.reciept_screen.ids.small_burrito_count.text = ' ' 
        self.ids.reciept_screen.ids.large_burrito_count.text = ' ' 
        self.ids.reciept_screen.ids.calzone_count.text = ' '
        self.ids.reciept_screen.ids.big_chicken_count.text = ' ' 
        self.ids.reciept_screen.ids.pbj_count.text = ' '
        self.ids.reciept_screen.ids.brats_count.text = ''
        self.ids.reciept_screen.ids.fresh_and_ready_count.text = ' '
        self.ids.reciept_screen.ids.tuna_count.text = ' ' 
        self.ids.reciept_screen.ids.parfait_count.text = ' ' 
        self.ids.reciept_screen.ids.ciggs_count.text = ' '
        self.ids.reciept_screen.ids.grizzly_count.text = ' ' 
        self.ids.reciept_screen.ids.stokers_count.text = ' '
        self.ids.reciept_screen.ids.lighters_count.text = ' ' 
        self.ids.reciept_screen.ids.chapstick_count.text = ' '
    

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