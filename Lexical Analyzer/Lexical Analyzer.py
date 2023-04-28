
import re
workfile = input("Enter Python file (.py) fullname: ")


puncList = [".", ";", ":", "!", "?", "/", "\\", ",", "@", "$", "&", ")", "(", "\"", "#",
            "[", "]", "{", "}", "=", "+=", "-=", "*=", "/=", "//=", "%=", "&=", "|=",
            "^=", ">>=", "<<=", "**=", "+", '-', '==', "->"]


keyword = ['int', 'char', 'float', 'double', 'long', 'short', 'void', 'if', 'else', 'switch', 'case', 'default', 'for', 'while', 'do', 'break', 'continue', 'return',
           'struct', 'typedef', 'enum', 'union', 'const', 'static', 'extern', 'volatile', 'register', 'sizeof', 'NULL', "#define", "#include", "#ifdef", "ifndef", "#endif"]


lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
             "p", "q", "r", "s", "t", "u", "v", "w", "x", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
             "S", "T", "U", "V", "W", "X", "Y", "Z"]
digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "_"]


def is_punc(a):
    if a in puncList:
        return True
        return a in puncList


def is_keyword(a):
    if a in keyword:
        print('<Keyword, "%s"' % (a))
    return a in keyword


def is_ID(a, cnt):
    try:
        a.index('"')
        return False
    except:
        pass
    try:
        a.index("'")
        return False
    except:
        pass
    try:
        int(a[0])
        return False
    except:
        pass
        k = all(i in digit or uppercase or lowercase for i in a)
        if k:
            print('<ID , "%s" , "%s">' % (a, cnt))
        return k


try:
    fin = open(workfile, 'r')
except:
    print("Input file does not exists: %s" % workfile)
    quit(0)


lines = fin.readlines()
if len(lines) <= 0:
    print("Input file %s is empty" % workfile)
    quit(0)


def breakup_line(line):
    words = line.split()
    newwords = []
    for i in range(len(words)):
        if words[i][0] in ("'", '"') and words[i][-1] in ("'", '"'):
            newwords.append(words[i])
        else:
            t = re.findall(r"[\w]+|[^\s\w]|[-:\w]", words[i])
            newwords.extend(t)
    return newwords


def get_strings(words):
    new_words = []
    adding = False
    tmpstring = ''
    skip = False
    for w in words:
        if ('"' in w or "'" in w) and (w.count('"') < 2 and w.count("'") < 2):
            adding = not adding
        if not adding:
            new_words.append(tmpstring+w)
            tmpstring = ''
            skip = True
        if adding:
            tmpstring += w + ' '
        else:
            if skip:
                skip = False
            else:
                new_words.append(w)
    return new_words


skip = False
cnt = 0
print("<Category , Words , Inner Code>")
for line in lines:
    if '#' in line:
        line = line[:line.index('#')]
    tokens = breakup_line(line)
    final = get_strings(tokens)

    for c, item in enumerate(final):
        cnt += 1
        if not skip:
            if is_punc(item):
                try:
                    if is_punc(item + final[c+1]):
                        print('<PUNC , "%s">' %
                              (str(item + final[c+1])))
                        skip = True
                    else:
                        print('<PUNC , "%s">' % (item))
                except:
                    print('<PUNC , "%s">' % (item))
            elif is_keyword(item, cnt):
                pass
            elif is_ID(item, cnt):
                pass
            else:
                print('<LIT , "%s">' % (item))
        else:
            skip = False
print("<END OF FILE>")
