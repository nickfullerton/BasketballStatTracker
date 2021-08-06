import dearpygui.dearpygui as dpg


class SavedGames:

    def __init__(self):
        self.mainGroup = dpg.generate_uuid()

    def show(self):

        with dpg.group(id=self.mainGroup):
            dpg.add_spacing(count=5)
            dpg.add_text("No Saved Games")
