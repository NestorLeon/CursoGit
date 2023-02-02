def IsAñoBisiesto(año):
    r1 = año % 4
    r2 = año % 100
    r3 = año % 400
    if not r1 == 0:
        return False
    elif not r2 == 0:
        return True
    elif not r3 == 0:
        return False
    else:
        return True

def CantidadDeDias(mes):
    match mes:
        case 1:
            return 0
        case 2:
            return 31
        case 3:
            return 31+28
        case 4:
            return 31+28+31
        case 5:
            return 31+28+31+30
        case 6:
            return 31+28+31+30+31
        case 7:
            return 31+28+31+30+31+30
        case 8:
            return 31+28+31+30+31+30+31
        case 9:
            return 31+28+31+30+31+30+31+31
        case 10:
            return 31+28+31+30+31+30+31+31+30
        case 11:
            return 31+28+31+30+31+30+31+31+30+31
        case 12:
            return 31+28+31+30+31+30+31+31+30+31+30

def DiasTranscurridos(año, mes, dia):
    dm = CantidadDeDias(mes)
    ab = 0
    if IsAñoBisiesto(año):
        ab = 1
    return dm + ab
    
x = DiasTranscurridos(2000, 12, 3)
print(x)