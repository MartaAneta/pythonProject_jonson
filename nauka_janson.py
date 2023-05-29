import json


# some JSON:
x1 =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y1 = json.loads(x1)

# the result is a Python dictionary:
print(y1["age"])

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
x2 = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x2, indent=4, separators=(". ", " = ")))
