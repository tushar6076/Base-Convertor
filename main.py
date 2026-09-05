import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import ThreeLineListItem
import sqlite3
from datetime import datetime

Builder.load_string("""
                    
<MyDropDown@DropDown>:
    max_height: 600
    
<Home>:
    MDScreen:
        MDNavigationLayout:
            MDScreenManager:
                MDScreen:
                    
                    Spinner:
                        id: spinner
                        dropdown_cls: 'MyDropDown'
                        size_hint: (1, 0.15)
                        pos_hint: {'top': 1}
                        halign: 'center'
                        color: [1, 1, 1, 1]
                        background_color: [0, 115, 176, 1]
                        font_style: 'H6'
                        font_size: root.height/24
                        text: 'Decimal to Binary'
                        values: ['Decimal to Binary',\
                            'Binary to Decimal',\
                            'Decimal to Octal',\
                            'Octal to Decimal',\
                            'Decimal to Hexadecimal',\
                            'Hexadecimal to Decimal',\
                            'Binary to Octal',\
                            'Octal to Binary',\
                            'Binary to Hexadecimal',\
                            'Hexadecimal to Binary',\
                            'Octal to Hexadecimal',\
                            'Hexadecimal to Octal']
                        on_text: root.select()
                    
                    MDTextField:
                        id: input
                        hint_text: 'Enter a Decimal Number : '
                        halign: 'center'
                        size_hint: (0.75, 0.15)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                        font_size: root.height/26
                        on_text_validate: root.convert()
                    
                    MDLabel:
                        id: label
                        halign: 'center'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                        font_style: 'Caption'
                        font_size: root.height/26
                    
                    MDLabel:
                        id: converted
                        halign: 'center'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
                        font_style: 'Caption'
                        font_size: root.height/26
                    
                    MDFillRoundFlatButton:
                        id: button
                        text: 'convert'
                        text_color: [1, 1, 1, 1]
                        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
                        font_style: 'Button'
                        font_size: root.height/26
                        on_press: root.convert()
                    
            MDNavigationDrawer:
                anchor: 'right'
                swipe_edge_width: root.width/4
                swipe_distance: root.width/1000

                MDBoxLayout:
                    id: drawer_layout
                    orientation: 'vertical'
                    padding: '10dp'
                    spacing: '10dp'

                    MDLabel:
                        id: hist_label
                        text: 'No Conversion is Performed yet....'
                        font_style: 'H1'
                        font_size: root.height/16
                    
                    MDScrollView:
                        scroll_y: 0
                        smooth_scroll_end: 100

                        MDList:
                            id: list
""")

class ConvertorApp(MDApp):

    def build(self):
        with open ('history.db', 'a'):
            pass

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.primary_hue = '300'
        self.manager = MDScreenManager()
        self.manager.add_widget(Home(name = 'home'))

        return self.manager
    
    def on_start(self):
        db = sqlite3.connect('history.db')
        cr = db.cursor()
        cr.execute("SELECT name FROM sqlite_master WHERE type = 'table'")

        if cr.fetchall() == []:
            cr.execute('''CREATE TABLE record(
	                    conversion VARCHAR(22) NOT NULL,
	                    deduce VARCHAR(128) NOT NULL,
                        time VARCHAR(40) UNIQUE NOT NULL)''')

        else:
            cr.execute("SELECT * FROM record")
            data = cr.fetchall()

            if data != []:
                self.manager.get_screen('home').ids.drawer_layout.remove_widget(
                    self.manager.get_screen('home').ids.hist_label
                )
                for row in data:
                    self.manager.get_screen('home').ids.list.add_widget(
                        ThreeLineListItem(
                            text = row[0],
                            secondary_text = row[1],
                            tertiary_text = row[2],
                        )
                    )
        db.close()

