import re
import os
import string
import urllib
import json
from datetime import datetime
import os.path
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

    def IDF(str, url = 'Dados/Funcionarios.csv'):
        if re.search("(^[1-9]\d{0}[0-9]{,7})+$", str):
            if inFile.exist(str,0,url) :
                boo = '-2'
            else:
                boo = 'True'
        else:
            return '-1'

        return boo

    def IDC(str, url = 'Dados/Categorias.csv'):
        if re.search("(^[1-9]\d{0}[0-9]{,7})+$", str):
            if inFile.exist(str,0,url,' ') :
                boo = 'True'
            else:
                boo = '-2'
        else:
            return '-1'
        
        return boo
    
    def IDT(str, url = 'Dados/Titulos.csv'):
        if re.search("(^[1-9]\d{0}[0-9]{,7})+$", str):
            if inFile.exist(str,0,url,'.') :
                boo = 'True'
            else:
                boo = '-2'
        else:
            return '-1'
        
        return boo
    
    def IDS(str, url = 'Dados/Servicos.csv'):
        if re.search("(^[1-9]\d{0}[0-9]{,7})+$", str):
            if inFile.isset(str,0,url) :
                boo = 'True'
            else:
                boo = '-2'
        else:
            return '-1'
        
        return boo
    
    def IDFC(str, url = 'Dados/Funcionarios.csv'):
        if re.search("(^[1-9]\d{0}[0-9]{,7})+$", str):
            if inFile.exist(str,0,url) :
                boo = 'True'
            else:
                boo = '-2'
        else:
            return '-1'

        return boo

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
        if not path.exists(url):
            return False

        with open(url) as fp:
            line = fp.readline()
            boo = False
            while line:
                if line.split(sep)[pos] == data:
                    boo = True
                line = fp.readline()
            return boo
    
    def line(pos,url):
        if not path.exists(url):
            return False
        f = open(url, "r", encoding="utf-8")
        str = f.read()
        f.close()
        arr = str.split('\n')
        ln = len(arr)-1
        pos = int(pos)
        if pos > ln:
            pos = ln
        elif pos < 0:
            pos = 0
        return arr[pos]

    def read(url):
        if not path.exists(url):
            return ''
        f = open(url, "r", encoding="utf-8")
        str = f.read()
        return str

    def isset(data, pos, url = ''):
        f = open(url, "r", encoding="utf-8")
        str = f.read()
        boo = False
        num = len(str.split("("))-1
        #try open array
        str = str.split("]")[0].split("[")[1]
        #try do step by step
        while num > 0:
            num = num - 1
            slc = str.split(")")[num].split("(")[1]
            if slc.split(".")[pos].replace('"','') == data:
                boo = True
        return boo

    def update(id, arr, url):
        f = open(url, 'rt', encoding='utf-8')
        rows = f.readlines()
        f.close()
        cat = ''
        
        for r in rows:
            r = r.rstrip('\n')
            tmp = r.split(';')
            if tmp[0] == id :
                for x in range(0,len(arr)):
                    if len(arr[x]) > 0 :
                        tmp[x] = arr[x]
                cat = cat + ";".join(tmp) + '\n'
            else:
                cat = cat + r + '\n'
                continue

        f = open(url, 'wt', encoding='utf-8')
        f.write(cat)
        f.close()

    def delete(id, url):
        f = open(url, 'rt', encoding='utf-8')
        rows = f.readlines()
        f.close()
        cat = ''
        
        for r in rows:
            r = r.rstrip('\n')
            tmp = r.split(';')
            if not tmp[0] == id :
                cat = cat + r + '\n'
                continue
                
        f = open(url, 'wt', encoding='utf-8')
        f.write(cat)
        f.close()

    def export(arr):
        url = 'Dados/exportados/ficheiro'

        if len(arr) > 0:
            stg = ";".join(arr)
            f = open(url+".csv", "a+")
            f.write( stg )
            f.close()

        if len(arr) > 0:
            stg = " ".join(arr)
            f = open(url+".txt", "a+")
            f.write( stg )
            f.close()

        # Make an update
        CAT = ''
        fc = open(url+'.csv', "r", encoding='utf-8')
        d1 = fc.readlines()
        f = open(url+".html", "w+")
        for k in range(len(d1)):
            CAT = CAT + '<tr>'
            dd1 = d1[k].split(';')
            for j in range( len(dd1) ):
                CAT = CAT + '<td>'+dd1[j]+'</td>'
            CAT = CAT + '</tr>'

        CAT = '<table border="1" width="100%" >' + CAT + '</table>'
        f.write( CAT )
        f.close()

class _f:
    def intToChar(num, start0 = False):
        CAT = ''
        c = ["A","B","C","D","E","F","G",
            "H","I","J","K","L","M","N",
            "O","P","Q","R","S","T","U",
            "V","W","X","Y","Z"]
        i = 0
        num = int(num) #make sure that is int
        sval = 1
        if num > 0:
            if start0:
                sval = 0
            while num != 0:
                tmp = (num % len(c))-sval
                CAT = CAT + c[tmp]
                i = i + 1
                num = int(num/len(c))
        else:
            return c[0]
        return CAT