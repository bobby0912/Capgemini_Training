d={}
print(d)

d1={'a':1,'b':2}
print(d1)

d2={'A':{'a':1,'b':2}}
print(d2)
print("answer: ",d2['A']['a'])

d3=dict(name='raju', age=20)
print(d3)


keys=['eggs','milk','bread']
vals=[6,30,50]

d4=dict(zip(keys,vals))
print(d4)

d2.update(d4)
print(d2)

print("default: ",d1.get('c',0))

# install mysql-connector-python