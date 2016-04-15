#Tegilbor

I wrote this program so that I could type quickly with shorthand. For example, typing "the program" can be done by typing ctrl-f space ctrl-/ ctrl-? (capitalization is important). In theory, this means that I will be able to type much more quickly, hopefully at talking speed. 

This program adds speed typing abilities to my other text editor, located at https://github.com/asinck/amdiron. 

###Explanation of the Program:

This program has the standard capabilities; that is, it can open, edit, and save files, and have multiple files open at the same time. It also has the following:

####Tabs:
The tabs show the file that each tab holds. Clicking on a tab will show that file. If a file is saved, the tab will be white. If the file has been edited since the last save, the tab will be gray. Note that right now, moving the cursor in the file turns the tab gray, and middle click pasting in the file doesn't.

####Text Entry Box:
There is one main entry box, which will be focused when the program is started. It is what you type in, and what has all the bindings. It will be directly above the text box, to the right.

####Looking up Bindings:
On the right is a sidebar. This sidebar contains both a lookup field and a quick definition field. The lookup field allows the user to look up bindings that have the search string in them. The user can jump directly to this field by hitting ctrl-enter.

####QuickDefs:
These allow the user to define a expansion string for a letter. To activate expansion, the user types a question mark followed by the letter. For example, if the user knows that they're going to type "github" a lot, they can define g as "github", and when they're typing, if they type "?g" it will be replaced with "github".

Quickdefs can be defined as pretty much anything, so they can used for word fragments, whole words, phrases, paragraphs, etc.

To add a quickdef (for the current session only), enter the letter and word that the letter stands for, and either hit enter or click the little [+] next to the entry. The quickdefs can also be imported/exported with the buttons under the list, for saving them between sessions. To remove a quickdef, select it from the list and click the [X] under the list.

The user can jump directly to the key definition entry field with shift-enter.

###Installation Notes:
This program uses the Tkinter GUI library. If it is not installed, you can't use the program. If you aren't sure, you can try to run the program, and it will let you know. 

###Bugs:
* Middle click pasting doesn't affect the "saved" status.
* Moving around in the document with the keyboard causes the document to be considered unsaved.
* The auto-scroll to cursor may not always work when a binding is looked up.
* The length sorting for the lookup does not work properly.
* The line/col indication is not correct (except by coincidence) if the user clicks in the text field.

###Upcoming enhancements:
#####File handling 
* Allow the program to generate timestamps to append to the filename.
* Get a better file open or save dialog (also import/export dialog).

#####Text area:
* Remember indentation.
* Line numbers.
* Let ctrl-backspace delete a string of whitespace.

#####Quickdefs:
* Automatically generated quickdefs.

#####Other:
* Allow the user to close tabs.
* Fix the readme to not switch between first, third, and second person.
* Allow typing of any character in the text entry box, and saving of files with UTF-8 characters.
* Rewrite the whole program to clean up the code.

###Notes:

The bindings for the keys may change occasionally, as I see fit. 

Hitting ESC from anywhere in the program saves the file.

Tegilbor is elvish for writer. See http://elf.namegeneratorfun.com/ .

Some bindings don't actually work; possibly due either to the OS not allowing it, or the keyboard not being able to handle it. This is not a bug that I can fix.
