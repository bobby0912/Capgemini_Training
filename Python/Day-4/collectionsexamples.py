# a=[10]
# print(len(a))
# for i in range(10):
#     n=int(input())
#     a[i]=n


#list examples

l1=[]
print("Empty List: ",l1)

l2=[0,8,34,7]
print("list of 4 items: ",l2)

#nested lists
l3=['abc',['bcd','def']]
print("nested lists: ",l3)
for i in l3:
    print(i)

l4=list('spam')
print("list vreated from string: ",l4)

l5=list(range(-9,9))
print("list created from ranges: ",l5)

print("slicing :",l5[4:9])
print("length of l5: ",len(l5))

l6=[10,list(range(1,6)),19,20]
print(l6)
print("nested slicing :",l6[1][2:5])

#sum and avg

l7=[4,5,6,7]
print("sum of elements in list: ",sum(l7))
print("Average of elements in a list: ",sum(l7)/len(l7))

ma=mi=l7[0]
for i in l7:
    if(ma<i):
        ma=i
    if(mi>i):
        mi=i
print(ma,mi)



