# 1.
def hello():
    print('hello user')
hello()

# 2.
def pack(item1,item2,item3):
    item_list = [item1,item2,item3]
    print(item_list)
pack('apple','orange','banana')

# 3.
food_list_1 = []
food_list_2 = ['sushi']
food_list_3 = ['sushi','taco','pizza']
def eat_lunch(food_list):
    if len(food_list) == 0:
        print('My lunchbox is empty')
    elif len(food_list) == 1:
        print(f'I eat {food_list[0]}')
    else:
        print(f'First I eat {food_list[0]}')
        for i in range(1,len(food_list)):
            print(f'Next I eat {food_list[i]}')
eat_lunch(food_list_1)
print('---')
eat_lunch(food_list_2)
print('---')
eat_lunch(food_list_3)  