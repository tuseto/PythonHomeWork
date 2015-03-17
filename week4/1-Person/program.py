first_name = input("Enter first name: ")
second_name = input("Enter second name: ")
third_name = input("Enter third name: ")
birth_year = int(input("Enter birth year: "))

from datetime import date
def arr(first_name,second_name,third_name,birth_year):
    current_age = date.today().year - birth_year
    arr = {"first_name":first_name,
           "second_name":second_name,
           "third_name":third_name,
           "birth_year":birth_year,
           "current_age":current_age
        }
    return arr

print(arr(first_name,second_name,third_name,birth_year))
    
    
