import os,csv
cwd=os.getcwd()
print(cwd)
os.chdir("c:/Capgemini_Training/Python/Day-9")
print(os.getcwd())

# file=open("sample.txt",'w')
# file.write("hello, this is a sample text.")

# for i in range(3):
#     name,age,id=map(str,input().split())
#     file.append(name+','+age+','+id)

# with open("sample.txt",'r') as file:
#     # content=file.read()
#     # print(content)
#     for line in file:
#         print(line.strip())



rows=[
    ['alice','45','34'],
    ['bob','324','23'],
    ['carlo','67','89']
]
with open("data.csv",mode='a',newline="") as file:
    writer=csv.writer(file)
    writer.writerows(rows)


file.close()