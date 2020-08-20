#STEP1: Provides a list-of-lists of the permutations of S1 HA/SA strategies called 'Strategies'.  
#Higher lists include members for each S1 Strategy permutation. 
#Subordinate lists have the HA:SA decision of S1 at each turn, with 1=HA, and  0=SA. 
#As HA is a 'game over' choice, strategies can only have one member that equals '1'.
#For example, for 5 turns, Strategies = [1,01,001,0001,00001,00000]
Turns = 15 #Adjust to change number of turns
import itertools
SLen=1
strat_length=[]
while (SLen<=Turns):
    strat_length.append(SLen)
    SLen+=1
Strategies=[]
for f2 in strat_length:
    strat3=[]
    n5=1
    while n5<f2:
        strat3.append(0)
        n5+=1
    strat3.append(1)
    Strategies.append(strat3)
n6=1
strat4=[]
while n6<=Turns:
    strat4.append(0)
    n6+=1
Strategies.append(strat4)
#STEP2: Use 'Strategies' to create a list-of-lists, called 'Probability_of_S2_Refuse'. 
#Higher lists include members for each S1 strategy permutation.  
#Sub-lists have members representing the probability of S2 refusing at each turn.
#Strategy is the member of 'Strategies' that is being be considered by the function.
def Payoff_Calculator (Strategy,Strategies):
    Probability_of_S2_Refuse=[]
    def Probability_of_S2_Refuse_Generator(Strategy):
        stepper = 0
        Probability_of_S2_Refuse.append(0.50)
        def next_step(Strategy,stepper):
            n = Probability_of_S2_Refuse[stepper] 
            if (n == 0.1):
                if (Strategy[stepper]==0):
                    Probability_of_S2_Refuse.append(0.25)
            elif (n == 0.25):
                if (Strategy[stepper]==0):
                    Probability_of_S2_Refuse.append(0.5)
            elif (n == 0.5):
                if (Strategy[stepper]==0):
                    Probability_of_S2_Refuse.append(0.75)
            elif (n == 0.75):
                if (Strategy[stepper]==0):
                    Probability_of_S2_Refuse.append(0.9)
            else:
                Probability_of_S2_Refuse.append(0.9)
            if (stepper < (len(Strategy)-2)):
                stepper=stepper+1
                next_step(Strategy,stepper)
        if (stepper == 0):
            next_step(Strategy,stepper)
    Probability_of_S2_Refuse_Generator(Strategy)
#STEP3: List all the potential sitations that may arise from a single Strategy, in 'Valid_Perms'
    def T_and_E_Finder_for__Strategy(Strategy,Strategies,Probability_of_S2_Refuse):
        Length_until_HA=0
        while (Length_until_HA<(Turns)) and (Strategy[Length_until_HA]==0):
            Length_until_HA+=1
        Length_until_HA+=1
        Perms = [list(w) for w in itertools.product([0, 1], repeat=Turns)]
        Valid_Perms=[]
        for q in Perms:
            n=sum(q)
            if n<=Length_until_HA:
                Valid_Perms.append(q)
#STEP4: Identify the probability (Prob_Slice_Total) of each permutation (Potentiality_Slice).
        T_List=[]
        E_List=[]
        for p in Valid_Perms:
            PotSliceLen=sum(p)
            Potentiality_Slice = p
            while (Potentiality_Slice[-1]==0) and (PotSliceLen==Length_until_HA):
                Potentiality_Slice.pop(-1)
            PS_Length = len(Potentiality_Slice)
            SA_Cost = PotSliceLen 
            if (Length_until_HA == PotSliceLen):
                SA_Cost=SA_Cost-1 
            SF_Cost = PS_Length - PotSliceLen
            Prob_Slice=[]
            v=0
            for r in Potentiality_Slice:
                if (r == 0):
                    Prob_Slice.append(Probability_of_S2_Refuse[v])
                else:
                    Prob_Slice.append(1-Probability_of_S2_Refuse[v])
                    v=v+1
            Prob_Slice_Total=1
            for i in Prob_Slice:
                Prob_Slice_Total=Prob_Slice_Total*i
#Step 5: Calculate proability weighted payoffs for each Probability_Slice.
# Sum them to find the total payoff for each Strategy.
            SA_CostProb=SA_Cost*Prob_Slice_Total
            SF_CostProb=SF_Cost*Prob_Slice_Total
            T_Slice=SA_CostProb+SF_CostProb
            E_Slice=SF_CostProb
            E_List.append(E_Slice)
            T_List.append(T_Slice)
        E_Total=sum(E_List)
        T_Total=sum(T_List)
        print(E_Total,T_Total)
    T_and_E_Finder_for__Strategy(Strategy,Strategies,Probability_of_S2_Refuse)
for Strategy in Strategies:
    Payoff_Calculator(Strategy,Strategies)
