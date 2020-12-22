from CSE8AImage import *

# PART 1.1
# TODO: Write the function as given in PA specifications
def make_menu(fruits, toppings):
    menu = []
    for f in fruits:
        for t in toppings:
            menu.append(str(f) + " ice cream with " + str(t))
    print(menu)



# PART 1.2
# TODO: Write the function as given in PA specifications
def multiplication_table(num, table):
    for i in range(num):
        lst = [*range(1,num+1,1)]
        for j in range(len(lst)):
            lst[j] = lst[j]*(i+1)
        print(lst)


# PART 1.3
def complement(img):
    # TODO: Complete the function body
    for row in range(len(img)):
        for column in range(len(img[row])):
            pixel = img[row][column]
            img[row][column] = (pixel[0], pixel[2], pixel[1])
    return img


def negative(img):
    for row in range(len(img)):
        for column in range(len(img[row])):
            pixel = img[row][column]
            img[row][column] = (255-pixel[0], 255-pixel[1], 255-pixel[2])
    return img







