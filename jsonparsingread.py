import json
with open ("data.json") as file:
    data=json.load(file)
    print(data)
    print(type(data))
    print(data["Pulse"])
    print(data["Pulse"]['1'])
    int_dict= data["Pulse"]
    print(int_dict['0'])