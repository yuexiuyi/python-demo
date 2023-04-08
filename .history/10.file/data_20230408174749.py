import json

number = [2,3,4,5,6]

filename = '10.file/number.json'
with open(filename,'w') as file_obj:
  json.dump(number,file_obj)

