import matplotlib.pyplot as plt
import commonVar as cmv

def seedManager(r,seed,name,address):
    if not name in cmv.functionDict: cmv.functionDict[name]=address
    if not hasattr(address, "r"):
        address.r=r.Random()
        address.r.seed(seed)

