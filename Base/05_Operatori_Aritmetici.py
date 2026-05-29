"""
Operatori Aritmetici
+ (somma), 
- (sottrazione), 
* (moltiplicazione), 
/ (divisione), 
// (divisione intera), 
% (modulo), 
** (potenza)
"""
num1 = int(input("Inserisci il primo numero da 0 a 1000000: "))
num2 = int(input("Inserisci il secondo numero da 0 a 1000000: "))

result_somma = num1 + num2
result_sottrazione = num1 - num2
result_moltiplicazione = num1 * num2
result_divisione = num1 / num2
result_divisione_intera = num1 // num2
result_modulo = num1 % num2
result_potenza = num1 ** num2
print(f"Il risultato della somma è: {result_somma}")
print(f"Il risultato della sottrazione è: {result_sottrazione}")
print(f"Il risultato della moltiplicazione è: {result_moltiplicazione}")
print(f"Il risultato della divisione è: {result_divisione}")
print(f"Il risultato della divisione intera è: {result_divisione_intera}")
print(f"Il risultato del modulo è: {result_modulo}")
print(f"Il risultato della potenza è: {result_potenza}")0