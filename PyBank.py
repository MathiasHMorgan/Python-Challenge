#import modules

import os
import csv

PyBank = os.path.join('PyBank_Budget_Data.csv')

# create lists

monthcount = []
profit = []
profit_change =[]

#set string and numerical parameters

Greatest_Increase = ["", 0]
Greatest_Decrease = ["", 999999]

#Read in csv and disregard headers

with open(PyBank, newline ='') as csvfile:
    
        csvreader = csv.reader(csvfile, delimiter = ',')
        
        header = next(csvreader)

#loop through data

        for row in csvreader:
        
            #Month Count
    
            monthcount.append(row[0])
        
            #Profit Calculation
    
            profit.append(int(row[1]))
        
            #Net Profit Change
        
            previous_net_change = int(row[1]) - int(row[1])
        
            net_change = int(row[1]) 
          
 #Loop though data

for i in range(len(profit)-1):
    
                #Profit Change
    
                profit_change.append(profit[i+1]-profit[i])
        
                # Greatest Increase and Decrease
                
                Greatest_Increase = max(profit_change)
                
                Greatest_Decrease = min(profit_change)
              
                Average_Change_in_profit = sum(profit_change)/len(profit_change)
                
 # Print Final Statement
print("Financial Analsis")
print("-------------------------------------")
print(f"Total Months:{len(monthcount)}")
print(f"Total:{sum(profit)}")
print(f"Average Change in Profit: ${Average_Change_in_profit}")
print(f"Greatest Increase in Profits: ${Greatest_Increase}")
print(f"Greatest Decrease in Profits: ${Greatest_Decrease}")
            
