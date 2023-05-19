import commonVar as cmv
import random as r


# seed must be a valid int number in range -2147483648 through 2147483647; here we set a super seed
# into the model machine cell

def generateSeeds():
    
    cmv.functionSeedList=[]
    # seeds for functions (currently quite large as quantity)
    for i in range(10):
        cmv.functionSeedList.append(r.randint(-2147483648,2147483647)) 
    
    # generators for class instances lists
    rHousehold=r.Random()
    rHousehold.seed(r.randint(-2147483648,2147483647))
    rFirm=r.Random()
    rFirm.seed(r.randint(-2147483648,2147483647))

    cmv.householdSeedList=[]
    # seeds for agent class instances; quantity = cmv.agentNum 
    cmv.firmSeedList=[]
    # seeds for firm class instances using quantity = cmv.firmsNum 
    # (add positions if new firms are created while the simulation is running)

    
    for i in range(cmv.householdNum):
        cmv.householdSeedList.append(rHousehold.randint(-2147483648,2147483647)) 
        
    for i in range(cmv.firmsNum):
        cmv.firmSeedList.append(rFirm.randint(-2147483648,2147483647)) 
 
    # function # 0 - setup
    if 'setup' in cmv.functionDict: del cmv.functionDict['setup'].r
        
        
 