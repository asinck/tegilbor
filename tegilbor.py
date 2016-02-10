#Adam Sinck

#This was originally a text editor I wrote for fun, and to see if I
#could. I have expanded it to be able to accept a lot of key bindings,
#so that I could type with shorthand. The original editor is at
#https://github.com/asinck/amdiron .

#this is a list of import commands. If the user doesn't have Tkinter
#or other libraries installed, it will fail gracefully instead of
#crashing.
imports = [
    "from Tkinter import *",
    "import Tkinter as tk",
    "import tkMessageBox",
    "from ScrolledText import ScrolledText",
    "from keybindings import *",
    "import hashlib",
    "import time",
    "import random"
]
#failedPackages will keep a record of the names of the packages that
#failed to import, so that the program can go through the entire list
#of packages that it wants to import. This will allow the program to
#give the user a complete list of packages that they need to install,
#instead of only telling the user one at a time.
failedPackages = ''
for i in imports:
    try:
        exec(i)
    except ImportError as error:
        failedPackages += str(error) + '\n'
#if there were any errors in the imports, tell the users what packages
#didn't import, and exit.
if len(failedPackages) > 0:
    print "Some packages could not be imported:"
    print failedPackages
    exit()

#global variables
currentTab = "Untitled 1" #this is the name of the initial tab
openDocuments = {}        #a hash table of documents
tabs = {}                 #a hash table of the tabs that will allow the
unnamedDocs = 1           #user to have multiple tabs open at once
quickDefs = {}


#functions

#notDone will give a message saying that that feature is not complete
def notDone(var=None):
    tkMessageBox.showinfo("Not Ready", "This feature is not complete yet.")

#this will pop up a dialog box for user input
def popup(title, message, proceed, cancel, command, inputWidth=30):
    functionA = lambda: removePopup(userDialog, command, userInput.get())
    functionB = lambda(n): removePopup(userDialog, command, userInput.get())
    userDialog = tk.Toplevel()
    userDialog.title(title)
    label = Label(userDialog, text = message)
    userInput = Entry(userDialog, width = inputWidth)
    submit = Button(userDialog, text = proceed)
    submit.config(command=functionA)
    cancel = Button(userDialog, text=cancel, command = userDialog.destroy)
    label.pack()
    userInput.pack()
    submit.pack(side=RIGHT)
    cancel.pack(side=RIGHT)
    userInput.focus_set()
    userInput.bind("<Escape>", lambda(nothing): destroyThis(userDialog))
    userInput.bind("<Return>", functionB)

#this will kill the popup window and return the value it died with
def removePopup(window, command, value):
    window.destroy()
    command(value)

#this will remove any window given to it
def destroyThis(window):
    window.destroy()

#this will check to see if the current tab has been edited
def currentTabIsUnedited():
    return openDocuments[currentTab].get(1.0, END) == '\n'

#this is used for switching tabs
def edit(tabName, sameTab=False):
    global currentTab
    openDocuments[currentTab].pack_forget()
    openDocuments[tabName].pack(fill = BOTH, expand=YES)
    root.title(tabName + " - Tegilbor Speed Text Editor")
    currentTab = tabName

#make a new document
def openFile():
    popup("Open File", "What is the file name?", "Open", "Cancel", openAFile)

