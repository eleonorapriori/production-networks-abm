import commonVar as cmv
import pandas as pd

def initMatrices():
    cmv.gammaMatrix=[]
    cmv.etaVector= []
    cmv.betaGamma=[]
    cmv.betaGammaE=[]
    cmv.zetaVector=[]
    cmv.muHatVector=[]
    cmv.logPriceOfFactors=[]
    cmv.priceOfFactors=[]
    cmv.partialPricesVector=[]
    cmv.partialOutputVector=[]
    
def initSeries():
    cmv.cycleSeries=[]
    cmv.priceSeries=[]
    cmv.outputSeries=[]
    cmv.consumptionSeries=[]
    cmv.utilitySeries=[]
    
    cmv.cycleDf=[]
    cmv.priceSeriesDf =[]
    cmv.outputSeriesDf=[]
    cmv.consumptionSeriesDf=[]
    cmv.utilitySeriesDf=[]
    cmv.myOutputData=[]
    
    
def computeSeries():
    prices=[]
    outputQuantities=[]
   
    for aFirm in cmv.firmsList:
        prices.append(aFirm.price)
        outputQuantities.append(aFirm.quantityOfOutput)
    cmv.priceSeries.append(prices)
    cmv.outputSeries.append(outputQuantities)

    consumptions=[]
    welfare=[]
  
    for aHousehold in cmv.householdList:
        consumptions.append(aHousehold.consumption)
        welfare.append(aHousehold.utility)
        
    cmv.consumptionSeries.append(consumptions[0])
    cmv.utilitySeries.append(welfare)
    cmv.cycleSeries.append(cmv.cycle)


def initMontecarlo():
    cmv.allSeriesReplications=[]
    cmv.montecarloDf=[]
    cmv.montecarloDfMeanOverReplications=pd.DataFrame([])
    
    cmv.montecarloPricesSeries=pd.DataFrame()
    cmv.montecarloOutputSeries=pd.DataFrame()
    cmv.montecarloConsumptionSeries=pd.DataFrame()
    cmv.montecarloUtilitySeries=pd.DataFrame()
    
    
   
   
    
    