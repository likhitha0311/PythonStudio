mylist=[]
nums=[1,2,3,4,5]

for every_item in nums:
    mylist.append(every_item)

print(mylist)

#List Comprehension
mylist_com=[every_item for every_item in nums]
print(mylist_com)

#Example 2
mylist=[]
for every_item in nums:
    mylist.append(every_item*every_item)

print(mylist)
myl=[every_item*every_item for every_item in nums]
print(myl)

#Example 3
mylist=[]
for every_item in nums:
    if  every_item%2==0:
        mylist.append(every_item)

print(mylist)
my=[every_item for every_item in nums if  every_item%2==0]
print(my)

#Example 4
mylist=[]
for every_letter in 'abcd':
    for every_number in range(5):
        mylist.append((every_letter,every_number))

print(mylist)
my_tup=[(every_letter,every_number) for every_letter in 'abcd' for every_number in range(4)]
print(my_tup)

#Exmaple 5 with dictionary
names=('lATIN','Beck','Jen','Marconi')
characters=('blackman','whiteman', 'brownman')
zip(names,characters)


my_dict={}
for n,c in zip(names,characters):
    my_dict[n]=c

print(my_dict)
my1={n:c for n,c in zip(names,characters) if n!= 'Beck'}
print(my1)


#Exmaple 6 with set
set1={1,22,22,33,44,11,1,1,22,33}
new_set=set(set1)
print(new_set)
empty_set=set()

for every_element in set1:
    empty_set.add(every_element)
print(empty_set)

#generator function
def gen_function(nums):
    for every_element in nums:
        yield every_element*every_element

my_list=gen_function(nums)

for i in my_list:
    print(i)

#with comprehension for above code
my_list=(every_element*every_element for every_element in nums)
for i in my_list:
    print(i)





