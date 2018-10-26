# LTL test bench

from tkinter import *
import tkinter.font
from gpiozero import LED
from time import sleep
import RPi.GPIO as GPIO
import time
import threading
from functools import partial

LEDready = LED(26) # BLUE - Test bench is ready for use post "Reset"
LEDrunning = LED(13) # YELLOW - Test bench is running
LEDcomplete = LED(6) # GREEN - Test has been completed
LEDerror =  LED(5) # RED - Test has failed/stopped, product has failed

# start sequence
LEDready.off()
LEDrunning.off()
LEDcomplete.off()
LEDerror.off()

# Relay setup
GPIO.setmode(GPIO.BCM)
PinList = [23, 24, 25, 12, 16]
for i in PinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
    
sleep(0.1)
LEDready.on()
LEDrunning.on()
LEDcomplete.on()
LEDerror.on()
sleep(0.1)
LEDready.off()
LEDrunning.off()
LEDcomplete.off()
LEDerror.off()
sleep(0.1)
LEDerror.on()    
sleep(0.1)
LEDerror.off()
LEDcomplete.on()
sleep(0.1)
LEDcomplete.off()
LEDrunning.on()
sleep(0.1)
#LEDrunning.off()
#LEDready.on()

# window setup
win = Tk()
win.geometry("800x480")
win.title("Life Test Lab - Test Bench 1")
Font = tkinter.font.Font(family = 'Helvetica', size = 15, weight = "bold")
#Font = tkinter.font.Font(family = 'Verdana', size = 12, weight = "bold")
win.config(cursor="none")

LEDrunning.off()
LEDready.on()
# end of start sequence

# static labels
RequiredCyclesLabel =  Label(win, text = "Required Cycles:", font = Font).grid(row=0, column=0, sticky=E)
TimeONLabel = Label(win, text = "Time ON (s):", font = Font).grid(row=1, column=0, sticky=E)
TimeOFFLabel = Label(win, text = "Time OFF (s):", font = Font).grid(row=2, column=0, sticky=E)
CyclesCompleteLabel = Label(win, text = "Cycles Complete:", font = Font).grid(row=0, column=2, sticky=E)
PercentCompleteLabel = Label(win, text = "% Complete:", font = Font).grid(row=1, column=2, sticky=E)
TimeRemainingLabel = Label(win, text = "Time Remaining:", font = Font).grid(row=2, column=2, sticky=E)
StatusLabel = Label(win, text = "Status:", font = Font).grid(row=5, column=2, sticky=E)
LogPowerLabel = Label(win, text = "Log Power", font = Font).grid(row=0, column=4, sticky=S)
LogTempLabel = Label(win, text = "Log Temperature", font = Font).grid(row=0, column=5, sticky=S)
CycleState = Label(win, text="Cycle:", font=Font).grid(row=3, column=2, sticky=E)

# dynamic labels
global StatusText
StatusText = StringVar()
StatusText.set("READY")
Label(win, textvariable=StatusText, font=Font, fg="blue").grid(row=5, column=3, sticky=W)
global CyclesCompleted
CyclesCompleted = IntVar()
CyclesCompleted.set(0)
Label(win, textvariable=CyclesCompleted, font=Font, fg="blue").grid(row=0, column=3, sticky=W)


