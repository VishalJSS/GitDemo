import json
content = '{"name":"Vishal", "Course":["Python", "RobotFramework"]}'
dict_content = json.loads(content)

#Checking basic printing by converting to dictionary
print(type(dict_content))
print(dict_content)
print(dict_content['name'])
print(dict_content['Course'])
list_lang = dict_content['Course']
print(type(list_lang))
print(list_lang[0])
print(list_lang[1])