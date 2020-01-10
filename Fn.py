import string

class isValid:

    def NIF(nif):
        # verificar tamanho do número passado
        if len(nif) != 9:
            return False

        # verificar validade do carácter inicial do NIF
        if nif[0] not in "125689":
            return False

        numstr = nif
        acceptX=0
        res = []
        # converter todos os dígitos
        for i in numstr:
            if i in string.digits:
                res.append(int(i))

        # converter dígito de controlo no ISBN
        if acceptX and (numstr[-1] in 'Xx'):
            res.append(10)

        num = res
        sum = 0
        for pos, dig in enumerate(num[:-1]):
            sum += dig * (9 - pos)
        
        return (sum % 11 and (11 - sum % 11) % 10) == num[-1]
    
    def NCC(str):
        str = str.replace(" ", "")
        upperCaseStr = str.upper()
        sum = 0
        secondDigit = 0
        
        if len(str) != 12:
            return 0

        for i in range(len(str) - 1, -1, -1):
            valor = upperCaseStr[i]
            
            charDict = {
            "0" : "0",
            "1" : "1",
            "2" : "2",
            "3" : "3",
            "4" : "4",
            "5" : "5",
            "6" : "6",
            "7" : "7",
            "8" : "8",
            "9" : "9",
            "A" : "10",
            "B" : "11",
            "C" : "12",
            "D" : "13",
            "E" : "14",
            "F" : "15",
            "G" : "16",
            "H" : "17",
            "I" : "18",
            "J" : "19",
            "K" : "20",
            "L" : "21",
            "M" : "22",
            "N" : "23",
            "O" : "24",
            "P" : "25",
            "Q" : "26",
            "R" : "27",
            "S" : "28",
            "T" : "29",
            "U" : "30",
            "V" : "31",
            "W" : "32",
            "X" : "33",
            "Y" : "34",
            "Z" : "35",
            }
            valor = int(charDict[valor])
            if secondDigit == 1:
                valor = valor * 2
                if valor > 9:
                    valor = valor - 9
            sum = sum + valor
            secondDigit = 1 if secondDigit == 0 else 0
        
            if (sum % 10) == 0 :
                result = True
            else:
                result = False
            
        return result

    def DATE(date):
        return True

class inFile:
    def NextLine(url):
        return sum(1 for line in open(url)) + 1