# text entry fields
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
RequiredCyclesEntry = Entry(win, width=6, justify=LEFT, textvariable=var1).grid(row=0, column=1)
TimeONEntry = Entry(win, width=6, justify=LEFT, textvariable=var2).grid(row=1, column=1)
TimeOFFEntry = Entry(win, width=6, justify=LEFT, textvariable=var3).grid(row=2, column=1)
'''
# popup Keypad code unfinished

RequiredCyclesEntry.bind('<Button-1>', run)

# KEYPAD
num_run = 0
btn_funcid = 0

def click(btn):
    global num_run
    text = "%s" % btn
    if not text == "Clear" and not text == "OK":
        RequiredCyclesEntry.insert(END, text)
    if text == 'Clear':
        RequiredCyclesEntry.delete(0, END)
    if text == 'OK':
        boot.destroy()
        num_run = 0
        win.unbind('<Button-1>', btn_funcid)


def numpad():
    global num_run, boot
    boot = tk.Tk()
    boot['bg'] = 'white'
    lf = tk.LabelFrame(boot, text=" keypad ", bd=3)
    lf.pack(padx=0, pady=0)
    btn_list = [
        '7',  '8',  '9',
        '4',  '5',  '6',
        '1',  '2',  '3',
        '0',  'Clear',  'OK']
    r = 1
    c = 0
    n = 0
    btn = list(range(len(btn_list)))
    for label in btn_list:
        cmd = partial(click, label)
        btn[n] = tk.Button(lf, text=label, width=10, height=5, command=cmd)
        btn[n].grid(row=r, column=c)
        n += 1
        c += 1
        if c == 3:
            c = 0
            r += 1


def close(event):
    global num_run, btn_funcid
    if num_run == 1:
        boot.destroy()
        num_run = 0
        win.unbind('<Button-1>', btn_funcid)


def run(event):
    global num_run, btn_funcid
    if num_run == 0:
        num_run = 1
        numpad()
        btn_funcid = win.bind('<Button-1>', close)


#e = Entry(root, width=10, background='white', textvariable=file, justify=CENTER, font='-weight bold')
#e = Entry(root, width=10, background='white', justify=RIGHT, font='-weight bold')

#e.bind('<Button-1>', run)


#e.grid(padx=10, pady=5, row=17, column=1, sticky='W,E,N,S')

win.mainloop()
'''
# Globals
TestRunning = False
ApowerLogging = False
BpowerLogging = False
CpowerLogging = False
DpowerLogging = False
EpowerLogging = False
Temp1Logging = False
Temp2Logging = False
Temp3Logging = False
Temp4Logging = False
Temp5Logging = False
Temp6Logging = False
Temp7Logging = False
Temp8Logging = False
Temp9Logging = False
Temp10Logging = False
#CycleCount = 0

# buttons
ButtonColourON = "white"
ButtonColourOFF = "grey"

def STARTSTOP():
    global TestRunning
    if TestRunning == True:
        
        for i in PinList:
            GPIO.output(i, GPIO.HIGH)
            
        LEDrunning.off()
        LEDerror.on()
        sleep(0.1)
        LEDerror.off()
        LEDcomplete.off()
        LEDready.on()
        STARTSTOPbutton["text"] = "START TEST"
        STARTSTOPbutton["bg"] = "green"
        STARTSTOPbutton["activebackground"] = "green"
        StatusText.set("READY")
        TestRunning = False
        print("Stopped Test")
    else:
        LEDrunning.on()
        LEDready.off()
        RequiredCycles = var1.get()
        TimeONs = var2.get()
        TimeOFFs = var3.get()
        print(TimeONs)
        print(TimeOFFs)
        #CycleCount = 0
        STARTSTOPbutton["text"] = "STOP TEST"
        STARTSTOPbutton["bg"] = "red"
        STARTSTOPbutton["activebackground"] = "red"
        StatusText.set("RUNNING")
        TestRunning = True
        thread = threading.Thread(target=RunTest, args = (RequiredCycles, TimeONs, TimeOFFs))
        thread.start()
        print("Started Test")
        
STARTSTOPbutton = Button(win, text="START TEST", font=Font, command=STARTSTOP, bg="green", fg="white", activebackground="green", activeforeground="white", height=1, width=10)
STARTSTOPbutton.grid(row=3, column=0)


def Apower():
    global ApowerLogging
    if ApowerLogging == True:
        Apowerbutton["bg"] = ButtonColourOFF
        Apowerbutton["activebackground"] = ButtonColourOFF
        ApowerLogging = False
        print("Stopped reading power from product A")
    else:
        Apowerbutton["bg"] = ButtonColourON
        Apowerbutton["activebackground"] = ButtonColourON
        ApowerLogging = True
        print("Started reading power from product A")

