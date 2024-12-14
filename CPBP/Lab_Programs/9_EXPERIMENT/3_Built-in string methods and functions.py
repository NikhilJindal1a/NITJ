# Built-in string methods and functions
s =  "hello"
print(s.capitalize())

s = "hello"
print(s.center(10, '*'))

msg = 'he'
str1 = "hellohello"
print(str1.count(msg, 0, len(str1)))

msg = "she is my best friend"
print(msg.endswith("end", 0, len(msg)))

str1 = "the world is beautiful"
print(str1.startswith("th", 0, len(str1)))

msg = "she is my best my friend"
print(msg.find("my", 0, len(msg)))
print(msg.find("mine", 0, len(msg)))

try:
    print(msg.index("mine", 0, len(msg)))
except:
    print("substring not found")
