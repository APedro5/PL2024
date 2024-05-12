# TP6
## António Pedro Azevedo Ribeiro Cardoso, a100821
# 
## Gramática Independente do Contexto
Gramática independente do contexto para a seguinte linguagem:
    ? a
    b = a * 2 / (27 - 3)
    ! a + b
    c = a * b / (a / b)
A gramática definida foi:

    ```
    T =  {'?', '!', '=', '+', '-', '*', '/', '(', ')', id, num}

    N = {S, Exp1, Exp2, Exp3, Op1, Op2}

    S = S

    P = {
    
        S -> '?' id             LA = {'?'}
        | '!' Exp1              LA = {'!'}
        | id '=' Exp1           LA = {id}

        Exp1 -> Exp2 Op1        LA = {'(', num, id}

        Op1 -> '+' Exp1         LA = {'+'}
            | '-' Exp1          LA = {'-'}
            | &                 LA = {')', $}

        Exp2 -> Exp3 Op2        LA = {'(', num, id}

        Op2 -> '*' Exp2         LA = {'*'}
            | '/' Exp2          LA = {'/'}
            | &                 LA = {'+', '-', ')', $}

        Exp3 -> '(' Exp1 ')'    LA = {'('}
            | num               LA = {num}
            | id                LA = {id}

    } ```