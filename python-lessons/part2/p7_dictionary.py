customer = {
    "name":"John",
    "age":21,
    "city":"California"
}
print(customer["name"])
print(customer.get("name"))

for key,value in customer.items():
    print(key,value)