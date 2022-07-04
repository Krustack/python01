motorcycle = {
    "model": "wave125",
    "brand": "Honda",
    "year": 2012
}
profile = {
    'name': "Wisanu",
    'age': 36
}
print(motorcycle["brand"])
print(profile["name"])
print(motorcycle)
# การเพิ่มkeyในdic
motorcycle['color'] = "blue"
print(motorcycle)
# การแก้ไขค่าในdic
motorcycle['color'] = 'red'
print(motorcycle)
motorcycle.pop('color')
print(motorcycle)
# การใช้list+dic
person = [{'name': 'Tuu', 'age': 18, 'favor': 'buffalo'},
          {'name': 'pom', 'age': 5, 'favor': 'aligator'},
          {'name': 'justin', 'age': 19, 'favor': 'pop music'}
          ]
print(person[0]['favor'])
# การใช้ใช้dicในdic
personDic = {'child': {'name': 'Tuu', 'age': 18, 'favor': 'buffalo'},'child2':{'name': 'pom', 'age': 5, 'favor': 'aligator'},'child3':{'name': 'justin', 'age': 19, 'favor': 'pop music'}}
print(personDic['child2']['favor'])