class Home(MDScreen):

    def select(self):
        number = self.ids.spinner.text.split()[0]
        hint_text = f"Enter a {number} number : "

        if self.ids.input.hint_text != hint_text:
            self.ids.input.text = ""
            self.ids.label.text = ""
            self.ids.converted.text = ""
            self.ids.input.hint_text = hint_text

    def convert(self):
        try:
            self.ids.label.text = f"in {self.ids.spinner.text.split()[-1]} is"

            if "." not in self.ids.input.text:

                if self.ids.spinner.text == 'Decimal to Binary':
                    val = bin(int(self.ids.input.text))[2:]

                elif self.ids.spinner.text == 'Binary to Decimal':
                    val = int(self.ids.input.text, 2)

                elif self.ids.spinner.text == 'Decimal to Octal':
                    val = oct(int(self.ids.input.text))[2:]

                elif self.ids.spinner.text == 'Octal to Decimal':
                    val = int(self.ids.input.text, 8)

                elif self.ids.spinner.text == 'Decimal to Hexadecimal':
                    val = hex(int(self.ids.input.text))[2:]

                elif self.ids.spinner.text == 'Hexadecimal to Decimal':
                    val = int(self.ids.input.text, 16)

                elif self.ids.spinner.text == 'Binary to Octal':
                    val = oct(int(self.ids.input.text, 2))[2:]

                elif self.ids.spinner.text == 'Octal to Binary':
                    val = bin(int(self.ids.input.text, 8))[2:]

                elif self.ids.spinner.text == 'Binary to Hexadecimal':
                    val = hex(int(self.ids.input.text, 2))[2:]

                elif self.ids.spinner.text == 'Hexadecimal to Binary':
                    val = bin(int(self.ids.input.text, 16))[2:]

                elif self.ids.spinner.text == 'Octal to Hexadecimal':
                    val = hex(int(self.ids.input.text, 8))[2:]

                elif self.ids.spinner.text == 'Hexadecimal to Octal':
                    val = oct(int(self.ids.input.text, 16))[2:]

                self.ids.converted.text = str(val)

            else:
                whole, fract = self.ids.input.text.split(".")

                if self.ids.spinner.text == 'Decimal to Binary':
                    whole = bin(int(whole))[2:]
                    fract = float("0."+fract) * 2
                    floating = "."
                    for i in range(10):
                        floating += str(int(fract // 1))
                        if fract % 1 == 0:
                            break
                        fract = (fract - (fract // 1)) * 2

                elif self.ids.spinner.text == 'Binary to Decimal':
                    whole = int(whole, 2)
                    floating = 0                    
                    for i, digit in enumerate(fract):
                        floating += int(digit, 2) * 2 ** (-(i+1))

                elif self.ids.spinner.text == 'Decimal to Octal':
                    whole = oct(int(whole))[2:]
                    fract = float("0."+fract) * 8
                    floating = "."
                    for i in range(10):
                        floating += str(int(fract // 1))
                        if fract % 1 == 0:
                            break
                        fract = (fract - (fract // 1) ) * 8

                elif self.ids.spinner.text == 'Octal to Decimal':
                    whole = int(whole, 8)
                    floating = 0                   
                    for i, digit in enumerate(fract):
                        floating += int(digit, 8) * 8 ** (-(i+1))

                elif self.ids.spinner.text == 'Decimal to Hexadecimal':
                    whole = oct(int(whole))[2:]
                    fract = float("0."+fract) * 16
                    floating = "."
                    for i in range(10):
                        floating += str(hex(int(fract//1))[2:])
                        if fract % 1 == 0:
                            break
                        fract = (fract - (fract // 1)) * 16

                elif self.ids.spinner.text == 'Hexadecimal to Decimal':
                    whole = int(whole, 16)
                    floating = 0                   
                    for i, digit in enumerate(fract):
                        floating += int(digit, 16) * 16 ** (-(i+1))

                elif self.ids.spinner.text == 'Binary to Octal':
                    whole = oct(int(whole, 2))[2:]
                    decimal = 0                   
                    for i, digit in enumerate(fract):
                        decimal += int(digit, 2) * 2 ** (-(i+1))
                    fract = decimal * 8
                    floating = "."
                    for i in range(10):
                        floating += str(int(fract // 1))
                        if fract % 1 == 0:
                            break
                        fract = (fract - (fract // 1) ) * 8

                elif self.ids.spinner.text == 'Octal to Binary':
                    whole = bin(int(whole, 8))[2:]
                    decimal = 0                   
                    for i, digit in enumerate(fract):
                        decimal += int(digit, 8) * 8 ** (-(i+1))
                    fract = decimal * 2
                    floating = "."
                    for i in range(10):
                        floating += str(int(fract // 1))
                        if fract % 1 == 0:
                            break
                        fract = (fract - (fract // 1) ) * 2

                elif self.ids.spinner.text == 'Binary to Hexadecimal':
                    whole = hex(int(whole, 2))[2:]
                    decimal = 0                    
                    for i, digit in enumerate(fract):
                        decimal += int(digit, 2) * 2 ** (-(i+1))
                    fract = decimal * 16
                    floating = "."
                    for i in range(10):
                        floating += str(hex(int(fract // 1))[2:])
                        if fract % 1 == 0:
                            break
                        fract = (fract - (fract // 1) ) * 16

                elif self.ids.spinner.text == 'Hexadecimal to Binary':
                    whole = bin(int(whole, 16))[2:]
                    decimal = 0
                    for i, digit in enumerate(fract):
                        decimal += int(digit, 16) * 16 ** (-(i+1))
                    fract = decimal * 2
                    floating = "."
                    for i in range(10):
                        floating += str(int(fract // 1))
                        if fract % 1 == 0:
                            break
                        fract = (fract - (fract // 1) ) * 2

                elif self.ids.spinner.text == 'Octal to Hexadecimal':
                    whole = hex(int(whole, 8))[2:]
                    decimal = 0                    
                    for i, digit in enumerate(fract):
                        decimal += int(digit, 8) * 8 ** (-(i+1))
                    fract = decimal * 16
                    floating = "."
                    for i in range(10):
                        floating += str(hex(int(fract // 1))[2:])
                        if fract % 1 == 0:
                            break
                        fract = (fract - (fract // 1) ) * 16

                elif self.ids.spinner.text == 'Hexadecimal to Octal':
                    whole = oct(int(whole, 16))[2:]
                    decimal = 0
                    for i, digit in enumerate(fract):
                        decimal += int(digit, 16) * 16 ** (-(i+1))
                    fract = decimal * 8
                    floating = "."
                    for i in range(10):
                        floating += str(int(fract // 1))
                        if fract % 1 == 0:
                            break
                        fract = (fract - (fract // 1) ) * 8

                self.ids.converted.text = str(whole + floating)

            deduce = self.ids.input.text + " = " + self.ids.converted.text
            time = str(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

            db = sqlite3.connect('history.db')
            cr = db.cursor()
            cr.execute(f'''INSERT INTO record VALUES(
                        '{self.ids.spinner.text}',
                        '{deduce}', '{time}')''')
            db.commit()
            db.close()

            self.ids.drawer_layout.remove_widget(self.ids.hist_label)
            self.ids.list.add_widget(
                ThreeLineListItem(
                    text = self.ids.spinner.text,
                    secondary_text = deduce,
                    tertiary_text = time,
                )
            )

        except ValueError:
            self.ids.converted.text = ""

            if self.ids.spinner.text == 'Decimal to Binary':
                self.ids.label.text = 'Please enter a valid Decimal number'

            elif self.ids.spinner.text == 'Binary to Decimal':
                self.ids.label.text = 'Please enter a valid Binary number'

            elif self.ids.spinner.text == 'Decimal to Octal':
                self.ids.label.text = 'Please enter a valid Decimal number'

            elif self.ids.spinner.text == 'Octal to Decimal':
                self.ids.label.text = 'Please enter a valid Octal number'
            
            elif self.ids.spinner.text == 'Decimal to Hexadecimal':
                self.ids.label.text = 'Please enter a valid Decimal number'

            elif self.ids.spinner.text == 'Hexadecimal to Decimal':
                self.ids.label.text = 'Please enter a valid Hexadecimal number'

            elif self.ids.spinner.text == 'Binary to Octal':
                self.ids.label.text = 'Please enter a valid Binary number'
            
            elif self.ids.spinner.text == 'Octal to Binary':
                self.ids.label.text = 'Please enter a valid Octal number'

            elif self.ids.spinner.text == 'Binary to Hexadecimal':
                self.ids.label.text='Please enter a valid Binary number'

            elif self.ids.spinner.text == 'Hexadecimal to Binary':
                self.ids.label.text = 'Please enter a valid Hexadecimal number'

            elif self.ids.spinner.text == 'Octal to Hexadecimal':
                self.ids.label.text = 'Please enter a valid Octal number'

            elif self.ids.spinner.text == 'Hexadecimal to Octal':
                self.ids.label.text = 'Please enter a valid Hexadecimal number'

if __name__ == "__main__" :
    ConvertorApp().run()