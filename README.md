I wrote this program so that I could type quickly with shorthand. For example, typing "the program" can be done by typing ctrl-f space ctrl-/ ctrl-? (capitalization is important). In theory, this means that I will be able to type much more quickly, hopefully at talking speed. 

Explanation of the Program:

Text Entry Box:
There is one main entry box, which will be focused when you start the program. It is what you type in, and what has all the bindings. It will be directly above the text box, to the right.

Saving a File:
To the left is an entry box so that you can put a prefix on the file name that it saves. If the user allows timestamps, the file will be saved with user_prefix_[MM-DD-YYYY]_HH.MM.SS.txt. Otherwise, it will just be user_prefix.txt. This is so that when I take notes for a class with this program, I can specify what class it is, with automatic dating. If this field is left blank, the program will turn the bar red and not save. Otherwise, the bar will turn gray. You can hit escape from anywhere in the program to save, or click the save button. 

Looking up Bindings:
On the right is a sidebar. This sidebar contains both a lookup field and a quick definition field. The lookup field allows the user to look up bindings that have the search string in them. 

QuickDefs:
These allow the user to define a expansion string for a letter. To activate expansion, the user types a question mark followed by the letter. For example, if the user knows that they're going to type "github" a lot, they can define g as "github", and when they're typing, if they type "?g" it will be replaced with "github".

These can also be helpful if you have a part of a word that you know you're going to use a lot, but doesn't have a binding assigned to it. 

The quick definitions can be defined as pretty much anything, so they can also be used for phrases. 

The little [+] next to a quickdef adds that quickdef to the program (they aren't saved though), as does enter. The [X] removes that quickdef from the program. 

The [+] at the bottom right is to add a quickdef slot.

Installation Notes:
This program uses the Tkinter library. If Tkinter is not installed, you can't use the program. If you aren't sure, you can try to run the program, and it will let you know. 

Bugs:
* The program warns a user if they try to overwrite a file, but does not allow them to open a file.
* Some keys don't actually work; possibly due either to the OS not allowing it, or the keyboard not being able to handle it.
* The text doesn't always auto-scroll to the bottom when a binding is looked up.

Upcoming enhancements:
* Warn the user if they try to exit the program without saving the file.
* Automatically generated quickdefs.

Notes:

The bindings for the keys may change occasionally, as I see fit. 

Tegilbor is elvish for writer. See http://elf.namegeneratorfun.com/ .