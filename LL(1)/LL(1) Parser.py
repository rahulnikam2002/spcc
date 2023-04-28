from collections import OrderedDict

def isterminal(char):
    if(char.isupper() or char == "#"):
        return False
    else:
        return True

def insert(grammar, lhs, rhs):
    if(lhs in grammar and rhs not in grammar[lhs] and grammar[lhs] != "null"):
        grammar[lhs].append(rhs)
    elif(lhs not in grammar or grammar[lhs] == "null"):
        grammar[lhs] = [rhs]
    return grammar
	
def first(lhs, grammar, grammar_first):
    rhs = grammar[lhs]
    for i in rhs:
        k = 0
        flag = 0
        current = []
        confirm = 0
        flog = 0
        if(lhs in grammar and "#" in grammar_first[lhs]):
            flog = 1
        while(1):	
            check = []
            if(k>=len(i)):
                if(len(current)==0 or flag == 1 or confirm == k or flog == 1):
                    grammar_first = insert(grammar_first, lhs, "#")
                break				
            if(i[k].isupper()):
                if(grammar_first[i[k]] == "null"):
                    grammar_first = first(i[k], grammar, grammar_first)
                 
                for j in grammar_first[i[k]]:
                    grammar_first = insert(grammar_first, lhs, j)
                    check.append(j)
            else:
                grammar_first = insert(grammar_first, lhs, i[k])
                check.append(i[k])
            if(i[k]=="#"):
                flag = 1
            current.extend(check)
            if("#" not in check):
                if(flog == 1):
                    grammar_first = insert(grammar_first, lhs, "#")
                break
            else:
                confirm += 1
                k+=1
                grammar_first[lhs].remove("#")
    return(grammar_first)

def rec_follow(k, next_i, grammar_follow, i, grammar, start, grammar_first, lhs):
    if(len(k)==next_i):
        if(grammar_follow[i] == "null"):
            grammar_follow = follow(i, grammar, grammar_follow, start)
        for q in grammar_follow[i]:
            grammar_follow = insert(grammar_follow, lhs, q)
    else:
        if(k[next_i].isupper()):
            for q in grammar_first[k[next_i]]:
                if(q=="#"):
                    grammar_follow = rec_follow(k, next_i+1, grammar_follow, i, grammar, start, grammar_first, lhs)		
                else:
                    grammar_follow = insert(grammar_follow, lhs, q)
        else:
            grammar_follow = insert(grammar_follow, lhs, k[next_i])

    return(grammar_follow)

def follow(lhs, grammar, grammar_follow, start):
    for i in grammar:
        j = grammar[i]
        for k in j:
            if(lhs in k):
                next_i = k.index(lhs)+1
                grammar_follow = rec_follow(k, next_i, grammar_follow, i, grammar, start, grammar_first, lhs)
    if(lhs==start):
        grammar_follow = insert(grammar_follow, lhs, "$")
    return(grammar_follow)

def show_dict(dictionary):
    for key in dictionary.keys():
        print(key+"  :  ", end = "")
        for item in dictionary[key]:
            if(item == "#"):
                print("Epsilon, ", end = "")
            else:
                print(item+", ", end = "")
        print("\b\b")

def get_rule(non_terminal, terminal, grammar, grammar_first):
    for rhs in grammar[non_terminal]:
        #print(rhs)
        for rule in rhs:
            if(rule == terminal):
                string = non_terminal+"~"+rhs
                return string
            
            elif(rule.isupper() and terminal in grammar_first[rule]):
                string = non_terminal+"~"+rhs
                return string
                
def generate_parse_table(terminals, non_terminals, grammar, grammar_first, grammar_follow):
    parse_table = [[""]*len(terminals) for i in range(len(non_terminals))]
    
    for non_terminal in non_terminals:
        for terminal in terminals:
            #print(terminal)
            #print(grammar_first[non_terminal])
            if terminal in grammar_first[non_terminal]:
                rule = get_rule(non_terminal, terminal, grammar, grammar_first)
             
            elif("#" in grammar_first[non_terminal] and terminal in grammar_follow[non_terminal]):
                rule = non_terminal+"~#"
                
            elif(terminal in grammar_follow[non_terminal]):
                rule = " "
                
            else:
                rule = ""
                
            parse_table[non_terminals.index(non_terminal)][terminals.index(terminal)] = rule
        
    return(parse_table)

