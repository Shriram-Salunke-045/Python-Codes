a=[1,2,3,4,5] # List

print(a[1],a[3],a[4]) # indexing

print(a[0:5]) #  Slicing
print(a)

b=[1,"Shriram",76.46] # differnt data types
print(b)
print(b[1])

b[0]=4 # List is mutable
print(b)

x=[]
dir(x)
print(dir(x)) # methods inn list

# append meethod
x=[20,40,50,60]
x.append(89)
print(x)

# insert metho
x.insert(3,67)
print(x)

# clear method
x.clear()
print(x)

# calculate length of list
y=[1,23,5,4]
len(y)
print(len(y))

# concatenate the list
p=[1,2,3,4]
q=[5,6,7,8]
r=p+q
print(r)

# pop method
r.pop()
print(r)

# remove method 
r.remove(4)
print(r)

# reverse method
r.reverse()
print(r)

# sort method
r.sort()
print(r)

# count method
shri=[1,2,3,2,2,4,2]
ram=shri.count(2)
print(ram)

#copy method
s=r.copy()
print("r: ",r)
print("s: ",s)


# extend method
gaurav=[9,6,1,8]
neha=[0,9,2,0]
gaurav.extend(neha)
print(gaurav)

#index method
print(r.index(5))