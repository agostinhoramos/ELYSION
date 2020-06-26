from Fn import _f
from Fn import isValid
from Fn import inFile
import json

_L = json.loads(inFile.read('lang/pt-pt.json'))

rd = "Hi %s, how are you?" % ("Agostinho Ramos")
print( rd )
