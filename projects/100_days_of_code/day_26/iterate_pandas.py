import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
# Looping through dictionaries
for (key, value) in student_dict.items():
    print(key, value)


# Pandas DataFrame creation
student_df = pandas.DataFrame(student_dict)
print(student_df)
for (key, value) in student_df.items():
    print(key) # gives columns
    print(value) # gives data from each column
    
# Pandas built-in iteration
# loop throuh rows of a data frame
for (index, row) in student_df.iterrows():
    print(index) # gives index number
    print(row) # gives each row one at a time
    print(row.student) # gives column of student
    
    if row.student == "Angela":
        print(row.score)