def display_parse_table(parse_table, terminal, non_terminal):
    print("\t\t\t\t",end = "")
    for terminal in terminals:
        print(terminal+"\t\t", end = "")
    print("\n\n")
    
    for non_terminal in non_terminals:
        print("\t\t"+non_terminal+"\t\t", end = "")
        for terminal in terminals:
            print(parse_table[non_terminals.index(non_terminal)][terminals.index(terminal)]+"\t\t", end = "")
        print("\n")

def parse(expr, parse_table, terminals, non_terminals):
    stack = ["$"]
    Input = ["$"]
    stack.insert(0, non_terminals[0])

    print("\t\t\tMatched\t\t\tStack\t\t\tInput\t\t\tParsing Table Entry\n")
    print("\t\t\t-\t\t\t", end = "")
    for i in stack:
        print(i,  end = "")
    print("\t\t\t", end = "")
    print(expr+"\t\t\t", end = "")
    print(" ")

    matched = "-"
    while(True):
        action = "-"

        if(stack[0] == expr[0] and stack[0] == "$" and Input[0] == "$"):
            print("\t\t\t\t\t\t\t\t\t\t\t\tAccept")
            print("\t\tThe given string ", expr2, "is Accepted.")
            break

        elif(stack[0] == expr[0]):
            if(matched == "-"):
                matched = expr[0]
            else:    
                matched = matched + expr[0]
            action = "Matched "+expr[0]
            expr = expr[1:]
            stack.pop(0)
        
        else:
            action = parse_table[non_terminals.index(stack[0])][terminals.index(expr[0])]
            stack.pop(0)
            i = 0
            for item in action[2:]:
                if(item != "#"):
                    stack.insert(i,item)
                i+=1

        print("\t\t\t"+matched+"\t\t\t", end = "")
        for i in stack:
            print(i,  end = "")
        print("\t\t\t", end = "")
        print(expr+"\t\t\t", end = "")
        print(action)
grammar = OrderedDict()
grammar_first = OrderedDict()
grammar_follow = OrderedDict()

f = open('grammar.txt')
for i in f:
    i = i.replace("\n", "")
    lhs = ""
    rhs = ""
    flag = 1
    for j in i:
        if(j=="~"):
            flag = (flag+1)%2
            continue
        if(flag==1):
            lhs += j
        else:
            rhs += j
    grammar = insert(grammar, lhs, rhs)
    grammar_first[lhs] = "null"
    grammar_follow[lhs] = "null"

print("Grammar\n")
show_dict(grammar)

for lhs in grammar:
    if(grammar_first[lhs] == "null"):
        grammar_first = first(lhs, grammar, grammar_first)
        
print("\n\n\n")
print("First\n")
show_dict(grammar_first)

start = list(grammar.keys())[0]
for lhs in grammar:
    if(grammar_follow[lhs] == "null"):
        grammar_follow = follow(lhs, grammar, grammar_follow, start)
        
print("\n\n\n")
print("Follow\n")
show_dict(grammar_follow)

non_terminals = list(grammar.keys())
terminals = []

for i in grammar:
    for rule in grammar[i]:
        for char in rule:
            
            if(isterminal(char) and char not in terminals):
                terminals.append(char)

terminals.append("$")

print("\n\n\n\n\t\t\t\t\t\t\tParse Table\n\n")
parse_table = generate_parse_table(terminals, non_terminals, grammar, grammar_first, grammar_follow)
display_parse_table(parse_table, terminals, non_terminals)

expr = input("\n\n\n\t\tEnter the expression ending with $ : ")
expr2= expr
# expr = "i+i*i$"

print("\n\n\n")
print("\t\t\t\t\t\tParsing Expression\n\n")
parse(expr, parse_table, terminals, non_terminals)












# Theory :
# LL(1) Parser :
# 10

