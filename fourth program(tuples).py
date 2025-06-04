#Tupless
'''A="apple","mango","banana",1,67,1.23
print(type(A))

b=("Ironman")

print(type(b))           #returns string instead of tuple

print()
b=("Ironman",)
print(type(b))
print()
a=("One plus","Vivo","Redmi","Samsung","Nokia")
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[1::2])
print(a[::-1])

for i in a:
    print(i)

for i in range (len(a)):
    print(a[i])

i=0
while i < len(a):
    print(a[i])
    i+=1

a=("OnePlus","NOKIA","Redmi")
print("before conversion",type(a))

a=list(a)
print("after conversion",type(a))
a.append("vivo")
a=tuple(a)
print(a)
print()
print(a.count("Redmi"))
print(a.index("NOKIA"))
print()

#DICTIONARY
E_Data={"name":"John","age":24,"gender":"male"}

print(E_Data)
print(E_Data["gender"])
print()

student={"name":"John","class":"6th","roll_no":23}
#key  in dictionary

for x in student:
    print(x)                  #gets key
    print(student[x])         #prints value


print()
#using values function
for x in student.values():
    print(x)

for x,y in student.items():        #way to access key value both
    print(x,'-',y)



#Functions in dictionary
x=student.get("name")          #returns value of a key
print(x)
a=student.items()         #retuns items of dict in tuple form
print(a)

b=student.keys()
print(b)
c=student.values()
print(c)

d=student.copy()
print(d)

x=student.setdefault('roll_no',24)         #returns initial value at that place
print(x)

student.update({'roll_no': 25})          #using dictionaries
print(student)

student.update([('roll_no',26)])      #using list of tuples
print(student)
 #for update: if key exists it changes the previous value to new value
 #if key does not exits it adds the key value pair

a = {'x': 1, 'y': 2}
b = {'y': 3, 'z': 4}
a.update(b)
print(a)  # {'x': 1, 'y': 3, 'z': 4}


a = {'x': 1, 'y': 2}
a.update([('y', 5), ('z', 6)])
print(a)  # {'x': 1, 'y': 5, 'z': 6}


a = {'x': 1}
a.update(y=2, z=3)
print(a)  # {'x': 1, 'y': 2, 'z': 3}
print()
print()
y=student.pop('roll_no')
z=student.pop('roll_no','not found')

print(y,z,student)
print()
student.update({'class':"6th"})

print(student)
#pop item removes last item and returns key,value tuple;gives error in case of empty dict
print()
l=student.popitem()

print(l,student)


student.clear() #deletes all elements
print(student)
'''
#NESTED DICTIONARY
'''
A={1:{"Name":"John","age":24,"gender":"male"},2:{"Name":"Lisa","age":23,"gender":"female"}}
print(A)
print(A[1])        #values of key1 not index
print(A[1]["gender"])
print()

#program to sort a dictionary by value
a= {"a": 12, "b": 24, "c": 18, "d": 29, "e": 9}
a=sorted(a.values())           #similarly for keys sorted(a.keys()) can be used
print(a)

#program to print square of keys from 1 to 15 in dict
a={}
for i in range (15):
    a[i]=i**2
print(a)
print()
print()

#program to multiply all vitems in dict
a= {"a": 12, "b": 24, "c": 18, "d": 29, "e": 9}
mult=1
dicti=a.values()             #OR mult*=a[i]
for i in dicti:
    mult=mult*i
print(mult)


#SETS
b={"Ironman","Hulk","Thor","Captain America"}
b.add("Spiderman")
print(b)

#Pop deletes value randomly
b.pop()
print(b)

#want to remove a particular value-remove
b.remove("Thor")
print(b)

b.discard("Hulk")               #deletes value if present ,doesn't raises error if value not present
print(b)

c=b.copy()
print(c)'''

'''
a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder Woman"}
c={"Hulk","Thor"}

print(a.isdisjoint(b))  #Elements of a are not in b-returns true
print(a.isdisjoint(c))

print(c.issubset(a))          #if c is subset of a

print(a.issuperset(c))
print(a.issuperset(b))

a.update(c)
print(a)

print(a.update(b))   #returns none value
print(a)

print(a.clear())      #return none value
print(a)'''
'''
a={"Ironman","Hulk","Thor","Captain America"}
b={"Superman","Batman","Wonder Woman"}
c={"Hulk","Thor","Vision"}

print(a.union(b))
#Differenece returns a-b :common elements are subtracted from a and leftover A's elements are returned

print(a.difference(c))         #Doesn't actually makes difference in original set
print(a)

print(a.difference_update(c))                #returns none value
#makes change in actual set
print(a)


print(a.intersection(c))

a.intersection_update(c)              #gives changes in a
print(a)

print(a.symmetric_difference(c))        #removes common value and provides elements of a & c
print(a)

print(a.symmetric_difference_update(c))
print(a)'''

a={78,90,23,12,34,5,6,45,9,10}
b=max(a)
c=min(a)
print(b,c)

#program to find common elements in 3 list using sets
a=[1,2,3,4,5]
b=[4,5,6,7,8]
c=[4,5,8,10,9]

print(set(a) & set(b) & set(c))



