#!/usr/bin/env python
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
    # "import hashlib",
    # "import time",
    # "import random"
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
#if there were any errors in the imports, tell the user what packages
#didn't import, and exit.
if len(failedPackages) > 0:
    print "Some packages could not be imported:"
    print failedPackages
    exit()

#global variables
currentTab = "Untitled 1" #this is the name of the initial tab
openDocuments = {}        #a hash table of documents
tabs = {}                 #a hash table of the tabs that will allow the
unnamedDocs = 0           #user to have multiple tabs open at once
quickDefs = {}
lastLen = 1

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
    global currentTab
    empty = openDocuments[currentTab].get(1.0, END) == '\n'
    unnamed = "Untitled" in currentTab
    return empty and unnamed

#this is used for switching tabs
def edit(tabName, sameTab=False):
    global currentTab
    openDocuments[currentTab].pack_forget()
    currentTab = tabName
    openDocuments[currentTab].pack(fill = BOTH, expand=YES)
    root.title(currentTab + " - Tegilbor Speed Text Editor")
    openDocuments[currentTab].bind("<Key>", lambda x: status())

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
            #make the command of the current tab be to edit the
            #document with the filename
            tabs[currentTab].configure(command = lambda: edit(fileName))
            #make a new entry in tabs, and make it point to the current
            #tab this makes it so that the key that points to the tab
            #matches the filename
            tabs[fileName] = tabs[currentTab]
            del tabs[currentTab]
            #put the file in the document area
            openDocuments[fileName] = ScrolledText(mainFrame, wrap=WORD, bg="#004", fg="#FFF")
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
            openDocuments[fileName] = ScrolledText(mainFrame, wrap=WORD, bg="#004", fg="#FFF")
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
    #This depends on the tabs _always_ being properly colored, whether
    #they were edited with the entry box or directly.
    unsavedChanges = False
    for tab in tabs:
        if tabs[tab].cget("bg") != "#FFF":
            unsavedChanges = True
    if unsavedChanges:
        if tkMessageBox.askokcancel("Save?", "Have you saved everything?"):
            root.destroy()
    else:
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
    openDocuments[s] = ScrolledText(mainFrame, wrap=WORD, bg="#004", fg="#FFF")#, height=28, width=80)
    
    edit(s)
    currentTab = s
    tabs[currentTab].configure(bg = "#FFF")

#this defines a new quickdef, or redefines an existing quickdef
def quickDef(key, word):
    if key not in quickDefs:
        currentText = activeQuickDefsLabel.cget("text")
        newText = currentText + "\n%s: %s\n" %(key, word)
        newText = '\n'.join(sorted(newText.split("\n"))).strip()
        activeQuickDefsLabel.config(text = newText);
        quickDefs[key] = word
    else:
        if (quickDefs[key] != word):
            deleteQuickDef(key)
            quickDef(key, word) #I'm lazy
    textEntry.focus_set()

#this deletes a quickdef, if possible
def deleteQuickDef(key):
    try:
        #find out what the word is, so the label can be deleted
        word = quickDefs[key]
        currentText = activeQuickDefsLabel.cget("text")
        newText = currentText.replace("%s: %s\n" %(key, word), "")
        activeQuickDefsLabel.config(text = newText);
        
        del quickDefs[key]
        
    except:
        messagesLabel.config(text = "Key not found.")

#this does the auto-replace of quickdefs
def findQuickDef(key):
    global currentTab
    try:
        word = quickDefs[key]
        openDocuments[currentTab].delete("%s-2c" % INSERT, INSERT)
        insert(word)
    except:
        messagesLabel.config(text = "Key not found.")

#this lets the user look up a binding
def lookup():
    global currentTab
    #get the string that the user wants to look up, clear the entry
    #box, and refocus the text entry box
    string = bindingLookupEntry.get()
    bindingLookupEntry.delete(0, 'end')
    textEntry.focus_set()

    #go through all the bindings, searching for the ones that have the
    #search string
    results = []
    if (string != ''):
        for key in bindings:
            if (string in bindings[key]):
                s = key + " " + bindings[key]
                results.append(s)
        results = sorted(results, key=len)
    bindingLookupLabel.config(text='\n'.join(results))
    #this might be an issue...if this focuses on the end, instead of
    #the current cursor position
    openDocuments[currentTab].see("end")
    
