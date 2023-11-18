from pathlib import Path

p1 = Path('weather_data.txt')
print(p1, type(p1))

'''with open(p1, 'r') as file:
    print(file.read())
'''

print(p1.name)
print(p1.stem)
print(p1.suffix)

p2 = Path('C:/Users/HP/Desktop/Material/UpSkill/Automation')
print(p2.iterdir())
print(list(p2.iterdir()))

for i in p2.iterdir():
    print(i)