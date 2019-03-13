from tkinter import *
from alpha_vantage_api import AlphaVantageAPI
import pandas



class MarketViewer(object):

    def __init__(self):

        api_key = "demo"
        self.api = AlphaVantageAPI(api_key=api_key)
        self.gui = Tk()
        self.gui.title("Market Viewer")
        self.calc_text = Label(self.gui, text=self.text, bd=1, relief=SUNKEN, anchor=N)
        self.calc_text.grid(column=1, columnspan=8, row=0)
        self.frame = Frame(self.gui, width=600, height=1800)
        self.gui.mainloop()







