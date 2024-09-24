# Constants
HOURS_IN_A_WEEK = 168  # Total hours in a week

# User input
credit_hours = int(input("Total credit hours for next semester? "))
travel_time = int(input("Daily travel time in minutes? ")) / 60  # Convert to hours
work_hours = int(input("Hours you work per week? "))
sleep_hours = int(input("Hours you sleep per night? ")) * 7  # Weekly sleep
eating_hours = int(input("Hours you spend eating per day? ")) * 7  # Weekly eating

# Calculate required classes and total hours used
classes_needed = credit_hours // 3
final_class_hours = credit_hours % 3
study_hours = credit_hours * 2
total_hours_used = study_hours + travel_time * 7 + work_hours + sleep_hours + eating_hours

# Calculate free time
free_time = HOURS_IN_A_WEEK - total_hours_used

# Display results
print(f"\nClasses needed: {classes_needed} (Final class: {final_class_hours} credits)")
print(f"Free time available: {free_time:.2f} hours/week")
