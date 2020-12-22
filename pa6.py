from CSE8AImage import *

def crop(img, width, height):
    # TODO Write the body of the function here
    crop_img = create_img(height, width,(0,0,0))
    for row in range(len(crop_img)):
        for col in range(len(crop_img[row])):
            crop_img[row][col] = img[row][col]
    return crop_img


def chromascale(img, target):
    # TODO Write the body of the function here
    for row in range(len(img)):
        for col in range(len(img[row])):
            luminance = 0.2126*img[row][col][0] + 0.7152*img[row][col][1] + 0.0722*img[row][col][2]
            ratio = luminance/255
            img[row][col] = (target[0]*ratio,target[1]*ratio,target[2]*ratio)
    return img


def overlay(foreground, background, topLeftrow, topLeftcol):
    #overlays foreground image on top of background at given coordinates: (row,col)
    # TODO Write the body of the function here
    for row in range(len(foreground)):
        for col in range(len(foreground[row])):
            background[row+topLeftrow][col+topLeftcol] = foreground[row][col]
    return background

    
def flip_top_down(img):
    #flips img about horizontal axis
    # TODO Write the body of the function here
    for row in range(len(img)//2):
        for col in range(len(img[row])):
            pixel = img[row][col]
            img[row][col] = img[len(img)-row-1][col]
            img[len(img)-row-1][col] = pixel
    return img


def collage(img):
    #create collage using at least 3 out of the 4 methods in this PA
    # TODO Write the body of the function here
    background = create_img(700,900,(255,0,0))
    texture = load_img("images/texture.jpg")
    heart = load_img("images/heart.jpg")
    new_heart = create_img(122, 140, (0,0,0))
    cat = load_img("images/cat.jpg")
    new_cat = create_img(150, 200, (0,0,0))
    star = load_img("images/star.png")
    for i in range(len(texture)//2):
        for j in range(len(texture[i])):
            temp = texture[i][j]
            texture[i][j] = texture[len(texture)-i-1][j]
            texture[len(texture)-i-1][j] = temp
    for i in range(len(texture)):
        for j in range(len(texture[i])):
            background[i+50][j+50] = texture[i][j]
    for i in range(len(new_heart)):
        for j in range(len(new_heart[i])):
            new_heart[i][j] = heart[i+89][j+80]
    for i in range(len(new_heart)):
        for j in range(len(new_heart[i])):
            background[i+300][j+380] = new_heart[i][j]
    for i in range(len(new_cat)):
        for j in range(len(new_cat[i])):
            new_cat[i][j] = cat[4*i][4*j]
    for i in range(len(new_cat)):
        for j in range(len(new_cat[i])):
            background[i+300][j+100] = new_cat[i][j]
    for i in range(len(star)):
        for j in range(len(star[i])):
            background[i+300][j+660] = star[i][j]
    save_img(background, "collage.jpg")

    
