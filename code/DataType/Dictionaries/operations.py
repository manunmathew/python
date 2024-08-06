person = {
  "Name": "Manu",
  "Age": "42",
  "Phone": 90540977
}
print(person)
print(person.keys())
print(person.values())

print(person.get("Name"))

x = person.pop("Name")
print(person)

person.popitem()
print(person)

person.update({"address": "xyz", "Des": "ëng"})
print(person)

person["company"] = "TCS"
print(person)


# Changing value
print(person)
person.update({"Name" : "Akhil"})
print(person)
person["Phone"] = "9003072987"
print(person)
