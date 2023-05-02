import sys
import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

class UiModulOOPC():
    def __init__(self):
        self.isActive = False
        self.formWindow = tk.Tk()
        self.formWindow.title('Ubuntessa')
        #self.historyCommand = historyCommand
        self.frame_list = tk.Frame(self.formWindow, height=800, width=800)
        self.frame_list.pack()
        self.headerForTable = ['Иторсия команд']
        self.treeviewOperationHistory = ttk.Treeview(self.frame_list)
        self.treeviewOperationHistory['show'] = 'headings'
        self.treeviewOperationHistory['columns'] = self.headerForTable
    def CreateWindow(self, data):
        self.isActive = True
        TkTrue = True
        #print(data)
        treeviewinfo = []
        #treeviewinfoStr = ''
        for commands in data:
            newData = []
            #treeviewinfoStr += " " + str(commands)
            #treeviewinfo.append(treeviewinfoStr)
            #treeviewinfo.append(commands)
            newData.append(commands)
            treeviewinfo.append(newData)
        #print(treeviewinfo)
        for header in self.headerForTable:
            self.treeviewOperationHistory.heading(header, text=header, anchor='center')
        for row in treeviewinfo:
            self.treeviewOperationHistory.insert('', tk.END, values=row)
        self.treeviewOperationHistory.pack(expand=tk.YES, fill=tk.BOTH)
        while(TkTrue):
            self.formWindow.update()    
            TkTrue = False
    def UpdateWindow(self, newData):
        TkTrue = True
        print(newData)
        newTreeInfo = []
        for child in self.treeviewOperationHistory.get_children():
            self.treeviewOperationHistory.delete(child)
        for commands in newData:
            sData = []
            sData.append(commands)
            newTreeInfo.append(sData)
        print(newTreeInfo)
        for row in newTreeInfo:
            self.treeviewOperationHistory.insert('', tk.END, values=row)
        while(TkTrue):
            self.formWindow.update()    
            TkTrue = False
    def GetActivity(self):
        return self.isActive
    def SayGoodbye(self):
        messagebox.showinfo("Завершение Работы", "До новых встреч!")
        time.sleep(1)
        sys.exit()
        
