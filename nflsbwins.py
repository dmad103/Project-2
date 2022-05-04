# The library is imported into the program
import sports 

# The Super Bowl wins of five NFL teams are extracted from the library
giants = sports.get_team(sports.FOOTBALL, 'giants')
print("The New York Giants have won ",giants.super_bowls,"Super Bowls")

falcons = sports.get_team(sports.FOOTBALL, 'falcons')
print("The Atlanta Falcons have won ",falcons.super_bowls,"Super Bowls")

vikings = sports.get_team(sports.FOOTBALL, 'vikings')
print("The Minnesota Vikings have won ",vikings.super_bowls,"Super Bowls")

dolphins = sports.get_team(sports.FOOTBALL, 'dolphins')
print("The Dolphins have won ",dolphins.super_bowls,"Super Bowls")

bears = sports.get_team(sports.FOOTBALL, 'bears')
print("The Bears have won ",bears.super_bowls,"Super Bowls")

# A abbrievated variable is made to store the other variable that has the value of Super
# Bowls won by that team
nyg = giants.super_bowls
falcons = falcons.super_bowls
vikings = vikings.super_bowls
dolphins = dolphins.super_bowls
bears = bears.super_bowls

# A new variable is made that lists the abbrievated variables. Then it's prints
# out a bracket of the sorted value of the Super Bowls of each team (from least to 
# greatest)
teams =[nyg, falcons, vikings, dolphins, bears]
print(sorted(teams))

