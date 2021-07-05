#Import Modules

import os
import csv

#Read in csv file

PyPoll = os.path.join('PyPoll_Election_Data.csv')

#List all candidates
Khan = []
Li = []
OTooley =[]
Correy = []

#Read in csv and disregard headers

with open(PyPoll, newline ='') as csvfile:
    
        csvreader = csv.reader(csvfile, delimiter = ',')
        
        header = next(csvreader)
        
        #Loop Through Data

        for row in csvreader:
            
            #Total Votes
            votes.append(row[0])
            
            #candidates
            candidates.append(row[2])
            
# Total Votes per candidate

for candidate in candidates:

    if candidate == "Khan":
        Khan.append(candidates)
        Khan_Votes = len(Khan)
        
    elif candidate == "Li":
        Li.append(candidates)
        Li_Votes = len(Li)
        
    elif candidate == "O'Tooley":
        OTooley.append(candidates)
        OTooley_Votes = len(OTooley)
        
    elif candidate == "Correy":
        Correy.append(candidates)
        Correy_Votes = len(Correy) 
        
#Percentage Votes Per Candidate

Khan_Percentage = (int(Khan_Votes))/len(votes) * 100

Li_Percentage = (int(Li_Votes))/len(votes) * 100

OTooley_Percentage = (int(OTooley_Votes))/len(votes) * 100

Correy_Percentage = (int(Correy_Votes))/len(votes) * 100

# Election Winner

if Khan_Percentage == max(Li_Percentage, OTooley_Percentage, Correy_Percentage):
        winner = "Khan"
    
elif Li_Percentage == max(Khan_Percentage, OTooley_Percentage, Correy_Percentage):
        winner = "Li"
    
elif OTooley_Percentage == max(Khan_Percentage, Li_Percentage, Correy_Percentage):
        winner = "Otooley"
    
elif Correy_Percentage == max(Khan_Percentage, OTooley_Percentage, Li_Percentage):
        winner = "Correy"
    
# Print Final Statement
print("Election REsults")
print("-------------------------------------")

print(f"Total Votes:{len(votes)}")

print("-------------------------------------")

print(f"Khan: %{Khan_Percentage}",(Khan_Votes))
print(f"Li: %{Li_Percentage}",(Li_Votes))
print(f"Otooley: %{OTooley_Percentage}",(OTooley_Votes))
print(f"Correy: %{Correy_Percentage}",(Correy_Votes))

print("-------------------------------------")

print(f"winner: Khan")
