Str = "Sandro Megrelishvili"
[ord(c) for c in Str]
AsciiList = [ord(c) for c in Str]
def multiplyList(AsciiList):
    result = 1
    for x in AsciiList:
        result = result * x
    return result
prod = multiplyList(AsciiList)
import random
random.seed(1)
Random = int(268745.8009399202)
num = prod ^ Random
hx = hex(num)
hx = str(hx)
print(hx[:16]) #result