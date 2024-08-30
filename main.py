from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.popup import Popup
import random
import json
from db_manager import DBManager

class ChampionSelector(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = DBManager()
        self.orientation = 'vertical'
        self.load_champions()

    def load_champions(self):
        with open('champions.json', 'r') as file:
            self.champions = json.load(file)
        
        self.select_random_champion()

    def select_random_champion(self):
        if not self.champions:
            popup = Popup(title='Error', content=Label(text='No more champions available'), size_hint=(None, None), size=(400, 200))
            popup.open()
            return

        champion = random.choice(self.champions)
        self.display_champion(champion)

    def display_champion(self, champion):
        self.clear_widgets()

        img = Image(source=f"assets/{champion['image']}")
        name_label = Label(text=champion['name'], font_size='24sp')
        victory_button = Button(text='Victory', on_press=lambda x: self.record_victory(champion))
        defeat_button = Button(text='Defeat', on_press=lambda x: self.record_defeat(champion))
        next_button = Button(text='Next Champion', on_press=lambda x: self.remove_and_next_champion(champion))

        self.add_widget(img)
        self.add_widget(name_label)
        self.add_widget(victory_button)
        self.add_widget(defeat_button)
        self.add_widget(next_button)

    def record_victory(self, champion):
        self.db.update_victory(champion['name'])

    def record_defeat(self, champion):
        self.db.update_defeat(champion['name'])

    def remove_and_next_champion(self, champion):
        self.db.delete_champion(champion['name'])
        self.champions.remove(champion)
        self.select_random_champion()

    def on_stop(self):
        self.db.close()

class ChampionApp(App):
    def build(self):
        return ChampionSelector()

if __name__ == '__main__':
    ChampionApp().run()
