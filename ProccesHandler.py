import asyncio
import os
import sys
import time
import subprocess
import alsaaudio
from threading import *
from multiprocessing import Pool
from microphoneTest import Degenerator
from uiModul import uiModul
from uiModulOOP import UiModulOOPC
from audioSpeecherOOP import AuidoSpeecher

class CommandHandler():
    def __init__(self):
        self.commandQueue = [
        ]
        self.historyOperations = []
        self.commandWithIDs = {
            'открой терминал': 10,
            'выключи звук': 20,
            'выключить звук': 20,
            'включи звук': 21,
            'включить звук': 21,
            'покажи файлы': 30,
            'создай папку': 31,
            'создай файл': 32,
            'заверши программу' : 40
        }
        #loop = asyncio.get_event_loop()
        #tasks = []
        self.uiModulObj = UiModulOOPC()
        self.audioSpeecherObj = AuidoSpeecher()
    def TreahdUi(self, historyCommand, exit):
    #UI = Thread(target=uiModul(historyCommand))
        if(exit):
            UI = Thread(target=self.uiModulObj.SayGoodbye())
        else:
            if(self.uiModulObj.GetActivity()):
                print("TRUE")
                UI = Thread(target=self.uiModulObj.UpdateWindow(historyCommand))
            else: 
                print("ELSE")
                UI = Thread(target=self.uiModulObj.CreateWindow(historyCommand))
        UI.start()
    def ParseCommand(self, command):
        commandOut = []
        out = command.split(" ")
        for pos in range(0, 4):
            out[pos] = ""
        out[-1] = out[-1].replace('}', '')
        out[-1] = out[-1].replace('\n', '')     
        for words in out:
            if(len(words) > 0):
                words = words.replace('\"', '')    
                commandOut.append(words)
        return commandOut
    
    def StartCommand(self, idCommand, optionalName):
        if (idCommand == 10):
            #os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
            os.system("gnome-terminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
        if (idCommand == 20):
            mix = alsaaudio.Mixer() # инициализируем объект микшера
            vol = mix.getvolume() # получили текущую громкость
            mix.setvolume(0) # - установим громкость 0
            
        if (idCommand == 21):
            mix = alsaaudio.Mixer() # инициализируем объект микшера
            vol = mix.getvolume() # получили текущую громкость
            mix.setvolume(100) # - установим громкость 100
            
        if (idCommand == 30):
            command = "ls" 
            res = subprocess.call(command, shell = True) 
            print("Returned Value: ", res)
            
        if (idCommand == 31):
            command = "mkdir " + str(optionalName) 
            res = subprocess.call(command, shell = True) 
            print("Returned Value: ", res)
            
        if (idCommand == 32):
            command = "touch " + str(optionalName) 
            res = subprocess.call(command, shell = True) 
            print("Returned Value: ", res)

        if(idCommand == 40):
            #time.sleep(1)
            #sys.exit()
            print("Good Bye")

    def FindCommand(self):
        optiName = ''
        commandToFind = ''
        if (self.commandQueue[0][0] == 'создай'):
            optiName = self.commandQueue[0][-1]
            self.commandQueue[0][-1] = ''
        for word in self.commandQueue[0]:
            commandToFind = commandToFind + " " + word
        commandToFind = commandToFind.strip()
        #print("CommandToFind " + commandToFind)
        #print("OptiName " + optiName)
        idCom = self.commandWithIDs.get(commandToFind)
        if (idCom == None):
            print('Комманда не распознана')
        else:
            if(idCom == 40):
                self.TreahdUi(self.historyOperations, True)
                self.StartCommand(idCom, optiName)
            else:
                self.StartCommand(idCom, optiName)
        #print(commandToFind)
        #print(commandToFind)
        self.historyOperations.append(commandToFind)
        #uiModul(historyOperations)
        #currentUiWindow = asyncio.create_task(AncStsyrartUI(historyOperations))
        #tasks.append(loop.create_task(AsyncStrartUI(historyOperations)))
        #loop.run_until_complete(asyncio.wait(tasks))
        #ProccesStrartUI(historyOperations)
        self.TreahdUi(self.historyOperations, False)
        #asyncio.run(currentUiWindow)
        self.commandQueue.pop(0)

    def StartProggram(self):
        for command in self.audioSpeecherObj.Degenerator():
            inCommand = self.ParseCommand(command)
            #print(inCommand)
            if(inCommand[0] == 'компьютер'):
                inCommand.pop(0)
                if(len(inCommand) > 0):
                    self.commandQueue.append(inCommand)
                    self.FindCommand()