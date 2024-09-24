# Seamus Sept, 23 - Credit Where Due
input1=input("How many 3 credit hour classes do you plan on taking next semester?")
input2=input("how many credit hours is your final class?")
n1=int(input1)
n2=int(input2)
total_3_credit_hours = n1 * 3
total_credit_hours = total_3_credit_hours + n2
print(f"The total number of credit hours you are taking is {total_credit_hours}.")
print("Spend around double this time outside of class for studying")
input3=input("How many hours a week do you spend travelling/commuting?")
n3=int(input3)
commute= total_credit_hours*2 + n3
print(f"we'll add this time to {total_credit_hours*2} to get {commute} total hours so far")
sleep=8*7
eating=1*7
input4=input("how many hours do you shower in a overall week?")
n4=int(input4)
print(f"To get your used up time for the week we also need to add up a average of {sleep} hours of sleep per week plus eating which will take around {eating} hours per week ")
final_time=commute+eating+sleep
print(f"Total time spent busy during a 168 hour week is {final_time} hours, leaving you with {168-final_time} hours of free time")
