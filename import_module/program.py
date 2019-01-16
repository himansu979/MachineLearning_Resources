

import config
print("var : ", config.var)
print("result : ", config.getval())

from config import var, getval
print("var : ", var)
print("result : ", getval())


import sys
filename = sys.argv[1].split(".")[0]
config1 = __import__(filename)

print("var1 : ", config1.var)
print("result1 : ", config1.getval())



