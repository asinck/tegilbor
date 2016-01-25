#this file has almost all of the key bindings for the main program.

#if I ever rebind the almost 200 combinations again, I am so writing a
#secondary program to format everything for me. Careful listing,
#grouping, and reassignment of all the keys took days; typing in the
#assignments and formatting everything took FOREVER. Seriously.


#some random helpful info copied off a site:
''' 
userInput.bind("<Escape>", lambda(nothing): destroyThis(userDialog))
userInput.bind("<Return>", functionB)

You can bind to virtually all keys on the keyboard. For an ordinary 102-key PC-style keyboard, the special keys are


Cancel (the Break key),
BackSpace,
Tab,
Return(the Enter key),
Shift_L (any Shift key), 
Control_L (any Control key), 
Alt_L (any Alt key), 
Pause, 
Caps_Lock, 
Escape, 
Prior (Page Up), 
Next (Page Down), 
End, 
Home, 
Left, 
Up, 
Right, 
Down, 
Print, 
Insert, 
Delete, 
F1, ... F12,
Num_Lock, 
and Scroll_Lock.

Use in format:
<Control-key>

# Little-known feature of Tk, it allows to bind an event to
# multiple keystrokes
self.bind("<Control-Key-%s><Key>" % k,
          lambda event, a=a: self.insert_accented(event.char, a))
'''

#modifiers
ctrl = "<Control-"
alt = "<Alt-"

#keys
backspace = "<BackSpace>"
enter = "<Return>"
space = "<space>"
less = "<less>"

a = "a>"; b = "b>"; c = "c>"; d = "d>"; e = "e>";
f = "f>"; g = "g>"; h = "h>"; i = "i>"; j = "j>";
k = "k>"; l = "l>"; m = "m>"; n = "n>"; o = "o>";
p = "p>"; q = "q>"; r = "r>"; s = "s>"; t = "t>";
u = "u>"; v = "v>"; w = "w>"; x = "x>"; y = "y>";
z = "z>";

A = "A>"; B = "B>"; C = "C>"; D = "D>"; E = "E>";
F = "F>"; G = "G>"; H = "H>"; I = "I>"; J = "J>";
K = "K>"; L = "L>"; M = "M>"; N = "N>"; O = "O>";
P = "P>"; Q = "Q>"; R = "R>"; S = "S>"; T = "T>";
U = "U>"; V = "V>"; W = "W>"; X = "X>"; Y = "Y>";
Z = "Z>";

