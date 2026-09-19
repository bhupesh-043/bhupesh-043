# def water():
#     for i in range(1, 6):
#         yield f"Glass {i}"


# for glass in water():
#     print(glass)

def numbers():
    for i in range(1, 100):
        yield i

for i in numbers():
    print(i)