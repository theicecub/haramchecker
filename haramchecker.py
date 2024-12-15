haram_things = ["Bad words", "Drink alcohol", "Kill people", "Do drugs", "Bullying", "Abuse", "Eat pork", "Polytheism"]

def check(something):
    if something in haram_things:
        print(f"{something} is haram")
    else:
        print(f"{something} is not haram")
