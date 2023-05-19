#import matplotlib.pyplot as plt
import commonVar as cmv
import pandas as pd
import numpy as np
import scipy.stats as st

def makeSeries():
    
    cmv.cycleDf=pd.DataFrame(cmv.cycleSeries)
    cmv.cycleDf.columns=["cycle"]
    cmv.priceSeriesDf=pd.DataFrame(cmv.priceSeries)
    cmv.priceSeriesDf.columns=["price_1","price_2","price_3"]
    cmv.outputSeriesDf=pd.DataFrame(cmv.outputSeries)
    cmv.outputSeriesDf.columns=["output_1","output_2","output_3"]
    cmv.consumptionSeriesDf=pd.DataFrame(cmv.consumptionSeries)
    cmv.consumptionSeriesDf.columns=["consumption_1","consumption_2","consumption_3"]
    cmv.utilitySeriesDf=pd.DataFrame(cmv.utilitySeries)
    cmv.utilitySeriesDf.columns=["utility"]   
    
    cmv.myOutputData=pd.concat([cmv.cycleDf, cmv.priceSeriesDf,cmv.outputSeriesDf, \
                               cmv.consumptionSeriesDf, cmv.utilitySeriesDf], axis=1)
    cmv.allSeriesReplications.append(cmv.myOutputData)
    

def makePlots():
    cmv.priceSeriesDf.plot(title="price Series Series", legend=False)
    cmv.outputSeriesDf.plot(title="quantity of output Series", legend=False)
    cmv.consumptionSeriesDf.plot(title="consumption over goods Series", legend=False)
    cmv.utilitySeriesDf.plot(title="consumer utility Series", legend=False)
    
    
    
