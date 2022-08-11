first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"
print(("Hello, {first_name} {last_name}. You are {age}. " + 
       "You are a {profession}. You were a member of {affiliation}.") \
       .format(first_name=first_name, last_name=last_name, age=age, \
               profession=profession, affiliation=affiliation))