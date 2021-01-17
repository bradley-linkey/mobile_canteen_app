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


class MyScreenManager(ScreenManager):

    def __init__(self, **kwargs):
        super(MyScreenManager, self).__init__(**kwargs)
        self.app = App.get_running_app()

        # create the email server object
        self.email_server = EmailServer()

        self.running_total = 0
        
        # TODO - print these values into csv
        
        self.candy_total = 0
        self.pastry_total = 0
        self.chips_total = 0
        self.el_sabroso_total = 0
        self.combos_total = 0
        self.soups_total = 0
        self.island_snacks_total = 0
        self.sun_flower_seeds_total = 0
        self.pop_tarts_total = 0
        self.takis_total = 0
        self.fruit_snacks_total = 0
        self.fruit_cups_total = 0
        self.gum_total = 0
        self.gatorade_bar_total = 0
        self.nesquick_total = 0
        self.red_bull_total = 0
        self.gatorade_total = 0
        self.monster_total = 0
        self.brisk_total = 0
        self.water_total = 0
        self.soda_total = 0
        self.arizona_total = 0
        self.v8_total = 0
        self.langers_total = 0
        self.body_armor_total = 0
        self.star_bucks_total = 0
        self.raze_total = 0
        self.bang_total = 0
        self.electro_life_total = 0
        self.coconut_water_total = 0
        self.five_hour_total = 0
        self.breakfast_total = 0
        self.small_burrito_total = 0
        self.large_burrito_total = 0
        self.calzone_total = 0
        self.big_chicken_total = 0
        self.pbj_total = 0
        self.brats_total = 0
        self.fresh_and_ready_total = 0
        self.tuna_total = 0
        self.parfait_total = 0
        self.ciggs_total = 0
        self.grizzly_total = 0
        self.stokers_total = 0
        self.lighters_total = 0
        self.chapstick_total = 0
        # 
        # 

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

        self.start_candy_total = 0
        self.start_pastry_total = 0
        self.start_chips_total = 0
        self.start_el_sabroso_total = 0
        self.start_combos_total = 0
        self.start_soups_total = 0
        self.start_island_snacks_total = 0
        self.start_sun_flower_seeds_total = 0
        self.start_pop_tarts_total = 0
        self.start_takis_total = 0
        self.start_fruit_snacks_total = 0
        self.start_fruit_cups_total = 0
        self.start_gum_total = 0
        self.start_gatorade_bar_total = 0
        self.start_nesquick_total = 0
        self.start_red_bull_total = 0
        self.start_gatorade_total = 0
        self.start_monster_total = 0
        self.start_brisk_total = 0
        self.start_water_total = 0
        self.start_soda_total = 0
        self.start_arizona_total = 0
        self.start_v8_total = 0
        self.start_langers_total = 0
        self.start_body_armor_total = 0
        self.start_star_bucks_total = 0
        self.start_raze_total = 0
        self.start_bang_total = 0
        self.start_electro_life_total = 0
        self.start_coconut_water_total = 0
        self.start_five_hour_total = 0
        self.start_breakfast_total = 0
        self.start_small_burrito_total = 0
        self.start_large_burrito_total = 0
        self.start_calzone_total = 0
        self.start_big_chicken_total = 0
        self.start_pbj_total = 0
        self.start_brats_total = 0
        self.start_fresh_and_ready_total = 0
        self.start_tuna_total = 0
        self.start_parfait_total = 0
        self.start_ciggs_total = 0
        self.start_grizzly_total = 0
        self.start_stokers_total = 0 
        self.start_lighters_total = 0
        self.start_chapstick_total = 0

        self.start_count_total = ""

    def get_data(self):
        totals = ['start count' , 'amount sold']

        # TODO - do some stuff


        self.write_to_file(totals)

        self.DIR_screen_selected()

        self.trigger_send_email()

    def write_to_file(self, data):
        col_names = ['Start_count' , 'Total_sold']
        candy = [self.start_candy_total , self.candy_total]
        pastry = [self.start_pastry_total , self.pastry_total]
        chips = [self.start_chips_total , self.chips_total]
        el_sabroso = [self.start_el_sabroso_total , self.el_sabroso_total]
        combos = [self.start_combos_total , self.combos_total]
        soups = self.start_soups_total , [self.soups_total]
        island_snacks = self.start_island_snacks_total , [self.island_snacks_total]
        sun_flower_seeds = [self.start_sun_flower_seeds_total , self.sun_flower_seeds_total]
        pop_tarts = [self.start_pop_tarts_total , self.pop_tarts_total]
        takis = [self.start_takis_total , self.takis_total]
        fruit_snacks = [self.start_fruit_snacks_total , self.fruit_snacks_total]
        fruit_cups = [self.start_fruit_cups_total , self.fruit_cups_total]
        gum = [self.start_gum_total , self.gum_total]
        gatorade_bar = [self.start_gatorade_bar_total , self.gatorade_bar_total]
        breakfast = [self.start_breakfast_total , self.breakfast_total]
        small_burrito = [self.start_small_burrito_total , self.small_burrito_total]
        large_burrito = [self.start_large_burrito_total , self.large_burrito_total]
        calzone = [self.start_calzone_total , self.calzone_total]
        big_chicken = [self.start_big_chicken_total , self.big_chicken_total]
        pbj = [self.start_pbj_total , self.pbj_total]
        brats = [self.start_brats_total , self.brats_total]
        fresh_and_ready = [self.start_fresh_and_ready_total , self.fresh_and_ready_total]
        tuna = [self.start_tuna_total , self.tuna_total]
        parfait = [self.start_parfait_total , self.parfait_total]
        nesquick = [self.start_nesquick_total , self.nesquick_total]
        red_bull = [self.start_red_bull_total , self.red_bull_total]
        gatorade = [self.start_gatorade_total , self.gatorade_total]
        monster = [self.start_monster_total , self.monster_total]
        brisk = [self.start_brisk_total , self.brisk_total]
        water = [self.start_water_total , self.water_total]
        soda = [self.start_soda_total , self.soda_total]
        arizona = [self.start_arizona_total , self.arizona_total]
        v8 = [self.start_v8_total , self.v8_total]
        langers = [self.start_langers_total , self.langers_total]
        body_armor = [self.start_body_armor_total , self.body_armor_total]
        star_bucks = [self.start_star_bucks_total , self.star_bucks_total]
        raze = [self.start_raze_total , self.raze_total]
        bang = [self.start_bang_total , self.bang_total]
        electro_life = [self.start_electro_life_total , self.electro_life_total]
        coconut_water = [self.start_coconut_water_total , self.coconut_water_total]
        five_hour = [self.start_five_hour_total , self.five_hour_total]
        ciggs = [self.start_ciggs_total , self.ciggs_total]
        grizzly = [self.start_grizzly_total , self.grizzly_total]
        stokers = [self.start_stokers_total , self.stokers_total]
        lighters = [self.start_lighters_total , self.lighters_total]
        chapstick = [self.start_chapstick_total , self.chapstick_total]
        
        # name of csv file 
        filename = "my_total_sales.csv"

        # writing to csv file 
        with open(filename, 'w') as csvfile: 
            # creating a csv writer object 
            csvwriter = csv.writer(csvfile)

            # writing the column names 
            csvwriter.writerow(col_names)
            csvwriter.writerow(candy)           
            csvwriter.writerow(nesquick) 
            csvwriter.writerow(red_bull) 
            csvwriter.writerow(gatorade) 
            csvwriter.writerow(monster) 
            csvwriter.writerow(brisk) 
            csvwriter.writerow(water) 
            csvwriter.writerow(soda)
            csvwriter.writerow(arizona )
            csvwriter.writerow(v8  )
            csvwriter.writerow(langers)
            csvwriter.writerow(body_armor )
            csvwriter.writerow(star_bucks )
            csvwriter.writerow(raze )
            csvwriter.writerow(bang )
            csvwriter.writerow(electro_life )
            csvwriter.writerow(coconut_water)
            csvwriter.writerow(five_hour )
            csvwriter.writerow(breakfast )
            csvwriter.writerow(small_burrito ) 
            csvwriter.writerow(large_burrito )
            csvwriter.writerow(calzone )
            csvwriter.writerow(big_chicken )
            csvwriter.writerow(pbj )
            csvwriter.writerow(brats)
            csvwriter.writerow(fresh_and_ready)
            csvwriter.writerow(tuna)
            csvwriter.writerow(parfait)
            csvwriter.writerow(pastry) 
            csvwriter.writerow(chips )
            csvwriter.writerow(el_sabroso)
            csvwriter.writerow(combos)
            csvwriter.writerow(soups) 
            csvwriter.writerow(island_snacks)
            csvwriter.writerow(sun_flower_seeds) 
            csvwriter.writerow(pop_tarts) 
            csvwriter.writerow(takis) 
            csvwriter.writerow(fruit_snacks) 
            csvwriter.writerow(fruit_cups) 
            csvwriter.writerow(gum)
            csvwriter.writerow(gatorade_bar)
            csvwriter.writerow(ciggs )
            csvwriter.writerow(grizzly ) 
            csvwriter.writerow(stokers )
            csvwriter.writerow(lighters )
            csvwriter.writerow(chapstick ) 
    
    def add_to_button(self, button):
        if button.name == 'candy':
            if self.inventory['candy']:
                old_row = self.inventory['candy']
            else:
                old_row = [0, 0, 0]
            old_row[1] = old_row[1]+1
            self.inventory['candy'] = old_row[0]+1, old_row[1], old_row[1]*PRICES['candy']

            # self.candy_total += 1
            # self.candy_count += 1
            # self.candy_product = (self.candy_count * 2.5 )

            # self.ids.reciept_screen.ids.candy_count.text = ' candy: ' + str(self.candy_count) + ' = '+ str(self.candy_product)
            self.ids.reciept_screen.ids.candy_count.text = ' candy: ' + str(self.inventory['candy'][1]) + ' = '+ str(self.inventory['candy'][2])

    def minus_to_button(self, button):
        if button.text == ' ':
            return
        
        if button.name == 'candy':
            # copy old row
            old_row = self.inventory['candy']

            # update the values
            new_row = old_row[0] -1, old_row[1]-1, old_row[2]-PRICES['candy']
            
            # save to dictionary
            self.inventory['candy'] = new_row 

            # self.candy_total -= 1
            # self.candy_count -= 1
            # self.candy_product -= 2.5

            # change global running total
            self.running_total -= 2.5

            # update button text
            button.text = ' candy: ' + str(self.candy_count) + ' = '+ str(self.candy_product)
            if self.candy_count < 1:
                button.text = ' '
        self.update_all_screen_totals()

    def add_to_candy(self, button_name):
        self.candy_total += 1
        self.candy_count += 1
        self.candy_product = (self.candy_count * 2.5 )
        self.ids.reciept_screen.ids.candy_count.text = ' candy:\n ' + str(self.candy_count) + ' = '+ str(self.candy_product)
    
    def minus_to_candy(self, button_name):
        if self.candy_count == 0 :
            self.ids.reciept_screen.ids.candy_count.text = ' '
        elif self.candy_count != 0:
            self.candy_total -= 1
            self.candy_count -= 1
            self.candy_product -= 2.5
            self.running_total -= 2.5 
            self.ids.reciept_screen.ids.candy_count.text = ' candy:\n' + str(self.candy_count) + ' = '+ str(self.candy_product)
            self.update_all_screen_totals()

    def add_to_pastry(self, button_name):
        self.pastry_total += 1
        self.pastry_count += 1
        self.pastry_product = (self.pastry_count * 1.5 )
        self.ids.reciept_screen.ids.pastry_count.text = ' pastry: \n' + str(self.pastry_count) + ' = '+ str(self.pastry_product)

    def minus_to_pastry(self, button_name):
        if self.pastry_count == 0 :
            self.ids.reciept_screen.ids.pastry_count.text = ' '
        elif self.pastry_count != 0:
            self.pastry_total -= 1
            self.pastry_count -= 1
            self.pastry_product -= 1.5
            self.running_total -= 1.5 
            self.ids.reciept_screen.ids.pastry_count.text = ' pastry: \n' + str(self.pastry_count) + ' = '+ str(self.pastry_product)
            self.update_all_screen_totals()

    def add_to_chips(self, button_name):
        self.chips_total += 1
        self.chips_count += 1
        self.chips_product = (self.chips_count * 2.00 )
        self.ids.reciept_screen.ids.chips_count.text = ' chips:\n ' + str(self.chips_count) + ' = '+ str(self.chips_product)

    def minus_to_chips(self, button_name):
        if self.chips_count == 0 :
            self.ids.reciept_screen.ids.chips_count.text = ' '
        elif self.chips_count != 0:
            self.chips_total -= 1
            self.chips_count -= 1
            self.chips_product -= 2
            self.running_total -= 2 
            self.ids.reciept_screen.ids.chips_count.text = ' chips: \n' + str(self.chips_count) + ' = '+ str(self.chips_product)
            self.update_all_screen_totals()

    def add_to_el_sabroso(self, button_name):
        self.el_sabroso_total += 1
        self.el_sabroso_count += 1
        self.el_sabroso_product = (self.el_sabroso_count * 2.0 )
        self.ids.reciept_screen.ids.el_sabroso_count.text = ' el sabroso: \n' + str(self.el_sabroso_count) + ' = '+ str(self.el_sabroso_product)
    
    def minus_to_el_sabroso(self, button_name):
        if self.el_sabroso_count == 0 :
            self.ids.reciept_screen.ids.el_sabroso_count.text = ' '
        elif self.el_sabroso_count != 0:
            self.el_sabroso_total -= 1
            self.el_sabroso_count -= 1
            self.el_sabroso_product -= 2
            self.running_total -= 2 
            self.ids.reciept_screen.ids.el_sabroso_count.text = ' elsabroso: \n' + str(self.el_sabroso_count) + ' = '+ str(self.el_sabroso_product)
            self.update_all_screen_totals()    

    def add_to_combos(self, button_name):
        self.combos_total += 1
        self.combos_count += 1
        self.combos_product = (self.combos_count * 3 )
        self.ids.reciept_screen.ids.combos_count.text = ' combos:\n ' + str(self.combos_count) + ' = '+ str(self.combos_product)

    def minus_to_combos(self, button_name):
        if self.combos_count == 0 :
            self.ids.reciept_screen.ids.combos_count.text = ' '
        elif self.combos_count != 0:
            self.combos_total -= 1
            self.combos_count -= 1
            self.combos_product -= 3
            self.running_total -= 3 
            self.ids.reciept_screen.ids.combos_count.text = ' combos: \n' + str(self.combos_count) + ' = '+ str(self.combos_product)
            self.update_all_screen_totals()

    def add_to_soups(self, button_name):
        self.soups_total += 1
        self.soups_count += 1
        self.soups_product = (self.soups_count * 2 )
        self.ids.reciept_screen.ids.soups_count.text = ' soups: \n' + str(self.soups_count) + ' = '+ str(self.soups_product)

    def minus_to_soups(self, button_name):
        if self.soups_count == 0 :
            self.ids.reciept_screen.ids.soups_count.text = ' '
        elif self.soups_count != 0:
            self.soups_total -= 1
            self.soups_count -= 1
            self.soups_product -= 2
            self.running_total -= 2 
            self.ids.reciept_screen.ids.soups_count.text = ' soups: \n' + str(self.soups_count) + ' = '+ str(self.soups_product)
            self.update_all_screen_totals()

    def add_to_island_snacks(self, button_name):
        self.island_snacks_total += 1
        self.island_snacks_count += 1
        self.island_snacks_product = (self.island_snacks_count * 3 )
        self.ids.reciept_screen.ids.island_snacks_count.text = ' I snacks: \n' + str(self.island_snacks_count) + ' = '+ str(self.island_snacks_product)

    def minus_to_island_snacks(self, button_name):
        if self.island_snacks_count == 0 :
            self.ids.reciept_screen.ids.island_snacks_count.text = ' '
        elif self.island_snacks_count != 0:
            self.island_snacks_total -= 1
            self.island_snacks_count -= 1
            self.island_snacks_product -= 3
            self.running_total -= 3 
            self.ids.reciept_screen.ids.island_snacks_count.text = ' I snacks: \n' + str(self.island_snacks_count) + ' = '+ str(self.island_snacks_product)
            self.update_all_screen_totals()

    def add_to_sun_flower_seeds(self, button_name):
        self.sun_flower_seeds_total += 1
        self.sun_flower_seeds_count += 1
        self.sun_flower_seeds_product = (self.sun_flower_seeds_count * 2.25 )
        self.ids.reciept_screen.ids.sun_flower_seeds_count.text = 'seeds: \n' + str(self.sun_flower_seeds_count) + ' = '+ str(self.sun_flower_seeds_product)

    def minus_to_sun_flower_seeds(self, button_name):
        if self.sun_flower_seeds_count == 0 :
            self.ids.reciept_screen.ids.sun_flower_seeds_count.text = ' '
        elif self.sun_flower_seeds_count != 0:
            self.sun_flower_seeds_total -= 1
            self.sun_flower_seeds_count -= 1
            self.sun_flower_seeds_product -= 2.25
            self.running_total -= 2.25
            self.ids.reciept_screen.ids.sun_flower_seeds_count.text = ' seeds: \n' + str(self.sun_flower_seeds_count) + ' = '+ str(self.sun_flower_seeds_product)
            self.update_all_screen_totals()

    def add_to_pop_tarts(self, button_name):
        self.pop_tarts_total += 1
        self.pop_tarts_count += 1
        self.pop_tarts_product = (self.pop_tarts_count * 1.5 )
        self.ids.reciept_screen.ids.pop_tarts_count.text = ' poptarts: \n' + str(self.pop_tarts_count) + ' = '+ str(self.pop_tarts_product)

    def minus_to_pop_tarts(self, button_name):
        if self.pop_tarts_count == 0 :
            self.ids.reciept_screen.ids.pop_tarts_count.text = ' '
        elif self.pop_tarts_count != 0:
            self.pop_tarts_total -= 1
            self.pop_tarts_count -= 1
            self.pop_tarts_product -= 1.5
            self.running_total -= 1.5 
            self.ids.reciept_screen.ids.pop_tarts_count.text = ' poptarts: \n' + str(self.pop_tarts_count) + ' = '+ str(self.pop_tarts_product)
            self.update_all_screen_totals()
    
    def add_to_takis(self, button_name):
        self.takis_total += 1
        self.takis_count += 1
        self.takis_product = (self.takis_count * 2.25 )
        self.ids.reciept_screen.ids.takis_count.text = 'takis: \n' + str(self.takis_count) + ' = '+ str(self.takis_product)
    
    def minus_to_takis(self, button_name):
        if self.takis_count == 0 :
            self.ids.reciept_screen.ids.takis_count.text = ' '
        elif self.takis_count != 0:
            self.takis_total -= 1
            self.takis_count -= 1
            self.takis_product -= 2.25
            self.running_total -= 2.25
            self.ids.reciept_screen.ids.takis_count.text = ' takis: \n' + str(self.takis_count) + ' = '+ str(self.takis_product)
            self.update_all_screen_totals()

    def add_to_fruit_snacks(self, button_name):
        self.fruit_snacks_total += 1
        self.fruit_snacks_count += 1
        self.fruit_snacks_product = (self.fruit_snacks_count * 1.25 )
        self.ids.reciept_screen.ids.fruit_snacks_count.text = ' frt snacks: \n' + str(self.fruit_snacks_count) + ' = '+ str(self.fruit_snacks_product)    
    
    def minus_to_fruit_snacks(self, button_name):
        if self.fruit_snacks_count == 0 :
            self.ids.reciept_screen.ids.fruit_snacks_count.text = ' '
        elif self.fruit_snacks_count != 0:
            self.fruit_snacks_total -= 1
            self.fruit_snacks_count -= 1
            self.fruit_snacks_product -= 1.25
            self.running_total -= 1.25 
            self.ids.reciept_screen.ids.fruit_snacks_count.text = ' frt snacks: \n' + str(self.fruit_snacks_count) + ' = '+ str(self.fruit_snacks_product)
            self.update_all_screen_totals()

    def add_to_fruit_cups(self, button_name):
        self.fruit_cups_total += 1
        self.fruit_cups_count += 1
        self.fruit_cups_product = (self.fruit_cups_count * 2.5 )
        self.ids.reciept_screen.ids.fruit_cups_count.text = ' frt cups: \n' + str(self.fruit_cups_count) + ' = '+ str(self.fruit_cups_product)    
    
    def minus_to_fruit_cups(self, button_name):
        if self.fruit_cups_count == 0 :
            self.ids.reciept_screen.ids.fruit_cups_count.text = ' '
        elif self.fruit_cups_count != 0:
            self.fruit_cups_total -= 1
            self.fruit_cups_count -= 1
            self.fruit_cups_product -= 2.5
            self.running_total -= 2.5
            self.ids.reciept_screen.ids.fruit_cups_count.text = ' frt cups: \n' + str(self.fruit_cups_count) + ' = '+ str(self.fruit_cups_product)
            self.update_all_screen_totals()

    def add_to_gum(self, button_name):
        self.gum_total += 1
        self.gum_count += 1
        self.gum_product = (self.gum_count * 1.25 )
        self.ids.reciept_screen.ids.gum_count.text = ' gum: \n' + str(self.gum_count) + ' = '+ str(self.gum_product)

    def minus_to_gum(self, button_name):
        if self.gum_count == 0 :
            self.ids.reciept_screen.ids.gum_count.text = ' '
        elif self.gum_count != 0:
            self.gum_total -= 1
            self.gum_count -= 1
            self.gum_product -= 1.25
            self.running_total -= 1.25 
            self.ids.reciept_screen.ids.gum_count.text = ' gum: \n' + str(self.gum_count) + ' = '+ str(self.gum_product)
            self.update_all_screen_totals()

    def add_to_gatorade_bar(self, button_name):
        self.gatorade_bar_total += 1
        self.gatorade_bar_count += 1
        self.gatorade_bar_product = (self.gatorade_bar_count * 3 )
        self.ids.reciept_screen.ids.gatorade_bar_count.text = ' g bar: \n' + str(self.gatorade_bar_count) + ' = '+ str(self.gatorade_bar_product)
    
    def minus_to_gatorade_bar(self, button_name):
        if self.gatorade_bar_count == 0 :
            self.ids.reciept_screen.ids.gatorade_bar_count.text = ' '
        elif self.gatorade_bar_count != 0:
            self.gatorade_bar_total -= 1
            self.gatorade_bar_count -= 1
            self.gatorade_bar_product -= 3
            self.running_total -= 3 
            self.ids.reciept_screen.ids.gatorade_bar_count.text = ' g bar: \n' + str(self.gatorade_bar_count) + ' = '+ str(self.gatorade_bar_product)
            self.update_all_screen_totals()

    def add_to_nesquick(self, button_name):
        self.nesquick_total += 1
        self.nesquick_count += 1
        self.nesquick_product = (self.nesquick_count * 3 )
        self.ids.reciept_screen.ids.nesquick_count.text = ' nesquick: \n' + str(self.nesquick_count) + ' = '+ str(self.nesquick_product)

    def minus_to_nesquick(self, button_name):
        if self.nesquick_count == 0 :
            self.ids.reciept_screen.ids.nesquick_count.text = ' '
        elif self.nesquick_count != 0:
            self.nesquick_total -= 1
            self.nesquick_count -= 1
            self.nesquick_product -= 3
            self.running_total -= 3 
            self.ids.reciept_screen.ids.nesquick_count.text = ' nesquick: \n' + str(self.nesquick_count) + ' = '+ str(self.nesquick_product)
            self.update_all_screen_totals()

    def add_to_red_bull(self, button_name):
        self.red_bull_total += 1
        self.red_bull_count += 1
        self.red_bull_product = (self.red_bull_count * 4.75 )
        self.ids.reciept_screen.ids.red_bull_count.text = ' red bull: \n' + str(self.red_bull_count) + ' = '+ str(self.red_bull_product)

    def minus_to_red_bull(self, button_name):
        if self.red_bull_count == 0 :
            self.ids.reciept_screen.ids.red_bull_count.text = ' '
        elif self.red_bull_count != 0:
            self.red_bull_total -= 1
            self.red_bull_count -= 1
            self.red_bull_product -= 4.75
            self.running_total -= 4.75 
            self.ids.reciept_screen.ids.red_bull_count.text = ' red bull: \n' + str(self.red_bull_count) + ' = '+ str(self.red_bull_product)
            self.update_all_screen_totals()

    def add_to_gatorade(self, button_name):
        self.gatorade_total += 1
        self.gatorade_count += 1
        self.gatorade_product = (self.gatorade_count * 3 )
        self.ids.reciept_screen.ids.gatorade_count.text = ' gatorade: \n' + str(self.gatorade_count) + ' = '+ str(self.gatorade_product)

    def minus_to_gatorade(self, button_name):
        if self.gatorade_count == 0 :
            self.ids.reciept_screen.ids.gatorade_count.text = ' '
        elif self.gatorade_count != 0:
            self.gatorade_total -= 1
            self.gatorade_count -= 1
            self.gatorade_product -= 3
            self.running_total -= 3 
            self.ids.reciept_screen.ids.gatorade_count.text = ' gatorade: \n' + str(self.gatorade_count) + ' = '+ str(self.gatorade_product)
            self.update_all_screen_totals()

    def add_to_monster(self, button_name):
        self.monster_total += 1
        self.monster_count += 1
        self.monster_product = (self.monster_count * 4 )
        self.ids.reciept_screen.ids.monster_count.text = ' monster: \n' + str(self.monster_count) + ' = '+ str(self.monster_product)

    def minus_to_monster(self, button_name):
        if self.monster_count == 0 :
            self.ids.reciept_screen.ids.monster_count.text = ' '
        elif self.monster_count != 0:
            self.monster_total -= 1
            self.monster_count -= 1
            self.monster_product -= 4
            self.running_total -= 4 
            self.ids.reciept_screen.ids.monster_count.text = ' monster: \n' + str(self.monster_count) + ' = '+ str(self.monster_product)
            self.update_all_screen_totals()

    def add_to_brisk(self, button_name):
        self.brisk_total += 1
        self.brisk_count += 1
        self.brisk_product = (self.brisk_count * 2.5 )
        self.ids.reciept_screen.ids.brisk_count.text = ' brisk: \n' + str(self.brisk_count) + ' = '+ str(self.brisk_product)
    
    def minus_to_brisk(self, button_name):
        if self.brisk_count == 0 :
            self.ids.reciept_screen.ids.brisk_count.text = ' '
        elif self.brisk_count != 0:
            self.brisk_total -= 1
            self.brisk_count -= 1
            self.brisk_product -= 2.5
            self.running_total -= 2.5 
            self.ids.reciept_screen.ids.brisk_count.text = ' brisk: \n' + str(self.brisk_count) + ' = '+ str(self.brisk_product)
            self.update_all_screen_totals()

    def add_to_water(self, button_name):
        self.water_total += 1
        self.water_count += 1
        self.water_product = (self.water_count * 2.25 )
        self.ids.reciept_screen.ids.water_count.text = ' water: \n' + str(self.water_count) + ' = '+ str(self.water_product)

    def minus_to_water(self, button_name):
        if self.water_count == 0 :
            self.ids.reciept_screen.ids.water_count.text = ' '
        elif self.water_count != 0:
            self.water_total -= 1
            self.water_count -= 1
            self.water_product -= 2.25
            self.running_total -= 2.25 
            self.ids.reciept_screen.ids.water_count.text = ' water: \n' + str(self.water_count) + ' = '+ str(self.water_product)
            self.update_all_screen_totals()

    def add_to_soda(self, button_name):
        self.soda_total += 1
        self.soda_count += 1
        self.soda_product = (self.soda_count * 2 )
        self.ids.reciept_screen.ids.soda_count.text = ' soda: \n' + str(self.soda_count) + ' = '+ str(self.soda_product)

    def minus_to_soda(self, button_name):
        if self.soda_count == 0 :
            self.ids.reciept_screen.ids.soda_count.text = ' '
        elif self.soda_count != 0:
            self.soda_total -= 1
            self.soda_count -= 1
            self.soda_product -= 2
            self.running_total -= 2 
            self.ids.reciept_screen.ids.soda_count.text = ' soda: \n' + str(self.soda_count) + ' = '+ str(self.soda_product)
            self.update_all_screen_totals()

    def add_to_arizona(self, button_name):
        self.arizona_total += 1
        self.arizona_count += 1
        self.arizona_product = (self.arizona_count * 1.25 )
        self.ids.reciept_screen.ids.arizona_count.text = ' AZ Tea: \n' + str(self.arizona_count) + ' = '+ str(self.arizona_product)

    def minus_to_arizona(self, button_name):
        if self.arizona_count == 0 :
            self.ids.reciept_screen.ids.arizona_count.text = ' '
        elif self.arizona_count != 0:
            self.arizona_total -= 1
            self.arizona_count -= 1
            self.arizona_product -= 1.25
            self.running_total -= 1.25 
            self.ids.reciept_screen.ids.arizona_count.text = ' AZ Tea: \n' + str(self.arizona_count) + ' = '+ str(self.arizona_product)
            self.update_all_screen_totals()

    def add_to_v8(self, button_name):
        self.v8_total += 1
        self.v8_count += 1
        self.v8_product = (self.v8_count * 2.25 )
        self.ids.reciept_screen.ids.v8_count.text = ' v8: \n' + str(self.v8_count) + ' = '+ str(self.v8_product)

    def minus_to_v8(self, button_name):
        if self.v8_count == 0 :
            self.ids.reciept_screen.ids.v8_count.text = ' '
        elif self.v8_count != 0:
            self.v8_total -= 1
            self.v8_count -= 1
            self.v8_product -= 2.25
            self.running_total -= 2.25 
            self.ids.reciept_screen.ids.v8_count.text = ' v8: \n' + str(self.v8_count) + ' = '+ str(self.v8_product)
            self.update_all_screen_totals()

    def add_to_langers(self, button_name):
        self.langers_total += 1
        self.langers_count += 1
        self.langers_product = (self.langers_count * 2 )
        self.ids.reciept_screen.ids.langers_count.text = ' langers: \n' + str(self.langers_count) + ' = '+ str(self.langers_product)

    def minus_to_langers(self, button_name):
        if self.langers_count == 0 :
            self.ids.reciept_screen.ids.langers_count.text = ' '
        elif self.langers_count != 0:
            self.langers_total -= 1
            self.langers_count -= 1
            self.langers_product -= 2
            self.running_total -= 2 
            self.ids.reciept_screen.ids.langers_count.text = ' langers: \n' + str(self.langers_count) + ' = '+ str(self.langers_product)
            self.update_all_screen_totals()

    def add_to_body_armor(self, button_name):
        self.body_armor_total += 1
        self.body_armor_count += 1
        self.body_armor_product = (self.body_armor_count * 3 )
        self.ids.reciept_screen.ids.body_armor_count.text = 'armor: \n' + str(self.body_armor_count) + ' = '+ str(self.body_armor_product)
    
    def minus_to_body_armor(self, button_name):
        if self.body_armor_count == 0 :
            self.ids.reciept_screen.ids.body_armor_count.text = ' '
        elif self.body_armor_count != 0:
            self.body_armor_total -= 1
            self.body_armor_count -= 1
            self.body_armor_product -= 3
            self.running_total -= 3 
            self.ids.reciept_screen.ids.body_armor_count.text = ' armor ' + str(self.body_armor_count) + ' = '+ str(self.body_armor_product)
            self.update_all_screen_totals()

    def add_to_star_bucks(self, button_name):
        self.star_bucks_total += 1
        self.star_bucks_count += 1
        self.star_bucks_product = (self.star_bucks_count * 4.75 )
        self.ids.reciept_screen.ids.star_bucks_count.text = ' s bucks: \n' + str(self.star_bucks_count) + ' = '+ str(self.star_bucks_product)

    def minus_to_star_bucks(self, button_name):
        if self.star_bucks_count == 0 :
            self.ids.reciept_screen.ids.star_bucks_count.text = ' '
        elif self.star_bucks_count != 0:
            self.star_bucks_total -= 1
            self.star_bucks_count -= 1
            self.star_bucks_product -= 4.75
            self.running_total -= 4.75 
            self.ids.reciept_screen.ids.star_bucks_count.text = ' s bucks: \n' + str(self.star_bucks_count) + ' = '+ str(self.star_bucks_product)
            self.update_all_screen_totals()

    def add_to_raze(self, button_name):
        self.raze_total += 1
        self.raze_count += 1
        self.raze_product = (self.raze_count * 3 )
        self.ids.reciept_screen.ids.raze_count.text = ' raze: \n' + str(self.raze_count) + ' = '+ str(self.raze_product)

    def minus_to_raze(self, button_name):
        if self.raze_count == 0 :
            self.ids.reciept_screen.ids.raze_count.text = ' '
        elif self.raze_count != 0:
            self.raze_total -= 1
            self.raze_count -= 1
            self.raze_product -= 3
            self.running_total -= 3 
            self.ids.reciept_screen.ids.raze_count.text = ' raze: \n' + str(self.raze_count) + ' = '+ str(self.raze_product)
            self.update_all_screen_totals()

    def add_to_bang(self, button_name):
        self.bang_total += 1
        self.bang_count += 1
        self.bang_product = (self.bang_count * 3 )
        self.ids.reciept_screen.ids.bang_count.text = ' bang: \n' + str(self.bang_count) + ' = '+ str(self.bang_product)

    def minus_to_bang(self, button_name):
        if self.bang_count == 0 :
            self.ids.reciept_screen.ids.bang_count.text = ' '
        elif self.bang_count != 0:
            self.bang_total -= 1
            self.bang_count -= 1
            self.bang_product -= 3
            self.running_total -= 3 
            self.ids.reciept_screen.ids.bang_count.text = ' bang: \n' + str(self.bang_count) + ' = '+ str(self.bang_product)
            self.update_all_screen_totals()

    def add_to_electro_life(self, button_name):
        self.electro_life_total += 1
        self.electro_life_count += 1
        self.electro_life_product = (self.electro_life_count * 4.75 )
        self.ids.reciept_screen.ids.electro_life_count.text = ' e water : \n' + str(self.electro_life_count) + ' = '+ str(self.electro_life_product)

    def minus_to_electro_life(self, button_name):
        if self.electro_life_count == 0 :
            self.ids.reciept_screen.ids.electro_life_count.text = ' '
        elif self.electro_life_count != 0:
            self.electro_life_total -= 1
            self.electro_life_count -= 1
            self.electro_life_product -= 4.75
            self.running_total -= 4.75 
            self.ids.reciept_screen.ids.electro_life_count.text = ' e water: \n' + str(self.electro_life_count) + ' = '+ str(self.electro_life_product)
            self.update_all_screen_totals()

    def add_to_coconut_water(self, button_name):
        self.coconut_water_total += 1
        self.coconut_water_count += 1
        self.coconut_water_product = (self.coconut_water_count * 3.5 )
        self.ids.reciept_screen.ids.coconut_water_count.text = ' c water: \n' + str(self.coconut_water_count) + ' = '+ str(self.coconut_water_product)
   
    def minus_to_coconut_water(self, button_name):
        if self.coconut_water_count == 0 :
            self.ids.reciept_screen.ids.coconut_water_count.text = ' '
        elif self.coconut_water_count != 0:
            self.coconut_water_total -= 1
            self.coconut_water_count -= 1
            self.coconut_water_product -= 3.5
            self.running_total -= 3.5 
            self.ids.reciept_screen.ids.coconut_water_count.text = ' c water: \n' + str(self.coconut_water_count) + ' = '+ str(self.coconut_water_product)
            self.update_all_screen_totals()

    def add_to_five_hour(self, button_name):
        self.five_hour_total += 1
        self.five_hour_count += 1
        self.five_hour_product = (self.five_hour_count * 3.25 )
        self.ids.reciept_screen.ids.five_hour_count.text = ' 5 hour: \n' + str(self.five_hour_count) + ' = '+ str(self.five_hour_product)

    def minus_to_five_hour(self, button_name):
        if self.five_hour_count == 0 :
            self.ids.reciept_screen.ids.five_hour_count.text = ' '
        elif self.five_hour_count != 0:
            self.five_hour_total -= 1
            self.five_hour_count -= 1
            self.five_hour_product -= 3.25
            self.running_total -= 3.25 
            self.ids.reciept_screen.ids.five_hour_count.text = ' 5 hour: \n' + str(self.five_hour_count) + ' = '+ str(self.five_hour_product)
            self.update_all_screen_totals()

    def add_to_breakfast(self, button_name):
        self.breakfast_total += 1
        self.breakfast_count += 1
        self.breakfast_product = (self.breakfast_count * 3.75  )
        self.ids.reciept_screen.ids.breakfast_count.text = 'bkft : \n' + str(self.breakfast_count) + ' = '+ str(self.breakfast_product)

    def minus_to_breakfast(self, button_name):
        if self.breakfast_count == 0 :
            self.ids.reciept_screen.ids.breakfast_count.text = ' '
        elif self.breakfast_count != 0:
            self.breakfast_total -= 1
            self.breakfast_count -= 1
            self.breakfast_product -= 3.75
            self.running_total -= 3.75 
            self.ids.reciept_screen.ids.breakfast_count.text = ' bkft: \n' + str(self.breakfast_count) + ' = '+ str(self.breakfast_product)
            self.update_all_screen_totals()  

    def add_to_small_burrito(self, button_name):
        self.small_burrito_total += 1
        self.small_burrito_count += 1
        self.small_burrito_product = (self.small_burrito_count * 3.25 )
        self.ids.reciept_screen.ids.small_burrito_count.text = 's burrito : \n' + str(self.small_burrito_count) + ' = '+ str(self.small_burrito_product)  

    def minus_to_small_burrito(self, button_name):
        if self.small_burrito_count == 0 :
            self.ids.reciept_screen.ids.small_burrito_count.text = ' '
        elif self.small_burrito_count != 0:
            self.small_burrito_total -= 1
            self.small_burrito_count -= 1
            self.small_burrito_product -= 3.25
            self.running_total -= 3.25 
            self.ids.reciept_screen.ids.small_burrito_count.text = ' s burrito: \n' + str(self.small_burrito_count) + ' = '+ str(self.small_burrito_product)
            self.update_all_screen_totals()

    def add_to_large_burrito(self, button_name):
        self.large_burrito_total += 1
        self.large_burrito_count += 1
        self.large_burrito_product = (self.large_burrito_count * 4 )
        self.ids.reciept_screen.ids.large_burrito_count.text = 'l burrito : \n' + str(self.large_burrito_count) + ' = '+ str(self.large_burrito_product)  

    def minus_to_large_burrito(self, button_name):
        if self.large_burrito_count == 0 :
            self.ids.reciept_screen.ids.large_burrito_count.text = ' '
        elif self.large_burrito_count != 0:
            self.large_burrito_total -= 1
            self.large_burrito_count -= 1
            self.large_burrito_product -= 4
            self.running_total -= 4 
            self.ids.reciept_screen.ids.large_burrito_count.text = ' l burrito: \n' + str(self.large_burrito_count) + ' = '+ str(self.large_burrito_product)
            self.update_all_screen_totals()

    def add_to_calzone(self, button_name):
        self.calzone_total += 1
        self.calzone_count += 1
        self.calzone_product = (self.calzone_count * 4 )
        self.ids.reciept_screen.ids.calzone_count.text = 'calzone : \n' + str(self.calzone_count) + ' = '+ str(self.calzone_product)  
    
    def minus_to_calzone(self, button_name):
        if self.calzone_count == 0 :
            self.ids.reciept_screen.ids.calzone_count.text = ' '
        elif self.calzone_count != 0:
            self.calzone_total -= 1
            self.calzone_count -= 1
            self.calzone_product -= 4
            self.running_total -= 4 
            self.ids.reciept_screen.ids.calzone_count.text = ' calzone: \n' + str(self.calzone_count) + ' = '+ str(self.calzone_product)
            self.update_all_screen_totals()

    def add_to_big_chicken(self, button_name):
        self.big_chicken_total += 1
        self.big_chicken_count += 1
        self.big_chicken_product = (self.big_chicken_count * 4.5 )
        self.ids.reciept_screen.ids.big_chicken_count.text = 'big chicken : \n' + str(self.big_chicken_count) + ' = '+ str(self.big_chicken_product)  

    def minus_to_big_chicken(self, button_name):
        if self.big_chicken_count == 0 :
            self.ids.reciept_screen.ids.big_chicken_count.text = ' '
        elif self.big_chicken_count != 0:
            self.big_chicken_total -= 1
            self.big_chicken_count -= 1
            self.big_chicken_product -= 4.5
            self.running_total -= 4.5 
            self.ids.reciept_screen.ids.big_chicken_count.text = ' big chicken: \n' + str(self.big_chicken_count) + ' = '+ str(self.big_chicken_product)
            self.update_all_screen_totals()

    def add_to_pbj(self, button_name):
        self.pbj_total += 1
        self.pbj_count += 1
        self.pbj_product = (self.pbj_count * 1.5 )
        self.ids.reciept_screen.ids.pbj_count.text = 'pbj : \n' + str(self.pbj_count) + ' = '+ str(self.pbj_product) 
        
    def minus_to_pbj(self, button_name):
        if self.pbj_count == 0 :
            self.ids.reciept_screen.ids.pbj_count.text = ' '
        elif self.pbj_count != 0:
            self.pbj_total -= 1
            self.pbj_count -= 1
            self.pbj_product -= 1.5
            self.running_total -= 1.5 
            self.ids.reciept_screen.ids.pbj_count.text = ' pbj ' + str(self.pbj_count) + ' = '+ str(self.pbj_product)
            self.update_all_screen_totals()

    def add_to_brats(self, button_name):
        self.brats_total += 1
        self.brats_count += 1
        self.brats_product = (self.brats_count * 3 )
        self.ids.reciept_screen.ids.brats_count.text = 'brats : \n' + str(self.brats_count) + ' = '+ str(self.brats_product) 

    def minus_to_brats(self, button_name):
        if self.brats_count == 0 :
            self.ids.reciept_screen.ids.brats_count.text = ' '
        elif self.brats_count != 0:
            self.brats_total -= 1
            self.brats_count -= 1
            self.brats_product -= 3
            self.running_total -= 3
            self.ids.reciept_screen.ids.brats_count.text = ' brats: \n' + str(self.brats_count) + ' = '+ str(self.brats_product)
            self.update_all_screen_totals() 

    def add_to_fresh_and_ready(self, button_name):
        self.fresh_and_ready_total += 1
        self.fresh_and_ready_count += 1       
        self.fresh_and_ready_product = (self.fresh_and_ready_count * 6.25 )
        self.ids.reciept_screen.ids.fresh_and_ready_count.text = ' F&R : \n' + str(self.fresh_and_ready_count) + ' = '+ str(self.fresh_and_ready_product)  

    def minus_to_fresh_and_ready(self, button_name):
        if self.fresh_and_ready_count == 0 :
            self.ids.reciept_screen.ids.fresh_and_ready_count.text = ' '
        elif self.fresh_and_ready_count != 0:
            self.fresh_and_ready_total -= 1
            self.fresh_and_ready_count -= 1
            self.fresh_and_ready_product -= 6.25
            self.running_total -= 6.25 
            self.ids.reciept_screen.ids.fresh_and_ready_count.text = ' F&R: \n' + str(self.fresh_and_ready_count) + ' = '+ str(self.fresh_and_ready_product)
            self.update_all_screen_totals()

    def add_to_tuna(self, button_name):
        self.tuna_total += 1
        self.tuna_count += 1
        self.tuna_product = (self.tuna_count * 3.5 )
        self.ids.reciept_screen.ids.tuna_count.text = 'tuna : \n' + str(self.tuna_count) + ' = '+ str(self.tuna_product) 

    def minus_to_tuna(self, button_name):
        if self.tuna_count == 0 :
            self.ids.reciept_screen.ids.tuna_count.text = ' '
        elif self.tuna_count != 0:
            self.tuna_total -= 1
            self.tuna_count -= 1
            self.tuna_product -= 3.50
            self.running_total -= 3.50 
            self.ids.reciept_screen.ids.tuna_count.text = ' tuna: \n' + str(self.tuna_count) + ' = '+ str(self.tuna_product)
            self.update_all_screen_totals() 

    def add_to_parfait(self, button_name):
        self.parfait_total += 1
        self.parfait_count += 1
        self.parfait_product = (self.parfait_count * 6.25 )
        self.ids.reciept_screen.ids.parfait_count.text = ' parfait: \n' + str(self.parfait_count) + ' = '+ str(self.parfait_product)  

    def minus_to_parfait(self, button_name):
        if self.parfait_count == 0 :
            self.ids.reciept_screen.ids.parfait_count.text = ' '
        elif self.parfait_count != 0:
            self.parfait_total -= 1
            self.parfait_count -= 1
            self.parfait_product -= 6.25
            self.running_total -= 6.25 
            self.ids.reciept_screen.ids.parfait_count.text = ' parfait: \n' + str(self.parfait_count) + ' = '+ str(self.parfait_product)
            self.update_all_screen_totals()

    def add_to_ciggs(self, button_name):
        self.ciggs_total += 1
        self.ciggs_count += 1
        self.ciggs_product = (self.ciggs_count * 10 )
        self.ids.reciept_screen.ids.ciggs_count.text = ' ciggs: \n' + str(self.ciggs_count) + ' = '+ str(self.ciggs_product)

    def minus_to_ciggs(self, button_name):
        if self.ciggs_count == 0 :
            self.ids.reciept_screen.ids.ciggs_count.text = ' '
        elif self.ciggs_count != 0:
            self.ciggs_total -= 1
            self.ciggs_count -= 1
            self.ciggs_product -= 10
            self.running_total -= 10 
            self.ids.reciept_screen.ids.ciggs_count.text = ' ciggs ' + str(self.ciggs_count) + ' = '+ str(self.ciggs_product)
            self.update_all_screen_totals()  

    def add_to_grizzly(self, button_name):
        self.grizzly_total += 1
        self.grizzly_count += 1
        self.grizzly_product = (self.grizzly_count * 6  )
        self.ids.reciept_screen.ids.grizzly_count.text = 'grizzly : \n' + str(self.grizzly_count) + ' = '+ str(self.grizzly_product)  

    def minus_to_grizzly(self, button_name):
        if self.grizzly_count == 0 :
            self.ids.reciept_screen.ids.grizzly_count.text = ' '
        elif self.grizzly_count != 0:
            self.grizzly_total -= 1
            self.grizzly_count -= 1
            self.grizzly_product -= 6
            self.running_total -= 6 
            self.ids.reciept_screen.ids.grizzly_count.text = ' grizzly: \n' + str(self.grizzly_count) + ' = '+ str(self.grizzly_product)
            self.update_all_screen_totals()

    def add_to_stokers(self, button_name):
        self.stokers_total += 1
        self.stokers_count += 1
        self.stokers_product = (self.stokers_count * 18 )
        self.ids.reciept_screen.ids.stokers_count.text = 'stokers : \n' + str(self.stokers_count) + ' = '+ str(self.stokers_product)  

    def minus_to_stokers(self, button_name):
        if self.stokers_count == 0 :
            self.ids.reciept_screen.ids.stokers_count.text = ' '
        elif self.stokers_count != 0:
            self.stokers_total -= 1
            self.stokers_count -= 1
            self.stokers_product -= 18
            self.running_total -= 18 
            self.ids.reciept_screen.ids.stokers_count.text = ' stokers: \n' + str(self.stokers_count) + ' = '+ str(self.stokers_product)
            self.update_all_screen_totals()

    def add_to_lighters(self, button_name):
        self.lighters_total += 1
        self.lighters_count += 1
        self.lighters_product = (self.lighters_count * 2 )
        self.ids.reciept_screen.ids.lighters_count.text = 'lighters : \n' + str(self.lighters_count) + ' = '+ str(self.lighters_product)  

    def minus_to_lighters(self, button_name):
        if self.lighters_count == 0 :
            self.ids.reciept_screen.ids.lighters_count.text = ' '
        elif self.lighters_count != 0:
            self.lighters_total -= 1
            self.lighters_count -= 1
            self.lighters_product -= 2
            self.running_total -= 2 
            self.ids.reciept_screen.ids.lighters_count.text = ' lighters: \n' + str(self.lighters_count) + ' = '+ str(self.lighters_product)
            self.update_all_screen_totals()

    def add_to_chapstick(self, button_name):
        self.chapstick_total += 1
        self.chapstick_count += 1
        self.chapstick_product = (self.chapstick_count * 3.25 )
        self.ids.reciept_screen.ids.chapstick_count.text = ' chapstick: \n' + str(self.chapstick_count) + ' = '+ str(self.chapstick_product)  

    def minus_to_chapstick(self, button_name):
        if self.chapstick_count == 0 :
            self.ids.reciept_screen.ids.chapstick_count.text = ' '
        elif self.chapstick_count != 0:
            self.five_hour_total -= 1
            self.chapstick_count -= 1
            self.chapstick_product -= 3.25
            self.running_total -= 3.25 
            self.ids.reciept_screen.ids.chapstick_count.text = ' chapstick: \n' + str(self.chapstick_count) + ' = '+ str(self.chapstick_product)
            self.update_all_screen_totals()

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