Apowerbutton = Button(win, text="Product A", font=Font, command=Apower, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Apowerbutton.grid(row=1, column=4)

def Bpower():
    global BpowerLogging
    if BpowerLogging == True:
        Bpowerbutton["bg"] = ButtonColourOFF
        Bpowerbutton["activebackground"] = ButtonColourOFF
        BpowerLogging = False
        print("Stopped reading power from product B")
    else:
        Bpowerbutton["bg"] = ButtonColourON
        Bpowerbutton["activebackground"] = ButtonColourON
        BpowerLogging = True
        print("Started reading power from product B")

Bpowerbutton = Button(win, text="Product B", font=Font, command=Bpower, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Bpowerbutton.grid(row=2, column=4)

def Cpower():
    global CpowerLogging
    if CpowerLogging == True:
        Cpowerbutton["bg"] = ButtonColourOFF
        Cpowerbutton["activebackground"] = ButtonColourOFF
        CpowerLogging = False
        print("Stopped reading power from product C")
    else:
        Cpowerbutton["bg"] = ButtonColourON
        Cpowerbutton["activebackground"] = ButtonColourON
        CpowerLogging = True
        print("Started reading power from product C")

Cpowerbutton = Button(win, text="Product C", font=Font, command=Cpower, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Cpowerbutton.grid(row=3, column=4)

def Dpower():
    global DpowerLogging
    if DpowerLogging == True:
        Dpowerbutton["bg"] = ButtonColourOFF
        Dpowerbutton["activebackground"] = ButtonColourOFF
        DpowerLogging = False
        print("Stopped reading power from product D")
    else:
        Dpowerbutton["bg"] = ButtonColourON
        Dpowerbutton["activebackground"] = ButtonColourON
        DpowerLogging = True
        print("Started reading power from product D")

Dpowerbutton = Button(win, text="Product D", font=Font, command=Dpower, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Dpowerbutton.grid(row=4, column=4)

def Epower():
    global EpowerLogging
    if EpowerLogging == True:
        Epowerbutton["bg"] = ButtonColourOFF
        Epowerbutton["activebackground"] = ButtonColourOFF
        EpowerLogging = False
        print("Stopped reading power from product E")
    else:
        Epowerbutton["bg"] = ButtonColourON
        Epowerbutton["activebackground"] = ButtonColourON
        EpowerLogging = True
        print("Started reading power from product E")

Epowerbutton = Button(win, text="Product E", font=Font, command=Epower, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Epowerbutton.grid(row=5, column=4)

def Temp1():
    global Temp1Logging
    if Temp1Logging == True:
        Temp1button["bg"] = ButtonColourOFF
        Temp1button["activebackground"] = ButtonColourOFF
        Temp1Logging = False
        print("Stopped reading temp from sensor 1")
    else:
        Temp1button["bg"] = ButtonColourON
        Temp1button["activebackground"] = ButtonColourON
        Temp1Logging = True
        print("Started reading temp from sensor 1")

Temp1button = Button(win, text="Sensor 1", font=Font, command=Temp1, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Temp1button.grid(row=1, column=5)

def Temp2():
    global Temp2Logging
    if Temp2Logging == True:
        Temp2button["bg"] = ButtonColourOFF
        Temp2button["activebackground"] = ButtonColourOFF
        Temp2Logging = False
        print("Stopped reading temp from sensor 2")
    else:
        Temp2button["bg"] = ButtonColourON
        Temp2button["activebackground"] = ButtonColourON
        Temp2Logging = True
        print("Started reading temp from sensor 2")

Temp2button = Button(win, text="Sensor 2", font=Font, command=Temp2, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Temp2button.grid(row=2, column=5)

def Temp3():
    global Temp3Logging
    if Temp3Logging == True:
        Temp3button["bg"] = ButtonColourOFF
        Temp3button["activebackground"] = ButtonColourOFF
        Temp3Logging = False
        print("Stopped reading temp from sensor 3")
    else:
        Temp3button["bg"] = ButtonColourON
        Temp3button["activebackground"] = ButtonColourON
        Temp3Logging = True
        print("Started reading temp from sensor 3")

Temp3button = Button(win, text="Sensor 3", font=Font, command=Temp3, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Temp3button.grid(row=3, column=5)

def Temp4():
    global Temp4Logging
    if Temp4Logging == True:
        Temp4button["bg"] = ButtonColourOFF
        Temp4button["activebackground"] = ButtonColourOFF
        Temp4Logging = False
        print("Stopped reading temp from sensor 4")
    else:
        Temp4button["bg"] = ButtonColourON
        Temp4button["activebackground"] = ButtonColourON
        Temp4Logging = True
        print("Started reading temp from sensor 4")

Temp4button = Button(win, text="Sensor 4", font=Font, command=Temp4, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Temp4button.grid(row=4, column=5)

def Temp5():
    global Temp5Logging
    if Temp5Logging == True:
        Temp5button["bg"] = ButtonColourOFF
        Temp5button["activebackground"] = ButtonColourOFF
        Temp5Logging = False
        print("Stopped reading temp from sensor 5")
    else:
        Temp5button["bg"] = ButtonColourON
        Temp5button["activebackground"] = ButtonColourON
        Temp5Logging = True
        print("Started reading temp from sensor 5")

Temp5button = Button(win, text="Sensor 5", font=Font, command=Temp5, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Temp5button.grid(row=5, column=5)

def Temp6():
    global Temp6Logging
    if Temp6Logging == True:
        Temp6button["bg"] = ButtonColourOFF
        Temp6button["activebackground"] = ButtonColourOFF
        Temp6Logging = False
        print("Stopped reading temp from sensor 6")
    else:
        Temp6button["bg"] = ButtonColourON
        Temp6button["activebackground"] = ButtonColourON
        Temp6Logging = True
        print("Started reading temp from sensor 6")

Temp6button = Button(win, text="Sensor 6", font=Font, command=Temp6, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Temp6button.grid(row=6, column=5)

def Temp7():
    global Temp7Logging
    if Temp7Logging == True:
        Temp7button["bg"] = ButtonColourOFF
        Temp7button["activebackground"] = ButtonColourOFF
        Temp7Logging = False
        print("Stopped reading temp from sensor 7")
    else:
        Temp7button["bg"] = ButtonColourON
        Temp7button["activebackground"] = ButtonColourON
        Temp7Logging = True
        print("Started reading temp from sensor 7")

Temp7button = Button(win, text="Sensor 7", font=Font, command=Temp7, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Temp7button.grid(row=7, column=5)

def Temp8():
    global Temp8Logging
    if Temp8Logging == True:
        Temp8button["bg"] = ButtonColourOFF
        Temp8button["activebackground"] = ButtonColourOFF
        Temp8Logging = False
        print("Stopped reading temp from sensor 8")
    else:
        Temp8button["bg"] = ButtonColourON
        Temp8button["activebackground"] = ButtonColourON
        Temp8Logging = True
        print("Started reading temp from sensor 8")

Temp8button = Button(win, text="Sensor 8", font=Font, command=Temp8, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Temp8button.grid(row=8, column=5)

def Temp9():
    global Temp9Logging
    if Temp9Logging == True:
        Temp9button["bg"] = ButtonColourOFF
        Temp9button["activebackground"] = ButtonColourOFF
        Temp9Logging = False
        print("Stopped reading temp from sensor 9")
    else:
        Temp9button["bg"] = ButtonColourON
        Temp9button["activebackground"] = ButtonColourON
        Temp9Logging = True
        print("Started reading temp from sensor 9")

Temp9button = Button(win, text="Sensor 9", font=Font, command=Temp9, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Temp9button.grid(row=9, column=5)

def Temp10():
    global Temp10Logging
    if Temp10Logging == True:
        Temp10button["bg"] = ButtonColourOFF
        Temp10button["activebackground"] = ButtonColourOFF
        Temp10Logging = False
        print("Stopped reading temp from sensor 10")
    else:
        Temp10button["bg"] = ButtonColourON
        Temp10button["activebackground"] = ButtonColourON
        Temp10Logging = True
        print("Started reading temp from sensor 10")

Temp10button = Button(win, text="Sensor 10", font=Font, command=Temp10, bg=ButtonColourOFF, activebackground=ButtonColourOFF, height=1, width=10)
Temp10button.grid(row=10, column=5)

# output labels TEMPORARY
#StatusText = "COMPLETE"
#Status = StringVar()
#Status.set('READY')
#CyclesCompleteOP = Label(win, text="12345", font=Font, fg="blue").grid(row=0, column=3, sticky=W)
PercentCompleteOP = Label(win, text="50%", font=Font, fg="blue").grid(row=1, column=3, sticky=W)
TimeRemainingOP = Label(win, text="24 hours", font=Font, fg="blue").grid(row=2, column=3, sticky=W)
CycleStateOP = Label(win, text="10s ON", font=Font, fg="blue").grid(row=3, column=3, sticky=W)
#StatusOP = Label(win, text=Status, font=Font, fg="blue").grid(row=5, column=3, sticky=W)
#StatusOP = Label(win, text="READY", font=Font, fg="blue").grid(row=5, column=3, sticky=W)

def RESET():
    print("Reset")
    global TestRunning
    global ApowerLogging
    global BpowerLogging
    global CpowerLogging
    global DpowerLogging
    global EpowerLogging
    global Temp1Logging
    global Temp2Logging
    global Temp3Logging
    global Temp4Logging
    global Temp5Logging
    global Temp6Logging
    global Temp7Logging
    global Temp8Logging
    global Temp9Logging
    global Temp10Logging
    TestRunning = False
    LEDrunning.off()
    LEDready.on()
    ApowerLogging = False
    BpowerLogging = False
    CpowerLogging = False
    DpowerLogging = False
    EpowerLogging = False
    Temp1Logging = False
    Temp2Logging = False
    Temp3Logging = False
    Temp4Logging = False
    Temp5Logging = False
    Temp6Logging = False
    Temp7Logging = False
    Temp8Logging = False
    Temp9Logging = False
    Temp10Logging = False
    STARTSTOPbutton["bg"] = "green"
    STARTSTOPbutton["text"] = "START TEST"
    Apowerbutton["bg"] = ButtonColourOFF
    Bpowerbutton["bg"] = ButtonColourOFF
    Cpowerbutton["bg"] = ButtonColourOFF
    Dpowerbutton["bg"] = ButtonColourOFF
    Epowerbutton["bg"] = ButtonColourOFF
    Temp1button["bg"] = ButtonColourOFF
    Temp2button["bg"] = ButtonColourOFF
    Temp3button["bg"] = ButtonColourOFF
    Temp4button["bg"] = ButtonColourOFF
    Temp5button["bg"] = ButtonColourOFF
    Temp6button["bg"] = ButtonColourOFF
    Temp7button["bg"] = ButtonColourOFF
    Temp8button["bg"] = ButtonColourOFF
    Temp9button["bg"] = ButtonColourOFF
    Temp10button["bg"] = ButtonColourOFF
    var1.set(0)
    var2.set(0)
    var3.set(0)

    for i in PinList:
            GPIO.output(i, GPIO.HIGH)
            
    # ADD CODE TO RESET OUTPUT LABELS
    
RESETbutton = Button(win, text="Reset", font=Font, command=RESET, bg="black", fg="white", activebackground="black", activeforeground="white", height=1, width=4)
RESETbutton.grid(row=5, column=0)

def COMPLETE(StatusText):
    for i in PinList:
            GPIO.output(i, GPIO.HIGH)

    
    #global Status
    #Status.set("COMPLETE")
    #StatusOP['text'] = "COMPLETE"
    #StatusOP.config(text=Status)
    LEDrunning.off()
    LEDcomplete.on()
    StatusText.set("COMPLETE")
    TestRunning = False
    print("Stopped Test")

print("Starting")

def RunTest(RequiredCycles, TimeONs, TimeOFFs):
    print("in runtest")
    global CycleCount
    CycleCount = 0
    while True:
        CyclesRemaining = RequiredCycles - CycleCount
        if TestRunning == False:
            break
        if RequiredCycles == CycleCount:
            COMPLETE(StatusText)
            break
        if TestRunning == True:
            GPIO.output(16, GPIO.LOW)
            sleep(TimeONs)
            GPIO.output(16, GPIO.HIGH)
            sleep(TimeOFFs)
            CycleCount = CycleCount + 1
            print(CycleCount)
            global CyclesCompleted
            CyclesCompleted.set(CycleCount)
            

