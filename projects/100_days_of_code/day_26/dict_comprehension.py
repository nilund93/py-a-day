# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}
# new_dict = {new_key:new_value for (key, value) in dict.items() if test}

from random import randint

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {
    "Alex": 68,
    "Beth": 89,
    "Caroline": 32,
    "Dave": 90,
    "Eleanor": 56,
    "Freddie": 20
}

students_score = {student:randint(1, 100) for student in names}
print(students_score)

passed_students = {student:score for (student,score) in students_score.items() if score >= 60}
print(passed_students)

# First exercise
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

# Second exercise
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:((temp*9/5) + 32) for (day, temp) in weather_c.items()}
print(weather_f)