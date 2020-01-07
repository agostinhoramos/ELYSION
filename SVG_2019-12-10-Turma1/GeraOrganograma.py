import os
nomeFicheiro = "Organograma.html"
f = open(nomeFicheiro, "wt")
s = """<!DOCTYPE html>
<html>
<body>
<svg width='1200' height='800' style='padding:0px'>"""
print (s, file=f)

func = [
(1702654, 1, 'VINICIUS DE CASTRO E SILVA CUNHA', 6,  5, 5, 61, 'vcunha@hotmail.com', 938160289, 957232916, 629014, '07-02-2014', 3200.00, 'VINICIUS CUNHA'),
(1012133, 2, 'Ivo Miguel Carrilho Pinto',        12, 3, 3, 67, 'ipinto@hotmail.com', 967218166, 278814162, 930919, '07-03-2010', 1500.00, 'Ivo Pinto'),
(1702119, 3, 'Alexandre Terras Simões',          6,  1, 3, 17, 'asimões@uc.pt', 936789141, 879500590, 309929, '13-01-2010', 1100.00, 'Alexandre Simões'),
(1703638, 4, 'Diogo Oliveira Fernandes',         12, 1, 7, 74, 'dfernandes@gmail.com', 926279970, 652557500, 791914, '26-10-2019', 2000.00, 'Diogo Fernandes'),
(1702678, 5, 'Neio Mendes',                      12, 5, 9, 77, 'nmendes@gmail.com', 948264623, 898162328, 374208, '14-01-2013', 2800.00, 'Neio Mendes'),
(1702724, 6, 'Malam Embaló',                     6,  3, 10, 87, 'membaló@hotmail.com', 959401717, 101821237, 801389, '30-04-2018', 2800.00, 'Malam Embaló')
        ]
print(func)
x = 20
for fc in func:
    nome = fc [13]
    s = """<rect x="%d" y="20" rx="20" ry="20"  width="150" height="100" style="fill:rgba(255,0,0,0.5);stroke-width:3;stroke:grey" />
      <g transform="translate(40,20)">
        <text x="0" y="25">Presidente IPG</text>
        <text x="0" y="50">Prof. Doutor</text>
        <text x="0" y="75">%s</text>
      <g>""" % (x, nome)
    x = x + 150
    print (s, file=f)

s = "</svg></body></html>"
print (s, file=f)
f.close()
os.system(nomeFicheiro)