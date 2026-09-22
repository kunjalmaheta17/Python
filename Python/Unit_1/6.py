#  Write a program to illustrate the use of tuples and sets with basic operations. 

t1=(10,20,"hii",2.5,'d')
print("Type :",type(t1))

print("Tuple :",t1)

print("Indexing : ",t1[0])
print("Negative Indexing : ",t1[-1])
print("Slicing : ",t1[2:5])

print("Concatenation : ",t1+("hello",20))
print("Repetition : ",t1*2)
print("Length : ",len(t1))
print("Count : ",t1.count("hii"))

s1={10,20,30,'hiii',2.3}
s1.add(25)
print(s1)
