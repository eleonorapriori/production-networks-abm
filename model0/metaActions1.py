import commonVar as cmv
#import random as r
from tools import *


def stateHouseholdParametersAll():
    for aHousehold in cmv.householdList:
        aHousehold.stateHouseholdParameters()
        
def stateFirmsParametersAll():
    for aFirm in cmv.firmsList:
        aFirm.stateFirmsParameters()
        
def identifyEquilibriumPriceAll():
    for aFirm in cmv.firmsList:
        aFirm.identifyEquilibriumPrice()    

def identifyEquilibriumOutputAll():
    for aFirm in cmv.firmsList:
        aFirm.identifyEquilibriumOutput()
        
def consumeAll():
    for aHousehold in cmv.householdList:
        aHousehold.consume()
