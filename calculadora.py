#!/usr/bin/python3

import sys
from sys import argv

if len(argv) != 4:
    sys.exit("Número de argumentos inválido.")

operacion = argv[1]

try:
    op1 = float(argv[2])
    op2 = float(argv[3])
except ValueError:
    sys.exit("Tipo de operando inválido, solo es posible int o float.")

if operacion == "sumar":
    print(op1, "+", op2, "=", op1+op2)
elif operacion == "restar":
    print(op1, "-", op2, "=", op1-op2)
elif operacion == "multiplicar":
    print(op1, "*", op2, "=", op1*op2)
elif operacion == "dividir":
    if op2 == 0:
        sys.exit('No se puede dividir entre 0.')
    else:
        print(op1, "/", op2, "=", op1/op2)
else:
    sys.exit('Esta operación no está contemplada.')  
