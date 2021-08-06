import dearpygui.dearpygui as dpg
from src.TeamMenu import *
from src.AppClass import *
from src.SavedGames import *
import os


class MainMenu:

    def __init__(self):
        self.mainWindow = dpg.generate_uuid()
        self.gameWindow = dpg.generate_uuid()
        self.teamWindow = dpg.generate_uuid()
        self.saveWindow = dpg.generate_uuid()

        self.TeamMenu = TeamMenu()
        self.AppMenu = App()
        self.SaveMenu = SavedGames()

        self.isGameOpened = False

    def ShowGameWindow(self):
        dpg.set_viewport_title("Basketball Stat Tracker")
        dpg.set_primary_window(self.gameWindow, True)
        dpg.configure_item(item=self.gameWindow, show=True)
        dpg.configure_item(item=self.teamWindow, show=False)
        dpg.configure_item(item=self.mainWindow, show=False)
        dpg.configure_item(item=self.saveWindow, show=False)
        self.isGameOpened = True

    def ShowTeamWindow(self):
        dpg.set_viewport_title("View Teams")
        dpg.set_primary_window(self.teamWindow, True)
        dpg.configure_item(item=self.gameWindow, show=False)
        dpg.configure_item(item=self.teamWindow, show=True)
        dpg.configure_item(item=self.mainWindow, show=False)
        dpg.configure_item(item=self.saveWindow, show=False)
        self.isGameOpened = False

    def ShowMainWindow(self):
        dpg.set_viewport_title("Main Menu")
        dpg.set_primary_window(self.mainWindow, True)
        dpg.configure_item(item=self.gameWindow, show=False)
        dpg.configure_item(item=self.teamWindow, show=False)
        dpg.configure_item(item=self.mainWindow, show=True)
        dpg.configure_item(item=self.saveWindow, show=False)
        self.isGameOpened = False

    def ShowSaveWindow(self):
        dpg.set_viewport_title("View Saved Games")
        dpg.set_primary_window(self.saveWindow, True)
        dpg.configure_item(item=self.gameWindow, show=False)
        dpg.configure_item(item=self.teamWindow, show=False)
        dpg.configure_item(item=self.mainWindow, show=False)
        dpg.configure_item(item=self.saveWindow, show=True)
        self.isGameOpened = False

    def run(self):
        dpg.setup_viewport()
        dpg.set_viewport_title("Main Menu")

        with dpg.font_registry():

            title_font = dpg.add_font('Resources/Fonts/Spantaran-GE2D.ttf', 30)

        with dpg.window(label="Main Menu", id=self.mainWindow, show=True):
            dpg.add_spacing(count=20)
            dpg.add_same_line(spacing=350)
            with dpg.group():
                dpg.add_text("Welcome to Basketball Stat Tracker")
                dpg.set_item_font(item=dpg.last_item(), font=title_font)
                dpg.add_spacing(count=10)
                dpg.add_button(label="Start Game", callback=self.ShowGameWindow, width=200, indent=150)
                dpg.add_spacing(count=5)
                dpg.add_button(label="View Saved Games", callback=self.ShowSaveWindow, width=200, indent=150)
                dpg.add_spacing(count=5)
                dpg.add_button(label="View Teams", callback=self.ShowTeamWindow, width=200, indent=150)

        with dpg.window(label="View Teams", id=self.teamWindow, show=False):

            with dpg.menu_bar():
                dpg.add_menu_item(label="Back", callback=self.ShowMainWindow)
            self.TeamMenu.show()

        with dpg.window(label="Basketball Stat Tracker", id=self.gameWindow, show=False):
            with dpg.menu_bar():
                dpg.add_menu_item(label="Back", callback=self.ShowMainWindow)
            self.AppMenu.show()

        with dpg.window(label="Saved Games", id=self.saveWindow, show=False):
            with dpg.menu_bar():
                dpg.add_menu_item(label="Back", callback=self.ShowMainWindow)
            self.SaveMenu.show()

        dpg.set_primary_window(self.mainWindow, True)
        while dpg.is_dearpygui_running():

            if self.isGameOpened:
                self.AppMenu.GetScore1(self.AppMenu.score_group)
                self.AppMenu.GetScore2(self.AppMenu.score_group)
                self.AppMenu.ShowTable1(self.AppMenu.child_parent_1)
                self.AppMenu.ShowTable2(self.AppMenu.child_parent_2)
            dpg.render_dearpygui_frame()

        dpg.cleanup_dearpygui()

