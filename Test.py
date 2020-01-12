from Fn import _f
from Fn import isValid
from Fn import inFile
import json


print( json.loads(inFile.read('lang/pt-pt.json'))['attr'] )