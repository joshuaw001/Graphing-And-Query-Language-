import random
import math
import turtle
import sqlite3
def blank():
    pass

class Command:
    self.query = ""
    self.fn    = blank()
    self.commType = "action"
    self.name     = "blank_script"
    def __init__(q,f,n):
        self.query = q
        self.fn    = f
        self.name  = n
    
    def config(**configs):
        for item in configs.keys():
            if item in ["query","function","name","commType"]:
                


