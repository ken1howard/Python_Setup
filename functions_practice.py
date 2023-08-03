def hello():
    print("Welcome to our website")

def pack(bags, luggage, backpacks):
    return [bags, luggage, backpacks]

my_list = ["steak", "chips", "cookies", "crackers"]

def eat_lunch(my_list):
    if not my_list:
        print("My lunchbox is empty")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[i]}")
            else:
                print(f"Next I eat {my_list[i]}")

hello()
print(pack("bags", "luggage", "backpacks"))
eat_lunch(my_list)
