class Example:
    def __init__(self,name):
        print(f"First constructor: hello {name}")
    
    def __init__(self,age):
        print(f"Second construtor: age is {age}")

obj=Example(45)

class Example:
    def __init__(self,*args):
        if len(args)==1:
            print(f'hello {args[0]}')
        elif len(args)==2:
            print(f'hello {args[0]} your age is {args[1]}')
        
    
obj1=Example('alice')
obj2=Example('bob',20)

class Example:
    def __init__(self,**kwargs):
        if 'name' in kwargs and 'age' in kwargs:
            print(f'hello {kwargs['name']} your age is {kwargs['age']}')
        elif 'name' in kwargs:
            print(f'hello {kwargs[0]}')
    def __del__(self):
        print('object is destroyed.')

obj3=Example(name='alibob',age=76)
del obj3

class DestructorExample:
    def __init__(self,name):
        self.name=name
        print(f"object {self.name} is created.")

    def __del__(self):
        print(f"object {self.name} is destroyed.")

obj4=DestructorExample("carlo")
del obj4