bindings = {
    #special characters
    enter:"\n",
    space:" ",

    #actual bindings
    ctrl+q:"who",    alt+q:"qu",     ctrl+Q:"que",    alt+Q:"dle",
    ctrl+w:"what",   alt+w:"wh",     ctrl+W:"was",    alt+W:"ware",
    ctrl+e:"when",   alt+e:"ere",    ctrl+E:"ese",    alt+E:"ele",
    ctrl+r:"where",  alt+r:"tri",    ctrl+R:"try",    alt+R:"tran",
    ctrl+t:"why",    alt+t:"tion",   ctrl+T:"tian",   alt+T:"ity",
    ctrl+y:"how",    alt+y:"st",     ctrl+Y:"str",    alt+Y:"thr",
    ctrl+u:"would",    alt+u:"ie",     ctrl+U:"ea",     alt+U:"ent",
    ctrl+i:"which",  alt+i:"ing",    ctrl+I:"ang",    alt+I:"ong",
    ctrl+o:"while",  alt+o:"ou",     ctrl+O:"uou",    alt+O:"ough",
    ctrl+p:"have",  alt+p:"ple",    ctrl+P:"pre",    alt+P:"per",
    
    ctrl+a:"this",   alt+a:"ose",    ctrl+A:"ore",    alt+A:"one",
    ctrl+s:"there",  alt+s:"sion",   ctrl+S:"sian",   alt+S:"ism",
    ctrl+d:"these",  alt+d:"con",    ctrl+D:"cont",   alt+D:"can",
    ctrl+f:"the",    alt+f:"ed",     ctrl+F:"nd",     alt+F:"nt",
    ctrl+g:"that",   alt+g:"gh",     ctrl+G:"ght",    alt+G:"ight",
    ctrl+h:"than",   alt+h:"ch",     ctrl+H:"sh",     alt+H:"th",
    ctrl+j:"they",   alt+j:"ass",    ctrl+J:"age",    alt+J:"ant",
    ctrl+k:"them",   alt+k:"act",    ctrl+K:"ect",    alt+K:"uct",
    ctrl+l:"those",  alt+l:"ly",     ctrl+L:"le",     alt+L:"ld",
    
    ctrl+z:"thing",  alt+z:"ice",    ctrl+Z:"ide",    alt+Z:"ize",
    ctrl+x:"think",  alt+x:"able",   ctrl+X:"ible",   alt+X:"ble",
    ctrl+c:"and",    alt+c:"ance",   ctrl+C:"ence",   alt+C:"nce",
    ctrl+v:"are",    alt+v:"eve",    ctrl+V:"ive",    alt+V:"ove",
    ctrl+b:"any",    alt+b:"ion",    ctrl+B:"ian",    alt+B:"ize",
    ctrl+n:"add",    alt+n:"ness",   ctrl+N:"less",   alt+N:"cess",
    ctrl+m:"ave",    alt+m:"ment",   ctrl+M:"main",   alt+M:"mult",

    #pairs of lines are physical keys on the keyboard
    #one line break is to separate keys in a group
    #two line breaks separate groups
    
    ctrl+"Key-1>"       : "first",   alt+"Key-1>"        : "in",           
    ctrl+"Key-exclam>"  : "cap",     alt+"exclam>"       : "sys",

    ctrl+"Key-2>"       : "second",  alt+"Key-2>"        : "on",           
    ctrl+"at>"          : "lex",     alt+"at>"           : "les",

    ctrl+"Key-3>"       : "third",   alt+"Key-3>"        : "is",           
    ctrl+"numbersign>"  : "tune",    alt+"numbersign>"   : "plan",

    ctrl+"Key-4>"       : "fourth",  alt+"Key-4>"        : "of",           
    ctrl+"dollar>"      : "icle",    alt+"dollar>"       : "mem",

    ctrl+"Key-5>"       : "fifth",   alt+"Key-5>"        : "at",           
    ctrl+"percent>"     : "ned",     alt+"percent>"      : "der",
    
    
    ctrl+"6>":"if",     alt+"6>":"it",

    ctrl+"7>":"else",   alt+"7>":"int",

    ctrl+"8>":"then",   alt+"8>":"ary",

    ctrl+"9>":"not",    alt+"9>":"est",

    ctrl+"0>":"for",    alt+"0>":"ll",


    ctrl+"quoteleft>"   : "but",     alt+"quoteleft>"    : "con",      
    ctrl+"asciitilde>"  : "com",     alt+"asciitilde>"   : "comp",


    ctrl+"minus>"       : "to",      alt+"minus>"        : "tune",         
    ctrl+"underscore>"  : "ture",    alt+"underscore>"   : "ure",

    ctrl+"equal>"       : "from",    alt+"equal>"        : "out",          
    ctrl+"plus>"        : "ea",      alt+"plus>"         : "igh",


    ctrl+"bracketleft>" : "some",    alt+"bracketleft>"  : "ign",
    ctrl+"braceleft>"   : "igh",     alt+"braceleft>"    : "ivi",
                                     
    ctrl+"bracketright>": "few",     alt+"bracketright>" : "gen",
    ctrl+"braceright>"  : "gent",    alt+"braceright>"   : "end",
                                     
    ctrl+"backslash>"   : "many",    alt+"backslash>"    : "inter",
    ctrl+"bar>"         : "chr",     alt+"bar>"          : "sub",

    
    ctrl+"semicolon>"   : "before",  alt+"semicolon>"    : "after", 
    ctrl+"colon>"       : "against", alt+"colon>"        : "ten",

    ctrl+"quoteright>"  : "with",    alt+"quoteright>"   : "ike",   
    ctrl+"quotedbl>"    : "ink",     alt+"quotedbl>"     : "ake",


    ctrl+"comma>"       : "ich",     alt+"comma>"        : "tch",   
    ctrl+"less>"        : "ick",     alt+"less>"         : "ack",

    ctrl+"period>"      : "use",     alt+"period>"       : "ose",   
    ctrl+"greater>"     : "chip",    alt+"greater>"      : "ship",

    ctrl+"slash>"       : "pro",     alt+"slash>"        : "pos",   
    ctrl+"question>"    : "gram",    alt+"question>"     : "graph"

    

#unassigned:
# ^ = ctrl+"asciicircum>":"",
# & = ctrl+"ampersand>":"",
# * = ctrl+"asterisk>":"",
# ( = ctrl+"parenleft>":"",
# ) = ctrl+"parenright>":"",

    #keys that have issues:
    #alt-` (OS level command similar to alt-tab)
    #ctrl-~, ctrl-!, ctrl-@ all don't fire
    #ctrl-U (OS level command, some sort of UTF8 insertion command)
}


letters = {
    "0":"0", "1":"1", "2":"2", "3":"3", "4":"4",
    "5":"5", "6":"6", "7":"7", "8":"8", "9":"9",

    "a":"a", "b":"b", "c":"c", "d":"d", "e":"e",
    "f":"f", "g":"g", "h":"h", "i":"i", "j":"j",
    "k":"k", "l":"l", "m":"m", "n":"n", "o":"o",
    "p":"p", "q":"q", "r":"r", "s":"s", "t":"t",
    "u":"u", "v":"v", "w":"w", "x":"x", "y":"y",
    "z":"z",

    "A":"A", "B":"B", "C":"C", "D":"D", "E":"E",
    "F":"F", "G":"G", "H":"H", "I":"I", "J":"J",
    "K":"K", "L":"L", "M":"M", "N":"N", "O":"O",
    "P":"P", "Q":"Q", "R":"R", "S":"S", "T":"T",
    "U":"U", "V":"V", "W":"W", "X":"X", "Y":"Y",
    "Z":"Z",

    "!":"!", '"':'"', "#":"#", "$":"$", "%":"%",
    "&":"&", "'":"'", "(":"(", ")":")", "*":"*",
    "+":"+", ",":",", "-":"-", ".":".", "/":"/",
    ":":":", ";":";", "=":"=", ">":">", "<less>":"<", #less doesn't like being bound
    "?":"?", "@":"@", "[":"[", "\\":"\\", "]":"]",
    "^":"^", "_":"_", "`":"`", "{":"{", "|":"|",
    "}":"}", "~":"~"
}
