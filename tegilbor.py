#this is a list of import commands. If the user doesn't have Tkinter
#or other libraries installed, it will fail gracefully instead of
#crashing.
imports = [
    "from Tkinter import *",
    "import Tkinter as tk",
    "from ScrolledText import ScrolledText",
    "from keybindings import *",
    "import time"
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

fileName = ""
#lastlen keeps track of the length of the most recent insertion, for backspace
lastLen = 0
quickDefs = {" ":"?  "}

# def resize(event):
#     size = (innerTextFrame.winfo_reqwidth(), innerTextFrame.winfo_reqheight())
#     canvas.config(scrollregion="0 0 %s %s" % size)

# def scroll(event):
#     direction = 1
#     if event.num == 4:
#         direction = -1
#     canvas.yview_scroll(direction, "units")

def save():
    global fileName
    print fileName
    if (fileName == ""):
        className = classNameField.get()
        if (className == ""):
            topFrame.configure(bg="RED")
        else:
            topFrame.configure(bg="GRAY")
            timestamp = time.strftime("[%m-%d-%Y]_%H.%M.%S", time.localtime())
            fileName = className + "_" + timestamp + ".txt"
            contents = textArea.get(1.0, END)
            myFile = open(fileName, "w+")
            myFile.write(contents)
            myFile.close()
            print "File Created."
    else:
        topFrame.configure(bg="GRAY")
        contents = textArea.get(1.0, END)
        myFile = open(fileName, "w+")
        myFile.write(contents)
        myFile.close()
        print "Saved."

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

def quickDef(key, word):
    quickDefs[key] = word

def deleteQuickDef(key):
    try:
        del quickDefs[key]
    except:
        print key + " not found."

def findQuickDef(key):
    try:
        word = quickDefs[key]
        textArea.delete("%s-2c" % INSERT, INSERT)
        insert(word)
    except:
        print "Key not found."

def lookup():
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
    textArea.see("end")
    
def deleteWord(var=None):
    global lastLen
    lastLen = 1
    char = '-'
    while char not in " _\n.,":
        textArea.delete("%s-1c" % INSERT, INSERT)
        char = textArea.get("%s-1c" % INSERT, INSERT)

def backspace(var=None):
    global lastLen
    for i in range(lastLen):
        textArea.delete("%s-1c" % INSERT, INSERT)
    lastLen = 1


def insert(string):
    global lastLen
    lastLen = len(string)
    textArea.insert(INSERT, string)
    if (textArea.get("%s-2c" % INSERT, "%s-1c" % INSERT) == '?'):
        findQuickDef(textArea.get("%s-1c" % INSERT, INSERT))
    textArea.tag_add("all", "1.0", "%s" %END)
    textArea.tag_config("all", background="white", foreground="black")
    textArea.tag_add("cursor", str(INSERT), "%s+1c" %INSERT)
    textArea.tag_config("cursor", background="black", foreground="white")
    textArea.see("end")

root = Tk()
root.title("Typewriter")

mainFrame = Frame(root, bg="gray")
leftFrame = Frame(mainFrame)
rightFrame = Frame(mainFrame)

topFrame = Frame(leftFrame)
textFrame = Frame(leftFrame, bg="blue")
textEntry = Entry(topFrame)

textArea = ScrolledText(textFrame, wrap=WORD)

classNameField = Entry(topFrame, width = 6)
saveButton = Button(topFrame, text = "Save", command = lambda: save())

lookupFrame = Frame(rightFrame)
quickDefLookupEntry = Entry(lookupFrame, width = 5)
quickDefLookupEntry.bind("<Return>", lambda x: lookup())
lookupLabel = Label(lookupFrame, text = "")

quickDefLabel = Label(rightFrame, text = "quickdefs", bg="gray")
addQuickDef = Button(rightFrame, text = "[+]", command = lambda: makeQuickDef(rightFrame))



for keystroke in bindings:
    def make_lambda(output):
        return lambda x: insert(output)
        #return lambda x : textArea.insert(INSERT, output)
    textEntry.bind(keystroke, make_lambda(bindings[keystroke]))

for keystroke in letters:
    def make_lambda(output):
        return lambda x : insert(output)
        #return lambda x : textArea.insert(INSERT, output)
    textEntry.bind(keystroke, make_lambda(letters[keystroke]))

#textEntry.bind(backspace, lambda x: textArea.delete("%s-1c" % INSERT, INSERT))
textEntry.bind("<BackSpace>", lambda x: backspace())
textEntry.bind(ctrl+"BackSpace>", lambda x: deleteWord())
root.bind("<Escape>", lambda x: save())
#textEntry.bind("<Control-Return>", lambda x: findQuickDef())
textEntry.bind("<Control-Return>", lambda x: quickDefLookupEntry.focus_set())
quickDefLookupEntry.bind("<Control-Return>", lambda x: lookup())

mainFrame.pack(expand=YES, fill=BOTH)
leftFrame.pack(expand=YES, side=LEFT, fill=BOTH)
rightFrame.pack(side=RIGHT, fill="y")
topFrame.pack(side=TOP, fill="x")
textFrame.pack(expand=YES, side=BOTTOM, fill=BOTH)

classNameField.pack(side=LEFT)
saveButton.pack(side=LEFT)
textEntry.pack(side=RIGHT)

textArea.pack(expand=YES, fill=BOTH)



lookupFrame.pack(side=TOP)
quickDefLookupEntry.pack(side=TOP)
lookupLabel.pack(side=TOP)

quickDefLabel.pack()
#makeQuickDef(rightFrame)
addQuickDef.pack(side=BOTTOM)

textEntry.focus_set()


# root.update()
# root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()
