from dynamic_array import DynamicArray




dynamic_array = DynamicArray()

#POP method test *****************************************************************************************
# popped empty array 
dynamic_array.pop() 

#Push and Print items method test*************************************************************************

for item in range(10):
    dynamic_array.push(item)

dynamic_array.print_items()


# INSERT AT method test***********************************************************************************

for i in range(10):
    dynamic_array.insert_at(i*10, i)

dynamic_array.print_items()

#REMOVE AT method test************************************************************************************
print('REMOVE AT method is testing')
counter = 0
while True:
    dynamic_array.removeat(counter)
    if dynamic_array.length == 10:
        break
    counter += 1


dynamic_array.print_items()
# dynamic_array.insert_at(777, 4)
# print('after insert')
# dynamic_array.print_items()
# dynamic_array.removeat(0)
# print('after remove')
# dynamic_array.print_items()
# print(f"0. index: {dynamic_array.getitem(0)} ")



# while True:
#     dynamic_array.pop()
#     if dynamic_array.length == 0:
#         break





# for item in range(10):
#     dynamic_array.push(item)