#this is a ctrl-backspace (delete previous word)
def deleteWord(var=None):
    global lastLen, currentTab
    lastLen = 1
    char = '-'
    while char not in " _\n.,":
        openDocuments[currentTab].delete("%s-1c" % INSERT, INSERT)
        char = openDocuments[currentTab].get("%s-1c" % INSERT, INSERT)
    status()

#this adds special functionality to backspace, so that it deletes the
#last insertion, instead of the last character. This is helpful when you
#typo a binding.
def backspace(var=None):
    global lastLen, currentTab
    for i in range(lastLen):
        openDocuments[currentTab].delete("%s-1c" % INSERT, INSERT)
    lastLen = 1
    status()


#this checks to make sure a function call is working
def functionCheck(var=None):
    print "Function call is working. Value is", var

#this checks to see if the given document is saved
def isSaved(docName):
    return openDocuments[docName].cget("bg") == "#FFF"
    
#this moves the cursor around
def setCursor(line, col):
    (currentLine, currentCol) = getPosition()
    newLine = currentLine + line
    newCol = currentCol + col
    openDocuments[currentTab].mark_set("insert", "%d.%d" % (newLine, newCol))
    #tabs[tab].cget("bg") == "#FFF"
    status() #status(True) might work, but needs to reflect if the
             #document is actually saved or not

#this takes the line.col string and returns a (line, col)
#representation
def getPosition():
    (line,col) = openDocuments[currentTab].index(INSERT).split(".")
    return (int(line),int(col))
    
#this will update the program with the current status
# - line and column number
# - saved or not saved
# - cursor position highlighting
def status(saved=False):

    #this does the current position highlighting
    #this should be changed to a) remove all irrelevant tags, and
    #    b) also track the main text window, not just the text entry
    openDocuments[currentTab].tag_delete("cursor")
    openDocuments[currentTab].tag_add("cursor", str(INSERT), "%s.%s+1c" %getPosition())
    openDocuments[currentTab].tag_config("cursor", background="white", foreground="#003")

    #this will give the user an indication of if the file is saved or not
    if (not saved):
        tabs[currentTab].configure(bg = "#CCC")
    else:
        tabs[currentTab].configure(bg = "#FFF")

    #this will tell the user the current line and column number
    #print "%s" %openDocuments[currentTab].END#openDocuments[currentTab].INSERT
    positionLabel.config(text="(%d:%d)" %getPosition())

#this does the insertion into the editor window.
def insert(string):
    global lastLen, currentTab
    messagesLabel.config(text = "")
    lastLen = len(string)
    openDocuments[currentTab].insert(INSERT, string)
    if (openDocuments[currentTab].get("%s-2c" % INSERT, "%s-1c" % INSERT) == '?') and \
    (openDocuments[currentTab].get("%s-1c" % INSERT, "%s" % INSERT) != ' '):
        findQuickDef(openDocuments[currentTab].get("%s-1c" % INSERT, INSERT))
    status()
    openDocuments[currentTab].see(str(INSERT))


#set up the gui

#top level stuff
root = Tk()
root.title("Tegilbor Speed Text Editor")
try:
    icon = PhotoImage(file="icon.png")
    root.tk.call('wm', 'iconphoto', root._w, icon)
except:
    try:
        icon = PhotoImage(file="icon.gif")
        root.tk.call('wm', 'iconphoto', root._w, icon)
    except:
        messagesLabel.config(text = "Note: Unable to set program icon.")

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
textEntry.bind("<Control-Return>", lambda x: bindingLookupEntry.focus_set())
textEntry.bind("<Control-space>", lambda x: insert("    "))
#I should also bind a click in the text area to setCursor or something
textEntry.bind("<Up>",    lambda x: setCursor(-1,0))
textEntry.bind("<Down>",  lambda x: setCursor(1,0))
textEntry.bind("<Right>", lambda x: setCursor(0,1))
textEntry.bind("<Left>",  lambda x: setCursor(0,-1))

