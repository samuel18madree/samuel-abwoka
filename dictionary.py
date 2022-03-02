
Dict = {1: 'Geeks' , 2: 'For' ,  3: 'Geeks'}
print("\nDictionary with the use of integer keys:")
print(Dict)
Dict = {'Name' : 'Geeks',1:[1,2,3,4]}
print("\nDictionary with the use of mixed keys:")
print(Dict)


Dict ={}
print("Empty Dictionary:")
print(Dict)
Dict = dict({1:'Geeks',2:'For',3:'Geeks'})
print("\nDictionary with the use of dict():")
print(Dict)
Dict = dict([(1,'Geeks'),(2,'For')])
print(Dict)


#nested dictionary
Dict={}
print("Empty Dictionary:")
print(Dict)
Dict[0]='Geeks'
Dict[2]='For'
Dict[3]=1
print("\nDictionary after adding 3 elements:")
print(Dict)
Dict['Value_set']=2,3,4
print("\nDictionary after adding 3 elements:")
print(Dict)
Dict[2]='Welcome'
print("\nUpdated key value:")
print(Dict)