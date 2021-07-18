'''

App Class will contain the main GUI of the program using DearPyGui

'''

import dearpygui.dearpygui as dpg
from src.PlayerClass import *


class App:

    def __init__(self):
        self.team1 = []
        self.team2 = []

        self.leftGroup_id = dpg.generate_uuid()
        self.middleGroup_id = dpg.generate_uuid()
        self.rightGroup_id = dpg.generate_uuid()

        self.leftChild_id = dpg.generate_uuid()
        self.rightChild_id = dpg.generate_uuid()

    def CreatePlayerButton(self, sender, app_data, user_data):
        name = dpg.get_value(user_data[0])
        parent = user_data[1]
        team = user_data[2]
        new_player = PlayerClass(name)

        if team == 1 and len(self.team1) < 15:
            self.team1.append(new_player)
            dpg.add_spacing(count=3, parent=parent)
            dpg.add_button(label=name, parent=parent, width=200)

        elif team == 2 and len(self.team2) < 15:
            self.team2.append(new_player)
            dpg.add_spacing(count=3, parent=parent)
            dpg.add_button(label=name, parent=parent, width=200)

    def AddPlayer1(self):
        name_id = 0
        with dpg.window(width=400):
            name_id = dpg.add_input_text(label="Enter Player's Name", width=200)
            dpg.add_button(label="Add Player", width=200, callback=self.CreatePlayerButton,
                           user_data=[name_id, self.leftGroup_id, 1])

    def AddPlayer2(self):
        name_id = 0
        with dpg.window(width=300):
            name_id = dpg.add_input_text(label="Enter Player's Name", width=200)
            dpg.add_button(label="Add Player", width=200, callback=self.CreatePlayerButton,
                           user_data=[name_id, self.rightGroup_id, 2])

    def start(self):

        dpg.setup_registries()
        dpg.setup_viewport()
        dpg.set_viewport_title("Basketball Stat Tracker")

        with dpg.window() as main_window:

            with dpg.menu_bar():
                dpg.add_menu_item(label="Start Game")
                dpg.add_menu_item(label="Box Score")

            dpg.add_spacing(count=20)
            with dpg.group(horizontal=True, horizontal_spacing=750) as group:

                with dpg.child(width=250, height=600, id=self.leftChild_id):
                    with dpg.group(id=self.leftGroup_id):
                        dpg.add_text(default_value="Team 1")
                        dpg.add_same_line(spacing=15)
                        dpg.add_button(label="+", width=20, height=20, callback=self.AddPlayer1)

                with dpg.child(width=250, height=600, id=self.rightChild_id):
                    with dpg.group(id=self.rightGroup_id):
                        dpg.add_text(default_value="Team 2")
                        dpg.add_same_line(spacing=15)
                        dpg.add_button(label="+", width=20, height=20, callback=self.AddPlayer2)

        dpg.set_primary_window(main_window, True)
        dpg.start_dearpygui()