#this opens a file and allows the user to edit it
def openAFile(fileName):
    if fileName in tabs:
        tkMessageBox.showerror("Error", "This file is already open.")
        return
    try:
        text = open(fileName)
        s = ''
        for i in text:
            s += i
        text.close()
        if currentTabIsUnedited():
            #edit the current tab
            #change the display name of the current tab
            tabs[currentTab].configure(text = fileName)
            #make the command of the current tab be to edit the document with
            #the filename
            tabs[currentTab].configure(command = lambda: edit(fileName))
            #make a new entry in tabs, and make it point to the current tab
            #this makes it so that the key that points to the tab matches
            #the filename
            tabs[fileName] = tabs[currentTab]
            del tabs[currentTab]
            #put the file in the document area
            openDocuments[fileName] = ScrolledText(mainFrame, wrap=WORD)
            #Text(mainFrame, height=28, width=80)
            edit(fileName, True)
            openDocuments[fileName].insert(END, s)
            tabs[fileName].configure(bg = "#FFF")
            
        else:
            #make a new tab
            tabs[fileName] = (Button(tabsFrame, text = fileName))
            tabs[fileName].configure(command = lambda: edit(fileName))
            tabs[fileName].pack(side=LEFT)
            #put the file in the document area
            openDocuments[fileName] = ScrolledText(mainFrame, wrap=WORD)
            #Text(mainFrame, height=28, width=80)
            edit(fileName)
            openDocuments[fileName].insert(END, s)
            tabs[fileName].configure(bg = "#FFF")
        
    except:
        s = 'The file "' + fileName + '" cannot be opened.'
        tkMessageBox.showerror("Error", s)
    
#this saves the current tab's contents
def save(var=None):
    text = open(currentTab, 'w')
    contents = openDocuments[currentTab].get(1.0, END)
    text.write(contents)
    tabs[currentTab].configure(bg = "#FFF")
#this pops up a message to the user when the close the program,
#reminding them to save everything.
def warn():
    if tkMessageBox.askokcancel("Save?", "Have you saved everything?"):
        root.destroy()


#this pops up a window for saving a document with a different name
def saveAs(var=None):
    popup("Save As", "What is the new file name?", "Save", "Cancel", saveAsThis)

#this does the saving part of the save as
def saveAsThis(fileName):
    global currentTab, unnamedDocs
    #get the file name to save as; if it exists make sure that the user
    #meant to save the file with that name
    if (fileName == ""):
        tkMessageBox.showerror("Error", "Invalid file name.")
        return
    try:
        text = open(fileName, 'r')
        message = "This file already exists. Save anyway?"
        answer = tkMessageBox.askyesno("Error", message)
        if not answer:
            return
    except:
        pass
    if currentTab[0:8] == "Untitled":
        unnamedDocs -= 1
    
    #rename the current tab and make sure that it points at the right file
    tabs[fileName] = tabs[currentTab]
    del tabs[currentTab]
    tabs[fileName].configure(text = fileName)
    tabs[fileName].configure(command = lambda: edit(fileName))
    #rename the current document's key
    openDocuments[fileName] = openDocuments[currentTab]
    del openDocuments[currentTab]
    #update currentTab
    currentTab = fileName
    #write to file
    text = open(fileName, 'w+')
    contents = openDocuments[fileName].get(1.0, END)
    text.write(contents)
    root.title(currentTab + " - Tegilbor Speed Text Editor")
    tabs[currentTab].configure(bg = "#FFF")

#this opens a new document
def newDoc(var=None):
    global currentTab, unnamedDocs
    unnamedDocs += 1
    s = "Untitled " + str(unnamedDocs)
    
    #make a tab
    tabs[s] = (Button(tabsFrame, text = s))
    tabs[s].configure(command = lambda: edit(s))
    tabs[s].pack(side=LEFT)
    
    #make the document
    openDocuments[s] = ScrolledText(mainFrame, wrap=WORD)#, height=28, width=80)
    
    edit(s)
    currentTab = s
    tabs[currentTab].configure(bg = "#FFF")

