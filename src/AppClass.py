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
        self.middleChild_id = dpg.generate_uuid()
        self.rightChild_id = dpg.generate_uuid()

        self.table_team1 = dpg.generate_uuid()
        self.table_team2 = dpg.generate_uuid()

        self.child_parent_1 = dpg.generate_uuid()
        self.child_parent_2 = dpg.generate_uuid()

        self.score_group = dpg.generate_uuid()
        self.score_1 = dpg.generate_uuid()
        self.score_2 = dpg.generate_uuid()

    def CreatePlayerButton(self, sender, app_data, user_data):
        name = dpg.get_value(user_data[0])
        parent = user_data[1]
        team = user_data[2]
        new_player = PlayerClass(name)

        if team == 1 and len(self.team1) < 15:
            self.team1.append(new_player)
            dpg.add_spacing(count=3, parent=parent)
            dpg.add_button(label=name, parent=parent, width=200, callback=new_player.GenerateWindow)

        elif team == 2 and len(self.team2) < 15:
            self.team2.append(new_player)
            dpg.add_spacing(count=3, parent=parent)
            dpg.add_button(label=name, parent=parent, width=200, callback=new_player.GenerateWindow)

    def AddPlayer1(self):
        name_id = 0
        with dpg.window(width=400, label="Add Player to Team 1"):
            name_id = dpg.add_input_text(label="Enter Player's Name", width=200)
            dpg.add_button(label="Add Player", width=200, callback=self.CreatePlayerButton,
                           user_data=[name_id, self.leftGroup_id, 1])

    def AddPlayer2(self):
        name_id = 0
        with dpg.window(width=400, label="Add Player to Team 2"):
            name_id = dpg.add_input_text(label="Enter Player's Name", width=200)
            dpg.add_button(label="Add Player", width=200, callback=self.CreatePlayerButton,
                           user_data=[name_id, self.rightGroup_id, 2])

    def ShowTable1(self, parent):

        if dpg.does_item_exist(item=self.table_team1):
            dpg.delete_item(item=self.table_team1)

        with dpg.table(id=self.table_team1, parent=parent):
            dpg.add_table_column(label="Name")
            dpg.add_table_column(label="Points")
            dpg.add_table_column(label="Assists")
            dpg.add_table_column(label="Rebounds")
            dpg.add_table_column(label="FG")
            dpg.add_table_column(label="3-FG")
            dpg.add_table_column(label="FT")

            for i in range(0, len(self.team1)):
                stats = self.team1[i].GetStatLine()
                for j in range(0, 7):
                    dpg.add_text(str(stats[j]))
                    if not (i == 4 and j == 6):
                        dpg.add_table_next_column()

    def ShowTable2(self, parent):

        if dpg.does_item_exist(item=self.table_team2):
            dpg.delete_item(item=self.table_team2)

        with dpg.table(id=self.table_team2, parent=parent):
            dpg.add_table_column(label="Name")
            dpg.add_table_column(label="Points")
            dpg.add_table_column(label="Assists")
            dpg.add_table_column(label="Rebounds")
            dpg.add_table_column(label="FG")
            dpg.add_table_column(label="3-FG")
            dpg.add_table_column(label="FT")

            for i in range(0, len(self.team2)):
                stats = self.team2[i].GetStatLine()
                for j in range(0, 7):
                    dpg.add_text(str(stats[j]))
                    if not (i == 4 and j == 6):
                        dpg.add_table_next_column()

    def GetScore1(self, parent):
        if dpg.does_item_exist(item=self.score_1):
            dpg.delete_item(item=self.score_1)

        points = 0
        for player in self.team1:
            points += player.GetPoints()
        dpg.add_text("Team 1 Score: " + str(points), parent=parent, id=self.score_1)

    def GetScore2(self, parent):
        if dpg.does_item_exist(item=self.score_2):
            dpg.delete_item(item=self.score_2)
        points = 0
        for player in self.team2:
            points += player.GetPoints()
        dpg.add_text("Team 2 Score: " + str(points), parent=parent, id=self.score_2)

    def start(self):

        dpg.setup_registries()
        dpg.setup_viewport()
        dpg.set_viewport_title("Basketball Stat Tracker")

        with dpg.window() as main_window:

            with dpg.menu_bar():
                dpg.add_menu_item(label="Start Game")

            dpg.add_spacing(count=5)
            with dpg.group(id=self.score_group):
                self.GetScore1(self.score_group)
                self.GetScore2(self.score_group)
            dpg.add_spacing(count=5)
            with dpg.group(horizontal=True, horizontal_spacing=75) as group:

                with dpg.child(width=250, height=600, id=self.leftChild_id):
                    with dpg.group(id=self.leftGroup_id):
                        dpg.add_text(default_value="Team 1")
                        dpg.add_same_line(spacing=15)
                        dpg.add_button(label="+", width=20, height=20, callback=self.AddPlayer1)

                with dpg.child(width=600, height=600, id=self.middleChild_id):
                    with dpg.group(id=self.middleGroup_id):
                        dpg.add_text("Team 1 Box Score")
                        with dpg.child(width=585, height=255, id=self.child_parent_1):
                            self.ShowTable1(self.child_parent_1)

                        dpg.add_spacing(count=5)
                        dpg.add_text("Team 2 Box Score")
                        with dpg.child(width=585, height=255, id=self.child_parent_2):
                            self.ShowTable2(self.child_parent_2)


                with dpg.child(width=250, height=600, id=self.rightChild_id):
                    with dpg.group(id=self.rightGroup_id):
                        dpg.add_text(default_value="Team 2")
                        dpg.add_same_line(spacing=15)
                        dpg.add_button(label="+", width=20, height=20, callback=self.AddPlayer2)

        dpg.set_primary_window(main_window, True)
        while dpg.is_dearpygui_running():
            # you can manually stop by using stop_dearpygui()
            self.GetScore1(self.score_group)
            self.GetScore2(self.score_group)
            self.ShowTable1(self.child_parent_1)
            self.ShowTable2(self.child_parent_2)
            dpg.render_dearpygui_frame()

        dpg.cleanup_dearpygui()
        #dpg.start_dearpygui()