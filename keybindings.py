'''
userInput.bind("<Escape>", lambda(nothing): destroyThis(userDialog))
userInput.bind("<Return>", functionB)

The user pressed the Enter key. You can bind to virtually all keys on the keyboard. For an ordinary 102-key PC-style keyboard, the special keys are
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
    less:"<",
    space:" ",

    #actual bindings

    #make ctrl-, and ctrl-. jump to beginning and end?
    #bind C-? to a word completion predictor?
    
    ctrl+a:"able",   alt+a:"ible",   ctrl+A:"ice",    alt+A:"act",
    ctrl+b:"ang",    alt+b:"ary",    ctrl+B:"ion",    alt+B:"ian",
    ctrl+c:"ie",     alt+c:"chr",    ctrl+C:"cess",   alt+C:"cont",
    ctrl+d:"ea",     alt+d:"ect",    ctrl+D:"ent",    alt+D:"der",
    ctrl+e:"ere",    alt+e:"ese",    ctrl+E:"ele",    alt+E:"eve",
    ctrl+f:"of",     alt+f:"is",     ctrl+F:"mem",    alt+F:"ble",
    ctrl+g:"gh",     alt+g:"ght",    ctrl+G:"gram",   alt+G:"gen",
    ctrl+h:"ch",     alt+h:"sh",     ctrl+H:"chip",   alt+H:"ship",
    ctrl+i:"ing",    alt+i:"ity",    ctrl+I:"ire",    alt+I:"ive",
    ctrl+j:"ich",    alt+j:"ide",    ctrl+J:"igh",    alt+J:"ign",
    ctrl+k:"ink",    alt+k:"can",    ctrl+K:"geom",   alt+K:"int",
    ctrl+l:"less",   alt+l:"ly",     ctrl+L:"lex",    alt+L:"ld",
    ctrl+m:"ment",   alt+m:"main",   ctrl+M:"mult",   alt+M:"nt",
    ctrl+n:"nce",    alt+n:"inter",  ctrl+N:"in",     alt+N:"ness",
    ctrl+o:"ou",     alt+o:"ough",   ctrl+O:"on",     alt+O:"ong",
    ctrl+p:"pro",    alt+p:"ple",    ctrl+P:"pos",    alt+P:"per",
    ctrl+q:"qu",     alt+q:"que",    ctrl+Q:"com",    alt+Q:"comp",
    ctrl+r:"tri",    alt+r:"try",    ctrl+R:"ure",    alt+R:"ture",
    ctrl+s:"sion",   alt+s:"st",     ctrl+S:"sian",   alt+S:"str",
    ctrl+t:"tion",   alt+t:"th",     ctrl+T:"tian",   alt+T:"thr",
    ctrl+u:"uct",    alt+u:"uou",    ctrl+U:"it",     alt+U:"dle", #C-U has issues
    ctrl+v:"ivi",    alt+v:"ove",    ctrl+V:"tran",   alt+V:"ten",
    ctrl+w:"wh",     alt+w:"ware",   ctrl+W:"ance",   alt+W:"ence",
    ctrl+x:"nd",     alt+x:"ass",    ctrl+X:"age",    alt+X:"ant",
    ctrl+y:"sys",    alt+y:"use",    ctrl+Y:"ed",     alt+Y:"sub",
    ctrl+z:"ize",    alt+z:"con",    ctrl+Z:"gent",   alt+Z:"plan",


    #ose?
    
    ctrl+"Key-1>":"first", ctrl+"Key-2>":"second", ctrl+"Key-3>":"third",
    ctrl+"Key-4>":"fourth", ctrl+"Key-5>":"fifth",
    
    ctrl+"6>":"if", ctrl+"7>":"then", ctrl+"8>":"else",
    ctrl+"9>":"not", ctrl+"0>":"for", 

    ctrl+"quoteleft>":"they",
    ctrl+"asciitilde>":"on",
    ctrl+"Key-exclam>":"est",
    ctrl+"at>":"at",
    ctrl+"numbersign>":"point",
    ctrl+"dollar>":"plane",
    ctrl+"percent>":"line",
    ctrl+"asciicircum>":"definition",
    ctrl+"ampersand>":"government",
    ctrl+"asterisk>":"who",
    ctrl+"parenleft>":"what",
    ctrl+"parenright>":"when",
    ctrl+"minus>":"where",
    ctrl+"underscore>":"why",
    ctrl+"plus>":"how",
    ctrl+"equal>":"would",
    
    ctrl+"bracketleft>":"the",
    ctrl+"bracketright>":"these",
    ctrl+"braceleft>":"this",
    ctrl+"braceright>":"this is",
    ctrl+"bar>":"is a",
    ctrl+"backslash>":"there",

    ctrl+"semicolon>":"but",
    ctrl+"colon>":"while",
    ctrl+"quoteright>":"poly",
    ctrl+"quotedbl>":"compute",

    ctrl+"less>":"any",
    ctrl+"greater>":"that",
    ctrl+"slash>":"to",
    ctrl+"question>":"from",



    alt+"Key-1>":"and", alt+"Key-2>":"are", alt+"Key-3>":"add",
    alt+"Key-4>":"ack", alt+"Key-5>":"ase",
    
    alt+"6>":"some", alt+"7>":"few", alt+"8>":"many",
    alt+"9>":"thing", alt+"0>":"think", 

    alt+"quoteleft>":"ave",
    alt+"asciitilde>":"",
    alt+"Key-exclam>":"one",
    alt+"at>":"",
    alt+"numbersign>":"",
    alt+"dollar>":"ill",
    alt+"percent>":"which",
    alt+"asciicircum>":"ism",
    alt+"ampersand>":"was",
    alt+"asterisk>":"ore",
    alt+"parenleft>":"pre",
    alt+"parenright>":"", #not working?
    alt+"minus>":"les",
    alt+"underscore>":"end",
    alt+"plus>":"tune",
    alt+"equal>":"ake",
    
    alt+"bracketleft>":"before",
    alt+"bracketright>":"after",
    alt+"braceleft>":"those",
    alt+"braceright>":"them",
    alt+"bar>":"tch",
    alt+"backslash>":"against",

    alt+"semicolon>":"est",
    alt+"colon>":"cap",
    alt+"quoteright>":"ose",
    alt+"quotedbl>":"icle",

    alt+"less>":"ick",
    alt+"greater>":"out",
    alt+"slash>":"ned",
    alt+"question>":"ike",
#    these are reserved
#    ctrl+"comma>":"",
#    ctrl+"period>":"",
    
    # ctrl+"!>":"", ctrl'">':'', ctrl"#>":"", ctrl"$>":"", ctrl"%>":"",
    # ctrl+"&>":"", ctrl"'>":"", ctrl"(>":"", ctrl")>":"", ctrl"*>":"",
    # ctrl+"+>":"", ctrl",>":"", ctrl"->":"", ctrl".>":"", ctrl"/>":"",
    # ctrl+":>":"", ctrl";>":"", ctrl"=>":"", ctrl">>":"", ctrl"?>":"",
    # ctrl+"@>":"", ctrl"[>":"", ctrl"\\>":"", ctrl"]>":"", ctrl"^>":"",
    # ctrl+"_>":"", ctrl"`>":"", ctrl"{>":"", ctrl"|>":"", ctrl"}>":"",
    # ctrl+"~>":""

#    # Little-known feature of Tk, it allows to bind an event to
#    # multiple keystrokes
#    self.bind("<Control-Key-%s><Key>" % k,
#              lambda event, a=a: self.insert_accented(event.char, a))

    #< and > might need special binding
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
    ":":":", ";":";", "=":"=", ">":">", #"<":"<", 
    "?":"?", "@":"@", "[":"[", "\\":"\\", "]":"]",
    "^":"^", "_":"_", "`":"`", "{":"{", "|":"|",
    "}":"}", "~":"~"
}
