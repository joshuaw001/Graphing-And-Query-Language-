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
            for item in ["query","function","name","commType"]:
                if item == "query":
                   self.query = configs.query
                elif item == "fn":
                    self.fn = configs.fn
                elif item == "name":
                    self.name = configs.name
                elif item == "commType":
                    if configs.commType in ["action","getter","setter"]:
                        self.commType = configs.commType
                    else:
                        return "FAIL"
                else:
                    return "FAIL"
