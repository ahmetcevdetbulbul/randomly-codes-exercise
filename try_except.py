"""
liste = ["345","sadas","324a","14","kemal"]


for i in liste:
    try:
        i =  int(i)
        print(i)
    except:
        pass


def even(number):
    if number % 2 == 0:

        return number
    else:
        raise ValueError

list = [34,2,1,3,33,100,61,1800]

for i in list:
    try:
        print(even(i))

    except ValueError:
        pass

"""


