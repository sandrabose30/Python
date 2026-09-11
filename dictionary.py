# dictionary = {}
# dictionary - elementsa are stored as key-value pairs
# properties :
#* mutable
#* ordered
#*uniques keys
# dict = {
#     "name": "Sandra",
#     "age": 23,
#     "city": "New York"
# }
# print(dict)
# print(dict["name"])
# print(dict["age"])
# print(dict["city"])
#
# #mutable
# dict["city"] = "Ernakulam"
# print(dict)
# print(dict["city"])
#
# #pop - changing key
# dict["Mark"] = dict.pop("city")
# print(dict)
# dict["Mark"] =80
# print(dict)
import dictionary

#in-built methods
# 1. .keys() - show the list of keys
# 2. .values() - values
# 3. .items() - key-values

# dict = {
#     "name": "Sandra",
#     "age": 23,
#     "city": "New York"
# }
# print(dict.keys())
# print(dict.values())
# print(dict.items())

# 1.print all keys
# student = {
#     "name": "Ali",
# "age": 22,
# "course" : "python"}
# print(student.items())
# 2.print all values
# student = {
#     "name": "Ali",
# "age": 22,
# "course" : "python"}
# print(student.values())
# 3.print key- values pair
# student = {
#     "name": "Ali",
# "age": 22,
# "course" : "python"}
# for key, value in student.items():
#     print(f"{key}: {value}")

# 4.Sum of dictionary values
# marks = {"maths":80,"science":75,"english":90}
# sum=0
# for key in marks:
#     sum= sum+marks[key]
# print("Max marks :",sum)

# 5. Count dictionary items
# student = {
#     "name": "Ali",
# "age": 22,
# "course" : "python"}
# count=0
# for value in student.values():
#     count+=1
# print(count)
# 6. find the highest value
marks = {"maths":80,"science":75,"english":90}
highest=0
for key in marks:
    if marks[key] > highest:
        highest = marks[key]
print(highest)