# LL(1) parsing is a top-down parsing method in the syntax analysis phase of compiler
# design. Required components for LL(1) parsing are input string, a stack, parsing table
# for given grammar, and parser. Here, we discuss a parser that determines whether a
# given string can be generated from a given grammar(or parsing table) or not.
# Let given grammar is G = (V, T, S, P)
# where V-variable symbol set, T-terminal symbol set, S- start symbol, P- production set.
# LL(1) Grammer :
# The first ‘L’ in LL(1) stands for scanning the input from left to right, the second ‘L’ stands
# for producing a leftmost derivation, and the ‘1’ for using one input symbol of lookahead
# at each step to make parsing action decisions. LL(1) grammar follows the Top-down
# parsing method. For a class of grammars called LL(1) we can construct a grammar
# predictive parser. That works on the concept of recursive-descent parser not requiring
# backtracking.
# Elimination of Left Recursion
# A grammar is left recursive if it has a nonterminal A such that there is a derivation A →
# A α | β. Top-down parsing methods cannot handle left-recursive grammars, so a
# transformation is needed to eliminate left recursion. Left recursion can be eliminated by
# modifying the rule as follows: (A’ is new non-terminal and ε is representing epsilon).
# A → β A’
# A’ → α A’ | ε
# Left Factoring
# It is a grammar transformation that is useful for producing grammar suitable for
# predictive or top-down parsing. When the choice between two alternative productions is
# not clear, we rewrite the productions to defer the decision to make the right choice.
# For example, if we have grammar rule A → α β1 | α β2
# A → α A’
# A’ → β1 | β2
# 11

# Concept of First and Follow
# The construction of a top-down parser is aided by FIRST and FOLLOW functions, that
# are associated with a grammar G. During top-down parsing, FIRST and FOLLOW allow
# us to choose which production to apply, based on the next input symbol.
# Rules for First computation :
# 1. If x is terminal, then FIRST(x)={x}
# 2. If X→ ε is production, then add ε to FIRST(X)
# 3. If X is a non-terminal and X → PQR then FIRST(X)=FIRST(P)
# 4. If FIRST(P) contains ε, then
# FIRST(X) = (FIRST(P) – {ε}) U FIRST(QR)
# Rules for Follow computation :
# Epsilon (ε) can never be present in the FOLLOW of any non-terminal symbol.
# 1. For Start symbol, place $ in FOLLOW(S)
# 2. If A→ α B, then FOLLOW(B) = FOLLOW(A)
# 3. If A→ α B β, then
# If ε not in FIRST(β),
# FOLLOW(B) = FIRST(β)
# else do,
# FOLLOW(B) = (FIRST(β)-{ε}) U FOLLOW(A)
# Parsing table :
# After the construction of the parsing table, if for any non-terminal symbol in the table we
# have more than one production rule for any terminal symbol in the table column the
# grammar is not LL(1). Otherwise, then grammar is considered as LL(1).
# Rules for construction of parsing table :
# 12

# Step 1 : For each production A → α , of the given grammar perform Step 2 and Step 3.
# Step 2 : For each terminal symbol ‘a’ in FIRST(α), ADD A → α in table T[A,a], where ‘A’
# determines row & ‘a’ determines column.
# Step 3 : If ε is present in FIRST(α) then find FOLLOW(A), ADD A → ε, at all columns
# ‘b’, where ‘b’ is FOLLOW(A). (T[A,b])
# Step 4 : If ε is in FIRST(α) and $ is the FOLLOW(A), ADD A → α to T[A,$].
# The assumption made in code :
# a. The LHS symbol of the First rule is considered as the start symbol.
# b. ‘#’ represents the epsilon symbol.
# LL(1) Parser algorithm :
# Input1. stack = S //stack initially contains only S.
# input string = w$
# 2. where S is the start symbol of grammar, w is given string, and $ is used for
# the end of string.
# 3. PT is a parsing table of given grammar in the form of a matrix or 2D array.
# Output- determines that given string can be produced by given grammar(parsing table)
# or not, if not then it produces an error.
# Steps :
# 1. while(stack is not empty) {
# // initially it is S
# 2. A = top symbol of stack;
# 13

# //initially it is first symbol in string, it can be $ also
# 3. r = next input symbol of given string;
# 4. if (A∈T or A==$) {
# 5. if(A==r){
# 6. pop A from stack;
# 7. remove r from input;
# 8. }
# 9. else
# 10. ERROR();
# 11. }
# 12. else if (A∈V) {
# 13. if(PT[A,r]= A⇢B1B2....Bk) {
# 14. pop A from stack;
# // B1 on top of stack at final of this step
# 15. push Bk,Bk-1......B1 on stack
# 16. }
# 17. else if (PT[A,r] = error())
# 18. error();
# 19. }
# 20. }
# // if parser terminate without error()
# // then given string can generated by given parsing table.
