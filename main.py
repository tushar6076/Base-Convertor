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
                        values: [
                            'Decimal to Binary',
                            'Binary to Decimal',
                            'Decimal to Octal',
                            'Octal to Decimal',
                            'Decimal to Hexadecimal',
                            'Hexadecimal to Decimal',
                            'Binary to Octal',
                            'Octal to Binary',
                            'Binary to Hexadecimal',
                            'Hexadecimal to Binary',
                            'Octal to Hexadecimal',
                            'Hexadecimal to Octal'
                            ]
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
                        font_style: 'H6'
                        font_size: root.height/28
                        halign: 'center'

                    MDScrollView:
                        scroll_y: 0
                        smooth_scroll_end: 100

                        MDList:
                            id: list
""")

class ConvertorApp(MDApp):

    def build(self):
        with open('history.db', 'a'):
            pass

        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.primary_hue = '300'
        self.manager = MDScreenManager()
        self.manager.add_widget(Home(name='home'))
        return self.manager

    def on_start(self):
        db = sqlite3.connect('history.db')
        cr = db.cursor()
        cr.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name = 'record'")

        if not cr.fetchall():
            cr.execute('''CREATE TABLE record(
                        conversion VARCHAR(22) NOT NULL,
                        deduce VARCHAR(128) NOT NULL,
                        time VARCHAR(40) UNIQUE NOT NULL)''')
        else:
            cr.execute("SELECT * FROM record")
            data = cr.fetchall()
            home_screen = self.manager.get_screen('home')

            if data:
                if home_screen.ids.hist_label in home_screen.ids.drawer_layout.children:
                    home_screen.ids.drawer_layout.remove_widget(home_screen.ids.hist_label)
                for row in data:
                    home_screen.ids.list.add_widget(
                        ThreeLineListItem(
                            text=row[0],
                            secondary_text=row[1],
                            tertiary_text=row[2],
                        )
                    )
        db.close()


class Home(MDScreen):
    prev_conversion = "Decimal to Binary"

    def select(self):
        current_conversion = self.ids.spinner.text
        if current_conversion != self.prev_conversion:
            source = current_conversion.split()[0]
            self.ids.input.text = ""
            self.ids.label.text = ""
            self.ids.converted.text = ""
            self.ids.input.hint_text = f"Enter a {source} Number : "
            self.prev_conversion = current_conversion

    def convert(self):
        raw_text = self.ids.input.text.strip()
        if not raw_text:
            return

        try:
            conversion_type = self.ids.spinner.text
            target_name = conversion_type.split()[-1]
            self.ids.label.text = f"in {target_name} is"

            if "." not in raw_text:
                if conversion_type == 'Decimal to Binary':
                    val = bin(int(raw_text))[2:]
                elif conversion_type == 'Binary to Decimal':
                    val = int(raw_text, 2)
                elif conversion_type == 'Decimal to Octal':
                    val = oct(int(raw_text))[2:]
                elif conversion_type == 'Octal to Decimal':
                    val = int(raw_text, 8)
                elif conversion_type == 'Decimal to Hexadecimal':
                    val = hex(int(raw_text))[2:].upper()
                elif conversion_type == 'Hexadecimal to Decimal':
                    val = int(raw_text, 16)
                elif conversion_type == 'Binary to Octal':
                    val = oct(int(raw_text, 2))[2:]
                elif conversion_type == 'Octal to Binary':
                    val = bin(int(raw_text, 8))[2:]
                elif conversion_type == 'Binary to Hexadecimal':
                    val = hex(int(raw_text, 2))[2:].upper()
                elif conversion_type == 'Hexadecimal to Binary':
                    val = bin(int(raw_text, 16))[2:]
                elif conversion_type == 'Octal to Hexadecimal':
                    val = hex(int(raw_text, 8))[2:].upper()
                elif conversion_type == 'Hexadecimal to Octal':
                    val = oct(int(raw_text, 16))[2:]
                result_str = str(val)

            else:
                parts = raw_text.split(".")
                if len(parts) != 2:
                    raise ValueError("Multiple decimal points")

                whole, fract = parts

                if conversion_type == 'Decimal to Binary':
                    whole_res = bin(int(whole))[2:]
                    fract_val = float("0." + fract) * 2
                    floating = "."
                    for _ in range(10):
                        floating += str(int(fract_val // 1))
                        if fract_val % 1 == 0:
                            break
                        fract_val = (fract_val - (fract_val // 1)) * 2

                elif conversion_type == 'Binary to Decimal':
                    whole_res = int(whole, 2)
                    floating = sum(int(d, 2) * (2 ** -(i + 1)) for i, d in enumerate(fract))

                elif conversion_type == 'Decimal to Octal':
                    whole_res = oct(int(whole))[2:]
                    fract_val = float("0." + fract) * 8
                    floating = "."
                    for _ in range(10):
                        floating += str(int(fract_val // 1))
                        if fract_val % 1 == 0:
                            break
                        fract_val = (fract_val - (fract_val // 1)) * 8

                elif conversion_type == 'Octal to Decimal':
                    whole_res = int(whole, 8)
                    floating = sum(int(d, 8) * (8 ** -(i + 1)) for i, d in enumerate(fract))

                elif conversion_type == 'Decimal to Hexadecimal':
                    whole_res = hex(int(whole))[2:].upper()  # Fixed from oct()
                    fract_val = float("0." + fract) * 16
                    floating = "."
                    for _ in range(10):
                        floating += str(hex(int(fract_val // 1))[2:]).upper()
                        if fract_val % 1 == 0:
                            break
                        fract_val = (fract_val - (fract_val // 1)) * 16

                elif conversion_type == 'Hexadecimal to Decimal':
                    whole_res = int(whole, 16)
                    floating = sum(int(d, 16) * (16 ** -(i + 1)) for i, d in enumerate(fract))

                elif conversion_type == 'Binary to Octal':
                    whole_res = oct(int(whole, 2))[2:]
                    dec_fract = sum(int(d, 2) * (2 ** -(i + 1)) for i, d in enumerate(fract))
                    fract_val = dec_fract * 8
                    floating = "."
                    for _ in range(10):
                        floating += str(int(fract_val // 1))
                        if fract_val % 1 == 0:
                            break
                        fract_val = (fract_val - (fract_val // 1)) * 8

                elif conversion_type == 'Octal to Binary':
                    whole_res = bin(int(whole, 8))[2:]
                    dec_fract = sum(int(d, 8) * (8 ** -(i + 1)) for i, d in enumerate(fract))
                    fract_val = dec_fract * 2
                    floating = "."
                    for _ in range(10):
                        floating += str(int(fract_val // 1))
                        if fract_val % 1 == 0:
                            break
                        fract_val = (fract_val - (fract_val // 1)) * 2

                elif conversion_type == 'Binary to Hexadecimal':
                    whole_res = hex(int(whole, 2))[2:].upper()
                    dec_fract = sum(int(d, 2) * (2 ** -(i + 1)) for i, d in enumerate(fract))
                    fract_val = dec_fract * 16
                    floating = "."
                    for _ in range(10):
                        floating += str(hex(int(fract_val // 1))[2:]).upper()
                        if fract_val % 1 == 0:
                            break
                        fract_val = (fract_val - (fract_val // 1)) * 16

                elif conversion_type == 'Hexadecimal to Binary':
                    whole_res = bin(int(whole, 16))[2:]
                    dec_fract = sum(int(d, 16) * (16 ** -(i + 1)) for i, d in enumerate(fract))
                    fract_val = dec_fract * 2
                    floating = "."
                    for _ in range(10):
                        floating += str(int(fract_val // 1))
                        if fract_val % 1 == 0:
                            break
                        fract_val = (fract_val - (fract_val // 1)) * 2

                elif conversion_type == 'Octal to Hexadecimal':
                    whole_res = hex(int(whole, 8))[2:].upper()
                    dec_fract = sum(int(d, 8) * (8 ** -(i + 1)) for i, d in enumerate(fract))
                    fract_val = dec_fract * 16
                    floating = "."
                    for _ in range(10):
                        floating += str(hex(int(fract_val // 1))[2:]).upper()
                        if fract_val % 1 == 0:
                            break
                        fract_val = (fract_val - (fract_val // 1)) * 16

                elif conversion_type == 'Hexadecimal to Octal':
                    whole_res = oct(int(whole, 16))[2:]
                    dec_fract = sum(int(d, 16) * (16 ** -(i + 1)) for i, d in enumerate(fract))
                    fract_val = dec_fract * 8
                    floating = "."
                    for _ in range(10):
                        floating += str(int(fract_val // 1))
                        if fract_val % 1 == 0:
                            break
                        fract_val = (fract_val - (fract_val // 1)) * 8

                if isinstance(floating, (int, float)):
                    result_str = str(whole_res + floating)
                else:
                    result_str = str(whole_res) + str(floating)

            self.ids.converted.text = result_str
            deduce = f"{raw_text} = {result_str}"
            timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            db = sqlite3.connect('history.db')
            cr = db.cursor()
            cr.execute("INSERT INTO record VALUES (?, ?, ?)", (conversion_type, deduce, timestamp))
            db.commit()
            db.close()

            if self.ids.hist_label in self.ids.drawer_layout.children:
                self.ids.drawer_layout.remove_widget(self.ids.hist_label)

            self.ids.list.add_widget(
                ThreeLineListItem(
                    text=conversion_type,
                    secondary_text=deduce,
                    tertiary_text=timestamp,
                )
            )

        except (ValueError, TypeError):
            self.ids.converted.text = ""
            source_type = self.ids.spinner.text.split()[0]
            self.ids.label.text = f"Please enter a valid {source_type} number"


if __name__ == "__main__":
    ConvertorApp().run()