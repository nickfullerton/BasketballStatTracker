'''

Player Class that will hold the players stats and percentages

'''

import dearpygui.dearpygui as dpg

class PlayerClass:

    def __init__(self, name):
        # Initialize class variables that will be unique to each player
        self.name = name
        self.ResetStats()

    def GetName(self):
        return self.name

    def MadeFG(self):
        self.points += 2
        self.fg_made += 1
        self.fg_attempts += 1

    def MissFG(self):
        self.fg_attempts += 1

    def DeleteFG(self):
        if self.points > 1 and self.fg_made > 0:
            self.points -= 2
            self.fg_made -= 1
        if self.fg_attempts > 0:
            self.fg_attempts -= 1

    def MadeFT(self):
        self.points += 1
        self.ft_made += 1
        self.ft_attempts += 1

    def MissFT(self):
        self.ft_attempts += 1

    def DeleteFT(self):
        if self.points > 0 and self.ft_made > 0:
            self.points -= 1
            self.ft_made -= 1
        if self.ft_attempts > 0:
            self.ft_attempts -= 1

    def MadeThree(self):
        self.points += 3
        self.three_made += 1
        self.three_attempts += 1
        self.fg_made += 1
        self.fg_attempts += 1

    def MissThree(self):
        self.three_attempts += 1
        self.fg_attempts += 1

    def DeleteThree(self):
        if self.points > 2 and self.three_made > 0:
            self.points -= 3
            self.three_made -= 1
            self.fg_made -= 1

        if self.three_attempts > 0:
            self.three_attempts -= 1

        if self.fg_attempts > 0:
            self.fg_attempts -= 1


    def MadeAssist(self):
        self.assists += 1

    def DeleteAssist(self):
        if self.assists > 0:
            self.assists -= 1

    def MadeRebound(self):
        self.rebounds += 1

    def DeleteRebound(self):
        if self.rebounds > 0:
            self.rebounds -= 1

    def GetPoints(self):
        return self.points

    def GetAssists(self):
        return self.assists

    def GetRebounds(self):
        return self.rebounds

    def GetFG(self):
        return self.fg_made

    def GetAttemptFG(self):
        return self.fg_attempts

    def GetFT(self):
        return self.ft_made

    def GetAttemptFT(self):
        return self.ft_attempts

    def GetThree(self):
        return self.three_made

    def GetAttemptThree(self):
        return self.three_attempts

    def GetStatLine(self):
        field_goal = f"{self.GetFG()}/{self.GetAttemptFG()}"
        free_throw = f"{self.GetFT()}/{self.GetAttemptFT()}"
        three_point = f"{self.GetThree()}/{self.GetAttemptThree()}"
        stat_line = [self.GetName(), self.GetPoints(), self.GetAssists(), self.GetRebounds(), field_goal, three_point,
                     free_throw]

        return stat_line

    def ResetStats(self):
        self.points = 0
        self.rebounds = 0
        self.assists = 0
        self.fg_made = 0
        self.fg_attempts = 0
        self.ft_made = 0
        self.ft_attempts = 0
        self.three_made = 0
        self.three_attempts = 0

    def GenerateWindow(self):
        with dpg.window(label=self.name, width=400, height=200):
            dpg.add_spacing()
            with dpg.group(horizontal=True, horizontal_spacing=5):
                dpg.add_button(label="Made FG", width=125, callback=self.MadeFG)
                dpg.add_button(label="Miss FG", width=125, callback=self.MissFG)
                dpg.add_button(label="Delete FG", width=125, callback=self.DeleteFG)
            dpg.add_spacing()
            with dpg.group(horizontal=True, horizontal_spacing=5):
                dpg.add_button(label="Made 3-FG", width=125, callback=self.MadeThree)
                dpg.add_button(label="Miss 3-FG", width=125, callback=self.MissThree)
                dpg.add_button(label="Delete 3-FG", width=125, callback=self.DeleteThree)
            dpg.add_spacing()
            with dpg.group(horizontal=True, horizontal_spacing=5):
                dpg.add_button(label="Made FT", width=125, callback=self.MadeFT)
                dpg.add_button(label="Miss FT", width=125, callback=self.MissFT)
                dpg.add_button(label="Delete FT", width=125, callback=self.DeleteFT)
            dpg.add_spacing()
            with dpg.group(horizontal=True, horizontal_spacing=5):
                dpg.add_button(label="Made Assist", width=125, callback=self.MadeAssist)
                dpg.add_button(label="Delete Assist", width=125, callback=self.DeleteAssist)
            dpg.add_spacing()
            with dpg.group(horizontal=True, horizontal_spacing=5):
                dpg.add_button(label="Made Rebound", width=125, callback=self.MadeRebound)
                dpg.add_button(label="Delete Rebound", width=125, callback=self.DeleteRebound)