#this makes a new quick def
def makeQuickDef(frame):
    myFrame = Frame(frame)
    left = Frame(myFrame)
    right = Frame(myFrame)

    #in left
    myLeftFrame = Frame(left)
    myRightFrame = Frame(left)
    
    keyLabel = Label(myLeftFrame, text = "Key")
    keyEntry = Entry(myLeftFrame, width = 2)
    keyEntry.bind("<Return>", lambda x: quickDef(keyEntry.get(), wordEntry.get()))
    colon = Label(left, text = "\n:")
    wordLabel = Label(myRightFrame, text = "Word")
    wordEntry = Entry(myRightFrame, width = 7)
    wordEntry.bind("<Return>", lambda x: quickDef(keyEntry.get(), wordEntry.get()))

    #in right
    def close():
        myFrame.pack_forget()
        deleteQuickDef(keyEntry.get())
    
    closeButton = Button(right, text = "[X]", command = lambda: close())
    addButton = Button(right, text = "[+]", command = lambda: quickDef(keyEntry.get(), wordEntry.get()))

    #pack
    myFrame.pack()
    left.pack(side=LEFT)
    right.pack(side=RIGHT)

    myLeftFrame.pack(side=LEFT)
    colon.pack(side=LEFT)
    myRightFrame.pack(side=LEFT)

    keyLabel.pack(side=TOP)
    keyEntry.pack(side=BOTTOM)
    wordLabel.pack(side=TOP)
    wordEntry.pack(side=BOTTOM)

    closeButton.pack(side=TOP)
    addButton.pack(side=BOTTOM)

    addQuickDef.pack_forget()
    addQuickDef.pack(side=BOTTOM)
    
    keyEntry.focus_set()

#this defines a new quickdef, or redefines an existing quickdef
def quickDef(key, word):
    quickDefs[key] = word
    textEntry.focus_set()

#this deletes a quickdef, if possible
def deleteQuickDef(key):
    try:
        del quickDefs[key]
    except:
        print key + " not found."

#this does the auto-replace of quickdefs
def findQuickDef(key):
    global currentTab
    try:
        word = quickDefs[key]
        openDocuments[currentTab].delete("%s-2c" % INSERT, INSERT)
        insert(word)
    except:
        print "Key not found."

#this lets the user look up a binding
def lookup():
    global currentTab
    string = quickDefLookupEntry.get()
    quickDefLookupEntry.delete(0, 'end')
    textEntry.focus_set()
    results = []
    if (string != ''):
        for key in bindings:
            if (string in bindings[key]):
                s = key + " " + bindings[key]
                results.append(s)
        results = sorted(results, key=len)
    lookupLabel.config(text='\n'.join(results))
    openDocuments[currentTab].see("end")
    
#this is a ctrl-backspace (delete previous word)
def deleteWord(var=None):
    global lastLen, currentTab
    lastLen = 1
    char = '-'
    while char not in " _\n.,":
        openDocuments[currentTab].delete("%s-1c" % INSERT, INSERT)
        char = openDocuments[currentTab].get("%s-1c" % INSERT, INSERT)

#this adds special functionality to backspace, so that it deletes the
#last insertion, instead of the last character. This is helpful when you
#typo a binding.
def backspace(var=None):
    global lastLen, currentTab
    for i in range(lastLen):
        openDocuments[currentTab].delete("%s-1c" % INSERT, INSERT)
    lastLen = 1
    
#this does the insertion into the editor window.
def insert(string):
    global lastLen, currentTab
    lastLen = len(string)
    tabs[currentTab].configure(bg = "#CCC")
    openDocuments[currentTab].insert(INSERT, string)
    if (openDocuments[currentTab].get("%s-2c" % INSERT, "%s-1c" % INSERT) == '?') and \
    (openDocuments[currentTab].get("%s-1c" % INSERT, "%s" % INSERT) != ' '):
        findQuickDef(openDocuments[currentTab].get("%s-1c" % INSERT, INSERT))
    openDocuments[currentTab].tag_add("all", "1.0", "%s" %END)
    openDocuments[currentTab].tag_config("all", background="white", foreground="black")
    openDocuments[currentTab].tag_add("cursor", str(INSERT), "%s+1c" %INSERT)
    openDocuments[currentTab].tag_config("cursor", background="black", foreground="white")
    openDocuments[currentTab].see(str(INSERT))