def makePlotsMontecarlo():

    for i in range(len(cmv.allSeriesReplications)):
        cmv.montecarloDf=pd.concat(cmv.allSeriesReplications)   
    #print(cmv.montecarloDf)
    
    meanPrice_1=[]
    meanPrice_2=[]
    meanPrice_3=[]
    meanOutput_1=[]
    meanOutput_2=[]
    meanOutput_3=[]
    meanConsumption_1=[]
    meanConsumption_2=[]
    meanConsumption_3=[]
    meanUtility=[]


    for i in range(cmv.nOfCycles):
        meanPrice_1.append(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'price_1'].mean())
        meanPrice_2.append(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'price_2'].mean())
        meanPrice_3.append(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'price_3'].mean())
        meanOutput_1.append(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'output_1'].mean())
        meanOutput_2.append(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'output_2'].mean())
        meanOutput_3.append(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'output_3'].mean())
        meanConsumption_1.append(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'consumption_1'].mean())
        meanConsumption_2.append(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'consumption_2'].mean())
        meanConsumption_3.append(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'consumption_3'].mean())
        meanUtility.append(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'utility'].mean())
      
    meanPrice_1=pd.DataFrame(meanPrice_1)
    meanPrice_2=pd.DataFrame(meanPrice_2)
    meanPrice_3=pd.DataFrame(meanPrice_3)
    meanOutput_1=pd.DataFrame(meanOutput_1)
    meanOutput_2=pd.DataFrame(meanOutput_2)
    meanOutput_3=pd.DataFrame(meanOutput_3)
    meanConsumption_1=pd.DataFrame(meanConsumption_1)
    meanConsumption_2=pd.DataFrame(meanConsumption_2)
    meanConsumption_3=pd.DataFrame(meanConsumption_3)
    meanUtility=pd.DataFrame(meanUtility)
    
    cmv.montecarloDfMeanOverReplications=pd.concat([cmv.cycleDf, meanPrice_1, meanPrice_2, meanPrice_3, meanOutput_1, meanOutput_2, \
                                       meanOutput_3, meanConsumption_1, meanConsumption_2, meanConsumption_3, meanUtility], axis=1)
    cmv.montecarloDfMeanOverReplications.columns= ["cycle","meanPrice_1","meanPrice_2","meanPrice_3","meanOutput_1","meanOutput_2", \
                                       "meanOutput_3","meanConsumption_1","meanConsumption_2","meanConsumption_3","meanUtility"]
 
    
    price1_ci=[]
    price1_ciMin=[]
    price1_ciMax=[]  
    
    price2_ci=[]
    price2_ciMin=[]
    price2_ciMax=[] 
    
    price3_ci=[]
    price3_ciMin=[]
    price3_ciMax=[]
    
    output1_ci=[]
    output1_ciMin=[]
    output1_ciMax=[]
    
    output2_ci=[]
    output2_ciMin=[]
    output2_ciMax=[]
    
    output3_ci=[]
    output3_ciMin=[]
    output3_ciMax=[]
    
    
    consumption1_ci=[]
    consumption1_ciMin=[]
    consumption1_ciMax=[]  
    
    consumption2_ci=[]
    consumption2_ciMin=[]
    consumption2_ciMax=[] 
    
    consumption3_ci=[]
    consumption3_ciMin=[]
    consumption3_ciMax=[]
    
    utility_ci=[]
    utility_ciMin=[]
    utility_ciMax=[]
       
    for i in range(cmv.nOfCycles):
        price1_ci.append(st.norm.interval(alpha=0.95, loc=np.mean(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, \
                         'price_1']), scale=st.sem(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'price_1'])))
        price1_ciMin.append(price1_ci[i][0])
        price1_ciMax.append(price1_ci[i][1])
        
        price2_ci.append(st.norm.interval(alpha=0.95, loc=np.mean(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, \
                         'price_2']), scale=st.sem(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'price_2'])))
        price2_ciMin.append(price2_ci[i][0])
        price2_ciMax.append(price2_ci[i][1])
    
        price3_ci.append(st.norm.interval(alpha=0.95, loc=np.mean(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, \
                         'price_3']), scale=st.sem(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'price_3'])))
        price3_ciMin.append(price3_ci[i][0])
        price3_ciMax.append(price3_ci[i][1])
        
        
        output1_ci.append(st.norm.interval(alpha=0.95, loc=np.mean(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, \
                         'output_1']), scale=st.sem(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'output_1'])))
        output1_ciMin.append(output1_ci[i][0])
        output1_ciMax.append(output1_ci[i][1])
        
        output2_ci.append(st.norm.interval(alpha=0.95, loc=np.mean(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, \
                         'output_2']), scale=st.sem(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'output_2'])))
        output2_ciMin.append(output2_ci[i][0])
        output2_ciMax.append(output2_ci[i][1])
    
        output3_ci.append(st.norm.interval(alpha=0.95, loc=np.mean(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, \
                         'output_3']), scale=st.sem(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'output_3'])))
        output3_ciMin.append(output3_ci[i][0])
        output3_ciMax.append(output3_ci[i][1])
        
        
        consumption1_ci.append(st.norm.interval(alpha=0.95, loc=np.mean(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, \
                         'consumption_1']), scale=st.sem(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'consumption_1'])))
        consumption1_ciMin.append(consumption1_ci[i][0])
        consumption1_ciMax.append(consumption1_ci[i][1])
           
        consumption2_ci.append(st.norm.interval(alpha=0.95, loc=np.mean(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, \
                         'consumption_2']), scale=st.sem(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'consumption_2'])))
        consumption2_ciMin.append(consumption2_ci[i][0])
        consumption2_ciMax.append(consumption2_ci[i][1])  
        
        consumption3_ci.append(st.norm.interval(alpha=0.95, loc=np.mean(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, \
                         'consumption_3']), scale=st.sem(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'consumption_3'])))
        consumption3_ciMin.append(consumption3_ci[i][0])
        consumption3_ciMax.append(consumption3_ci[i][1])  
        
        utility_ci.append(st.norm.interval(alpha=0.95, loc=np.mean(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, \
                         'utility']), scale=st.sem(cmv.montecarloDf.loc[cmv.montecarloDf['cycle'] == i, 'utility'])))
        utility_ciMin.append(utility_ci[i][0])
        utility_ciMax.append(utility_ci[i][1])  
        
  
    price1_ciMin=pd.DataFrame(price1_ciMin)
    price1_ciMax=pd.DataFrame(price1_ciMax)
    price2_ciMin=pd.DataFrame(price2_ciMin)
    price2_ciMax=pd.DataFrame(price2_ciMax)
    price3_ciMin=pd.DataFrame(price3_ciMin)
    price3_ciMax=pd.DataFrame(price3_ciMax)
    
    output1_ciMin=pd.DataFrame(output1_ciMin)
    output1_ciMax=pd.DataFrame(output1_ciMax)
    output2_ciMin=pd.DataFrame(output2_ciMin)
    output2_ciMax=pd.DataFrame(output2_ciMax)
    output3_ciMin=pd.DataFrame(output3_ciMin)
    output3_ciMax=pd.DataFrame(output3_ciMax)   
    
    consumption1_ciMin=pd.DataFrame(consumption1_ciMin)
    consumption1_ciMax=pd.DataFrame(consumption1_ciMax)
    consumption2_ciMin=pd.DataFrame(consumption2_ciMin)
    consumption2_ciMax=pd.DataFrame(consumption2_ciMax)
    consumption3_ciMin=pd.DataFrame(consumption3_ciMin)
    consumption3_ciMax=pd.DataFrame(consumption3_ciMax)   
    
    utility_ciMin=pd.DataFrame(utility_ciMin)
    utility_ciMax=pd.DataFrame(utility_ciMax)   
    

    cmv.montecarloPricesSeries=pd.concat([meanPrice_1, meanPrice_2, meanPrice_3], axis=1)
    graphPrices=cmv.montecarloPricesSeries.plot(title="price Series", legend=False)
    graphPrices.fill_between(price1_ciMin[0].index, price1_ciMin[0],price1_ciMax[0], color='blue', alpha=.05)
    graphPrices.fill_between(price2_ciMin[0].index,price2_ciMin[0],price2_ciMax[0], color='orange', alpha=.05)
    graphPrices.fill_between(price3_ciMin[0].index,price3_ciMin[0],price3_ciMax[0], color='green', alpha=.05) 


    cmv.montecarloOutputSeries=pd.concat([meanOutput_1, meanOutput_2,meanOutput_3], axis=1)
    graphOutputs=cmv.montecarloOutputSeries.plot(title="Output Series", legend=False)
    graphOutputs.fill_between(output1_ciMin[0].index, output1_ciMin[0],output1_ciMax[0], color='blue', alpha=.05)
    graphOutputs.fill_between(output2_ciMin[0].index,output2_ciMin[0],output2_ciMax[0], color='orange', alpha=.05)
    graphOutputs.fill_between(output3_ciMin[0].index,output3_ciMin[0],output3_ciMax[0], color='green', alpha=.05) 
    
    cmv.montecarloConsumptionSeries=pd.concat([meanConsumption_1, meanConsumption_2, meanConsumption_3], axis=1)
    graphConsumptions=cmv.montecarloConsumptionSeries.plot(title="Consumption Series", legend=False)
    graphConsumptions.fill_between(consumption1_ciMin[0].index, consumption1_ciMin[0], consumption1_ciMax[0], color='blue', alpha=.05)
    graphConsumptions.fill_between(consumption2_ciMin[0].index, consumption2_ciMin[0], consumption2_ciMax[0], color='orange', alpha=.05)
    graphConsumptions.fill_between(consumption3_ciMin[0].index, consumption3_ciMin[0], consumption3_ciMax[0], color='green', alpha=.05)
    
    cmv.montecarloUtilitySeries=meanUtility
    graphUtility=cmv.montecarloUtilitySeries.plot(title="Utility Series", legend=False)
    graphUtility.fill_between(utility_ciMin[0].index, utility_ciMin[0], utility_ciMax[0], color='blue', alpha=.05)