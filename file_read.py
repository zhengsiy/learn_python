import json


file_path='I:/python_work/pi_digits.txt'
with open(file_path) as file_object:
    content=file_object.read()
    lines=file_object.readlines()
    
print(content)

for line in lines:
        print(line.rstrip())


file_path2='I:/python_work/I  can.txt'
with open(file_path2) as file_object2:
      content=file_object2.read()
      print(content)

with open(file_path2) as file_object2:
      for line in file_object2:
            print(line)


with open(file_path2) as file_object2:
      lines=file_object2.readlines()

pi_string=''
for line in lines:
      pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

print(pi_string.replace('python','C++'))


with open(file_path2,'a') as file_object3:
      content=file_object3.write('I also love finding meaning in large datasets.\n')
      content=file_object3.write('I love creaing apps that can run in a broser.')
print(content)


number=[3,6]
file_path2='number.json'
with open(file_path2,'w') as f:
      json.dump(number,f)