#these are the tabs for multiple files
tabsFrame = Frame(leftFrame, bg = "#3C3B37") #magic value for a tone of gray
tabsFrame.pack(side=TOP, fill=BOTH)

mainFrame = Frame(leftFrame)
mainFrame.pack(side=TOP, fill=BOTH, expand=YES)

statusBar = Frame(leftFrame)
positionLabel = Label(statusBar, text = "(1:0)")
messagesLabel = Label(statusBar, text = "")

statusBar.pack(side=BOTTOM, fill="x")
positionLabel.pack(side=RIGHT)
messagesLabel.pack(side=LEFT)
#initialize a document
newDoc()

#stuff on the right
#the lookup area
bindingLookupFrame = Frame(rightFrame)
bindingLookupEntry = Entry(bindingLookupFrame, width = 5)
bindingLookupEntry.bind("<Return>", lambda x: lookup())
bindingLookupEntry.bind("<Control-Return>", lambda x: lookup())
bindingLookupLabel = Label(bindingLookupFrame, text = "")

bindingLookupFrame.pack(side=TOP)
bindingLookupEntry.pack(side=TOP)
bindingLookupLabel.pack(side=TOP)

#the quick defs area
#hold the quick def stuff
quickDefFrame = Frame(rightFrame)
#the label telling the user what this area is
quickDefLabel = Label(quickDefFrame, text = "quickdefs", bg="gray")

quickDefFrame.pack(side=TOP)
quickDefLabel.pack(side=TOP, expand = YES, fill = "x")

#a list of active quick defs
activeQuickDefsLabel = Label(quickDefFrame, text = "")

#allow the user to add quick defs
newQuickDefFrame = Frame(quickDefFrame)
newQuickDefLeftFrame = Frame(newQuickDefFrame)
newQuickDefRightFrame = Frame(newQuickDefFrame)
newQuickDefButtonFrame = Frame(newQuickDefFrame)

newQuickDefKeyLabel = Label(newQuickDefLeftFrame, text = "Key")
newQuickDefKeyEntry = Entry(newQuickDefLeftFrame, width = 2)
newQuickDefKeyEntry.bind("<Return>", lambda x: quickDef(newQuickDefKeyEntry.get(), newQuickDefWordEntry.get()))
newQuickDefColon = Label(newQuickDefFrame, text = "\n:")
newQuickDefWordLabel = Label(newQuickDefRightFrame, text = "Word")
newQuickDefWordEntry = Entry(newQuickDefRightFrame, width = 7)
newQuickDefWordEntry.bind("<Return>", lambda x: quickDef(newQuickDefKeyEntry.get(), newQuickDefWordEntry.get()))
newQuickDefCloseButton = Button(newQuickDefButtonFrame, text = "[X]", command = lambda: deleteQuickDef(newQuickDefKeyEntry.get()))
newQuickDefAddButton = Button(newQuickDefButtonFrame, text = "[+]", command = lambda: quickDef(newQuickDefKeyEntry.get(), newQuickDefWordEntry.get()))

#pack all the stuff for the quick defs
newQuickDefFrame.pack(side=TOP)
newQuickDefLeftFrame.pack(side=LEFT)
newQuickDefButtonFrame.pack(side=RIGHT)
newQuickDefRightFrame.pack(side=RIGHT)

newQuickDefFrame.pack(side=TOP)
newQuickDefKeyLabel.pack(side=TOP)
newQuickDefKeyEntry.pack(side=BOTTOM)
newQuickDefColon.pack()
newQuickDefWordLabel.pack(side=TOP)
newQuickDefWordEntry.pack(side=BOTTOM)

newQuickDefAddButton.pack(side=TOP)
newQuickDefCloseButton.pack(side=BOTTOM)

activeQuickDefsLabel.pack(side=TOP)

textEntry.focus_set()

#set an action to happen when the window is closed
root.protocol("WM_DELETE_WINDOW", warn)

if __name__ == "__main__":
    root.mainloop()
