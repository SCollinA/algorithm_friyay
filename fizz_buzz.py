fizz = "Fizz"
buzz = "Buzz"

# for i in range(1, 101):
#     text = ""
#     if i % 3 == 0:
#         text += fizz
#     if i % 5 == 0:
#         text += buzz
#     if text != "":
#         print(text)
#     else:
#         print(i)

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(fizz + buzz)
    elif i % 3 == 0:
        print(fizz)
    elif i % 5 == 0:
        print(buzz)
    else:
        print(i)