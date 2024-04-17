data = {'Name': 'bytexl', 2: 'company', 'Domain': 'technical'}
data[4] = 'trainer'
print(data)

keys_view = data.keys()
print(keys_view)

values_view = data.values()
print(values_view)

data_value = data.get('Name')
print(data_value)

copied_data = data.copy()
print(copied_data)

addition = {5: 'Hyderabad'}
data.update(addition)
print(data)

remove = data.pop('Domain')
print(remove)
#M

if 'Name' in data:
    print("Name is present:", data['Name'])
else:
    print("Name not found")
