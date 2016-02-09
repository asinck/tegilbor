I wrote this program so that I could type quickly with shorthand. For example, typing "the program" can be done by typing ctrl-f space ctrl-/ ctrl-? (capitalization is important). In theory, this means that I will be able to type much more quickly, hopefully at talking speed. 

This program adds speed typing abilities to my other text editor, located at https://github.com/asinck/amdiron. 

Explanation of the Program:

This program has the standard capabilities; that is, it can open, edit, and save files, and have multiple files open at the same time.

Tabs:
The tabs show the file that each tab holds. Clicking on a tab will show that file. If a file is saved, the tab will be white. If the file has been edited via the speed entry box since the last save, the tab will be gray.

Text Entry Box:
There is one main entry box, which will be focused when you start the program. It is what you type in, and what has all the bindings. It will be directly above the text box, to the right.

Looking up Bindings:
On the right is a sidebar. This sidebar contains both a lookup field and a quick definition field. The lookup field allows the user to look up bindings that have the search string in them. 

QuickDefs:
These allow the user to define a expansion string for a letter. To activate expansion, the user types a question mark followed by the letter. For example, if the user knows that they're going to type "github" a lot, they can define g as "github", and when they're typing, if they type "?g" it will be replaced with "github".

These can also be helpful if you have a part of a word that you know you're going to use a lot, but doesn't have a binding assigned to it. 

The quick definitions can be defined as pretty much anything, so they can also be used for phrases. 

The little [+] next to a quickdef adds that quickdef to the program (for the current session only), as does enter. The [X] removes that quickdef from the program. 

The [+] at the bottom right is to add a quickdef slot.

Installation Notes:
This program uses the Tkinter library. If Tkinter is not installed, you can't use the program. If you aren't sure, you can try to run the program, and it will let you know. 

Bugs:
* Some keys don't actually work; possibly due either to the OS not allowing it, or the keyboard not being able to handle it.
* The auto-scroll to cursor may not always work when a binding is looked up.
* The highlighting that tells the user where the cursor is is a bit messed up.
* Editing the file directly instead of with the speed entry box doesn't turn the tab gray to indicate that the tab is not saved.
* The program should not allow the user to try to save a file without a name.
* The highlight that indicates where the user is typing might accidentally black out some of the user's text (unconfirmed).

Upcoming enhancements:
* Warn the user if they try to exit the program without saving the file, instead of just warning them to make sure they saved everything.
* Automatically generated quickdefs.
* Allow the program to generate timestamps to append to the filename.
* Remember indentation.

Notes:

The bindings for the keys may change occasionally, as I see fit. 

Hitting ESC from anywhere in the program saves the file.

Tegilbor is elvish for writer. See http://elf.namegeneratorfun.com/ .



