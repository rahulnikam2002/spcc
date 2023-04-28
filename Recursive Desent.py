print("Recursive Desent Parsing For following grammar\n")
print("E->TE'\nE'->+TE'/@\nT->FT'\nT'->*FT'/@\nF->(E)/i/n\n")
print("Enter the string want to be checked\n")
global string
string = list(input())
global index
index = 0


def match(a):
  global string
  global index
  if (index >= len(string)):
    return False
  elif (string[index] == a):
    index += 1
    return True
  else:
    return False


def F():
  if (match('(')):
    if (E()):
      if (match(')')):
        return True
      else:
        return False
    else:
      return False
  elif (match('i')):
    return True
  elif(match('n')):
    return True
  else:
    return False


def Tx():
  if (match('*')):
    if (F()):
      if (Tx()):
        return True
      else:
        return False
    else:
      return False
  else:
    return True


def T():
  if (F()):
    if (Tx()):
      return True
    else:
      return False
  else:
    return False


def Ex():
  if (match('+')):
    if (T()):
      if (Ex()):
        return True
      else:
        return False
    else:
      return False
  else:
    return True


def E():
  if (T()):
    if (Ex()):
      return True
    else:
      return False
  else:
    return False


if (E()):
  if (index == len(string)):
    print('\nString is accepted')
  else:
    print('\nString is not accepted')
else:
  print('String is not accepted')


















# Aim : Implementation of Recursive Descent Parser.
# Theory :
# 14

# The Top-Down parsing technique parses the input, and starts constructing a parse
# tree from the root node gradually moving down to the leaf nodes. The types of
# top-down parsing are depicted below:
# Recursive Descent Parsing
# Recursive descent is a top-down parsing technique that constructs the parse tree
# from the top and the input is read from left to right. It uses procedures for every
# terminal and non-terminal entity. This parsing technique recursively parses the input
# to make a parse tree, which may or may not require back-tracking. But the grammar
# associated with it (if not left factored) cannot avoid back-tracking. A form of
# recursive-descent parsing that does not require any back-tracking is known as
# predictive parsing.
# This parsing technique is regarded as recursive as it uses context-free grammar
# which is recursive in nature.
# 15

# Back-tracking
# Top- down parsers start from the root node (start symbol) and match the input string
# against the production rules to replace them (if matched). To understand this, take the
# following example of CFG:
# S → rXd | rZd
# X → oa | ea Z
# For an input string: read, a top-down parser, will behave like this:
# For an input string: read, a top-down parser, will behave like this:
# It will start with S from the production rules and will match its yield to the left-most
# letter of the input, i.e. ‘r’. The very production of S (S → rXd) matches with it. So the
# top-down parser advances to the next input letter (i.e. ‘e’). The parser tries to expand
# non-terminal
# X’ and checks its production from the left (X → oa). It does not match with the next
# input symbol. So the top-down parser backtracks to obtain the next production rule of
# X, (X → ea).
# Now the parser matches all the input letters in an ordered manner. The string is
# accepted.
# Predictive Parser
# 16

# Predictive parser is a recursive descent parser, which has the capability to predict
# which production is to be used to replace the input string. The predictive parser does
# not suffer from backtracking.
# To accomplish its tasks, the predictive parser uses a look-ahead pointer, which points
# to the next input symbols. To make the parser back-tracking free, the predictive
# parser puts some constraints on the grammar and accepts only a class of grammar
# known as LL(k) grammar.
# Predictive parsing uses a stack and a parsing table to parse the input and generate a
# parse tree. Both the stack and the input contains an end symbol $ to denote that the
# stack is empty and the input is consumed. The parser refers to the parsing table to
# take any decision on the input and stack element combination.
# 17

# In recursive descent parsing, the parser may have more than one production to
# choose from for a single instance of input, whereas in predictive parser, each step
# has at most one production to choose. There might be instances where there is no
# production matching the input string, making the parsing procedure to fail.
# LL Parser
# An LL Parser accepts LL grammar. LL grammar is a subset of context-free grammar
# but with some restrictions to get the simplified version, in order to achieve easy
# implementation. LL grammar can be implemented by means of both algorithms
# namely, recursive-descent or table-driven.
# LL parser is denoted as LL(k). The first L in LL(k) is parsing the input from left to
# right, the second L in LL(k) stands for left-most derivation and k itself represents the
# number of look aheads. Generally k = 1, so LL(k) may also be written as LL(1).



# input = i+n



