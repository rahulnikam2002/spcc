import re

digit_pattern = r'[0-9]'
letter_pattern = r'[a-zA-Z]'

dcount = 0
ccount = 0

with open('hii.txt', 'r') as fp:
    for line in fp:
        digit_matches = re.findall(digit_pattern, line)
        letter_matches = re.findall(letter_pattern, line)
        
        for match in digit_matches:
            dcount += 1
            print(f'\n\n{match} is a digit')
        
        for match in letter_matches:
            ccount += 1
            print(f'\n\n{match} is a character')
        
print(f'\n {dcount} no of digits are there')
print(f'\n {ccount} no of characters are there')




















# Theory :
# Lex is officially known as a "Lexical Analyzer". Its main job is to break up an input
# stream into more meaningful units, or tokens. For example, consider breaking a text file
# up into individual words. More pragmatically, Lex is a tool for automatically generating a
# lexer ( also known as scanner) starting from a lex specification.
# Lex specifications :
# A Lex program (the .l file ) consists of three parts:
# declarations
# %%
# translation rules
# %%
# auxiliary procedures
# 1. The declarations section includes declarations of variables, manifest constants
# (A manifest constant is an identifier that is declared to represent a constant. e.g.
# # define PIE 3.14), and regular definitions.
# 2. The translation rules of a Lex program are statements of the form :
# p1 {action 1}
# p2 {action 2}
# p3 {action 3}
# … …
# … …
# where each p is a regular expression and each action is a program fragment
# describing what action the lexical analyzer should take when a pattern p matches
# a lexeme. In Lex the actions are written in C.
# 19

# 3. The third section holds whatever auxiliary procedures are needed by the actions.
# Alternatively, these procedures can be compiled separately and loaded with the
# lexical analyzer.
# A Lex program has the following form :
# declarations
# %%
# translation rules
# %%
# auxiliary functions
# The declarations section includes declarations of variables, manifest constants and
# regular definitions.
# The translation rules each have the form Pattern { Action }
# Each pattern is a regular expression, which may use the regular definitions of the
# declaration section. The actions are fragments of code, typically written in C, although
# many variants of Lex using other languages have been created.
# STEP BY STEP PROCEDURE FOR RUNNING A LEX AND YACC PROGRAM
# For compiling a lex program
# 1. write the lex program in a file and save it as file.l (where file is the name of the
# file).
# 2. open the terminal and navigate to the directory where you have saved the file.l
# 3. type - lex file.l
# 4. then type - cc lex.yy.c
# 5. then type - ./a.out or a.exe
# For compiling lex and yacc together
# 1. write lex program in a file file.l and yacc in a file file.y
# 2. open the terminal and navigate to the directory where you have saved the files.
# 3. type lex file.l
# 20
# 
# 4. type yacc file.y
# 5. type cc lex.yy.c y.tab.h
# 6. type ./a.out or a.exe
