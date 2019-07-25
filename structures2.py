#List,
# Tuple,
# Dictionary
#strings-alphanumeric or special character
#integer-numeric with no decimals

#float-numeric with few decimals,22
#double-a number with a very large decimal

#boolean-variable which holds true or false

sum = (67 +87 +56 +78 +45)
average = sum / 5
#modulus-Used today for conditional operators

rem = 7 % 2
print(type(str(rem)))


dec1 = 3.4512123
print(int(dec1))

bo = 4 > 7
print(bo)

dec2 = round(dec , 2)
print(dec2)

INDEXES START FROM 0




person_1 = ["John","Doe", 30, 65.54, "Mombasa", True]
print (type(person_1))
person_1[1:5]
print (person_1[-4:-2]) #integer is normally given 11 bits,string 254 bits,list 10 bytes
print(len(person_1))
print(person_1.append("New Value"))
person_1.remove("New Value")
print (person_1)
person_1.pop(0)
person_t = ("John","Doe", 30, 65.54, "Mombasa", True)
print (type(person_t))
print (person_t[0:4])
print(person_t)

#Dictionary-Structure that holds variables in key:value pairs
#when getting value use square brackets
person_dict = {"firstName" : "john" , "SurName" : "Doe , "weight": 65.54 , "location" : "mombasa" , "activeUser" : True}
print(person_dict["SurName"])

#revise on

task_list = [23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76, "John" )]
print(type(task_list))
print task_list[]
print (task_list[2][2]["currency"])
print (len(task_list)