import re
import os
import string
import urllib
from datetime import datetime
from os import path

class isValid:

    def NIF(nif):
        # verificar se é apenas inteiro
        if not isValid.INT(nif) :
            return '-1'
        # verificar tamanho do número passado
        if len(nif) != 9:
            return '-1'

        # verificar validade do carácter inicial do NIF
        if nif[0] not in "125689":
            return '-1'

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
        
        if (sum % 11 and (11 - sum % 11) % 10) == num[-1]:
            rslt = 'True'
        else:
            rslt = '-2'

        return rslt
    
    def NCC(str):
        str = str.replace(" ", "")
        upperCaseStr = str.upper()
        sum = 0
        secondDigit = 0
        
        if len(str) != 12:
            return '-1'

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
                result = 'True'
            else:
                result = '-2'
            
        return result

    def DATE(date):
        
        try:
            LastTime = datetime.strptime(date,"%Y %m %d %H %M %S")
        except ValueError:
            return '-1'

        if datetime.timestamp(LastTime) <= datetime.timestamp( datetime.now() ):
            return 'True'
        else:
            return '-2'

    def IDF(str,url):
        if re.search("(^[1-9]\d{0}[0-9]{,7})+$", str):
            if inFile.exist(str,0,url) :
                boo = '-2'
            else:
                boo = 'True'
        else:
            return '-1'

        return boo
    def IDC(str):
        if re.search("(^[1-9]\d{0}[0-9]{,7})+$", str) :
            link = "https://cloud.sysnovare.pt/ipg/unidades_geral.lista_nivel?p_nivel_id="+str
            f = urllib.urlopen(link)
            myfile = f.read()
        else:
            return '-1'

    def INT(str):
        try:
            int(str)
            return True
        except ValueError:
            return False



class inFile:
    def NextLine(url):
        if path.exists(url):
            n = sum(1 for line in open(url))
        else:
            n = 0

        return n + 1

    def exist(data,pos,url,sep=";"):
        with open(url) as fp:
            line = fp.readline()
            boo = False
            while line:
                if line.split(sep)[pos] == data:
                    boo = True
                line = fp.readline()
            return boo

class Algrthm:
    def CDF(url):
        CAT = ''
        char = ["A","B","C","D","E","F","G",
                "H","I","J","K","L","M","N",
                "O","P","Q","R","S","T","U",
                "V","W","X","Y","Z"]
        ln = inFile.NextLine(url)
        i = 0
        while ln != 0:
            tmp = (ln % 26)-1
            CAT = CAT + char[tmp]
            i = i + 1
            ln = int(ln/26)

        return CAT