#set up the gui

#top level stuff
root = Tk()
root.title("Text Editor")
try:
    icon = PhotoImage(file="te.png")
    root.tk.call('wm', 'iconphoto', root._w, icon)
except:
    print "Icon not found."

leftFrame = Frame(root)
rightFrame = Frame(root)

rightFrame.pack(side=RIGHT, fill="y")
leftFrame.pack(expand=YES, side=LEFT, fill=BOTH)

#menus and text entry
topBar = Frame(leftFrame, bg="#3C3B37")
topBar.pack(side=TOP, fill=BOTH)

fileMenu = Menubutton(topBar, text = 'File')
fileMenu.config(fg = "white", bg = "#3C3B37")
fileMenu.pack(side = LEFT)
menu = Menu(fileMenu)
menu.add_command(label = 'New document', command = newDoc, underline = 0)
menu.add_command(label = 'Open...', command = openFile, underline = 0)
menu.add_command(label = 'Save', command = save, underline = 0)
menu.add_command(label = 'Save As...', command =saveAs, underline = 5)
menu.add_command(label = 'Quit', command = warn, underline = 0)
fileMenu['menu'] = menu

#for the text entry
textEntry = Entry(topBar)
textEntry.pack(side=RIGHT)
#most of the bindings
for keystroke in bindings:
    def make_lambda(output):
        return lambda x: insert(output)
    textEntry.bind(keystroke, make_lambda(bindings[keystroke]))

for keystroke in letters:
    def make_lambda(output):
        return lambda x : insert(output)
    textEntry.bind(keystroke, make_lambda(letters[keystroke]))

#some more bindings
textEntry.bind("<BackSpace>", lambda x: backspace())
textEntry.bind(ctrl+"BackSpace>", lambda x: deleteWord())
root.bind("<Escape>", lambda x: save())
textEntry.bind("<Control-Return>", lambda x: quickDefLookupEntry.focus_set())
textEntry.bind("<Control-space>", lambda x: insert("    ")) #I don't know if this will work

#these are the tabs for multiple files
tabsFrame = Frame(leftFrame, bg = "#3C3B37") #magic value for a tone of gray
tabsFrame.pack(side=TOP, fill=BOTH)

tabs["Untitled 1"] = (Button(tabsFrame, text = currentTab))
tabs["Untitled 1"].configure(command = lambda: edit("Untitled 1"))
tabs["Untitled 1"].configure(bg = "#FFF")
tabs["Untitled 1"].pack(side=LEFT)
mainFrame = Frame(leftFrame)
mainFrame.pack(side=TOP, fill=BOTH, expand=YES)

#initialize a document
openDocuments["Untitled 1"] = ScrolledText(mainFrame, wrap=WORD)#, height=28, width=80)
openDocuments["Untitled 1"].pack(fill = BOTH, expand=YES)
#openDocuments["Untitled 1"].focus_set()
#setKeyBindings("Untitled 1")


#stuff on the right

lookupFrame = Frame(rightFrame)
quickDefLookupEntry = Entry(lookupFrame, width = 5)
quickDefLookupEntry.bind("<Return>", lambda x: lookup())
lookupLabel = Label(lookupFrame, text = "")

quickDefLabel = Label(rightFrame, text = "quickdefs", bg="gray")
addQuickDef = Button(rightFrame, text = "[+]", command = lambda: makeQuickDef(rightFrame))

quickDefLookupEntry.bind("<Control-Return>", lambda x: lookup())

lookupFrame.pack(side=TOP)
quickDefLookupEntry.pack(side=TOP)
lookupLabel.pack(side=TOP)

quickDefLabel.pack()
#makeQuickDef(rightFrame)
addQuickDef.pack(side=BOTTOM)

textEntry.focus_set()

#set an action to happen when the window is closed
root.protocol("WM_DELETE_WINDOW", warn)

if __name__ == "__main__":
    root.mainloop()
