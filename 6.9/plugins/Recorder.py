# Created by: Storm Shadow http://www.techbliss.org

# WARNING! All changes made in this file will be lost!
import re
import idaapi
import idc
from idc import *
from idaapi import *
import sys
sys.path.insert(0 , idaapi.idadir("plugins\\recorder\\icons"))
import ico
from ico import *
class hawk(idaapi.plugin_t):
    flags = idaapi.PLUGIN_FIX
    comment = "This is a comment"

    help = "Screen Recorder"
    wanted_name = "Screen Recorder"
    wanted_hotkey = "Shift-R"



    def init(self):
        idaapi.msg("Screen Recorder Is Found Use Shift-R to load to menu \n")
        return idaapi.PLUGIN_OK


    def run(self, arg):
        idaapi.msg("run() called with %d!\n" % arg)

    def term(self):
        idaapi.msg("")



    def AddMenuElements(self):
        idaapi.add_menu_item("File/", "Screen Recorder", "Shift-R", 0, self.eyes, ())
        idaapi.set_menu_item_icon("File/Screen Recorder", idaapi.load_custom_icon(":/ico/python.png"))




    def run(self, arg = 0):
        idaapi.msg("Screen Recorder Loaded to File menu use Shift-R once more to run")
        self.AddMenuElements()

    def eyes(self):
        g = globals()
        idahome = idaapi.idadir("plugins\\recorder")
        IDAPython_ExecScript(idahome +  "\\rec_main.py", g)




def PLUGIN_ENTRY():
    return hawk()