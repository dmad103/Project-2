from datetime import date
import holidays

# Holidays are filtered to only ones in the US
us_holidays = holidays.US() 

# Checking to see if there's any holidays on the first 7 days of July
Day1 = date(2022, 7, 1) in us_holidays  
Day2 = date(2022, 7, 2) in us_holidays  
Day3 = date(2022, 7, 3) in us_holidays   
Day4 = date(2022, 7, 4) in us_holidays 
Day5 = date(2022, 7, 5) in us_holidays 
Day6 = date(2022, 7, 6) in us_holidays 
Day7 = date(2022, 7, 7) in us_holidays 

# The variables hold the data within those specific days 
y_o_n_holiday1 = us_holidays.get('2022-7-1')  
y_o_n_holiday2 = us_holidays.get('2022-7-2')
y_o_n_holiday3 = us_holidays.get('2022-7-3')    
y_o_n_holiday4 = us_holidays.get('2022-7-4') 
y_o_n_holiday5 = us_holidays.get('2022-7-5') 
y_o_n_holiday6 = us_holidays.get('2022-7-6') 
y_o_n_holiday7 = us_holidays.get('2022-7-7') 

# The days are printed. "True" means there's a holiday on that day. "False" means there 
# isn't.
print(Day1)
print(Day2)
print(Day3)
print(Day4)
print(Day5)
print(Day6)
print(Day7)

# Prints a space to separate the 2 types of data
print('')

# Prints out whether there's a holiday within those variables that hold the data. If there
# is then the holiday will be printed. If there isn't then it'll display "None".
print(y_o_n_holiday1)
print(y_o_n_holiday2)
print(y_o_n_holiday3)
print(y_o_n_holiday4)
print(y_o_n_holiday5)
print(y_o_n_holiday6)
print(y_o_n_holiday7)

