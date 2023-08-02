import math

hexDecimal = {
    "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,
    "A": 10, "B":11, "C":12, "D":13, "E":14, "F": 15
}
def hexToDec(hexNum):
    
    decimal = 0;
    brojac = 0;
    lista = list();

    if len(hexNum) > 3:
        return None;

    for i in hexDecimal:
        lista.append(i);
    
    for i in hexNum:
        if i not in lista:
            return None;

    for i in hexNum:
        for j in range(0, len(hexDecimal)):
            if i == lista[j]:
                decimal += hexDecimal[i] * pow(16, len(hexNum)-1-brojac);
                brojac += 1;

            
        
    
    return round(decimal, 2);

print(hexToDec("FFF"));