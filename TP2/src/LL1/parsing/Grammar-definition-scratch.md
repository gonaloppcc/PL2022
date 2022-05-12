# Test case

```
Tokens:
num \d+
id [a-zA-Z_]\w*
fIM s
empty s

Programa:
Comandos fIM

Comandos:
empty                        
Comando Comandos

Comando:
Atrib
Print
Read

Atrib:
id '=' Exp

Print:
'!' Exp

Read:
'?' id

Exp:
Termo Exp2                          
```

---

# Grammar definition

```
Grammar -> STATES TOKENS ':' NEW_LINE Tokens NonTerminalList

STATES -> state ':'NEW_LINE  StatesList 
      | 

StatesList -> StatesList name Type NEW_LINE 
              | name Type NEW_LINE 

Type -> incl
      | excl


Imports -> Imports Import NEW_LINE

Tokens -> Tokens token NEW_LINE 
        | empty

NonTerminalList -> NonTerminalList NTerminal
            | NTerminal
            
NTerminal -> '-' NT ':' NEW_LINE Productions NEW_LINE

Productions -> Productions NEW_LINE Production
       | Production

Production -> Production Simb
           | Simb

Simb -> EMPTY
      | literal
      | NT
      | token

```

---

# Abstract Syntax Tree (AST)

```md
(Tokens, Productions)

Tokens : {token : rexpr} # TODO: Do we need to separate de literals from the tokens?
Literals : [str]

Non-terminal : {non-terminal : [Production]}

States : {Name : InOrOut}

Production : [Simb]

[Simb] -> token | literal | NT | EMPTY
```
