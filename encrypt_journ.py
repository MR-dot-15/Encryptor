import os
import sys
import numpy as np
import PIL.Image as Img

st = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
baselist = list(st + st.lower() + '1234567890.,:;/?!@^()+-_\"\'' + ' ' + '\n')
key = 0

# determining appropriate shape for the output image
def find_shape(num):
    xy = num // 3 + 1
    return int(xy**0.5) + 1


# encypting: comparing input file with baselist
# and the corresponding index goes into array
# key is autoselected if not manually provided
def encrypt(fn1, fn2, k):
    with open(fn1) as file:
        content = list(file.read())
        dim = find_shape(len(content))
        if k == 0:
            k = min([200, 2 * dim])
        else:
            k = key

        array = np.asarray(np.zeros([3 * dim**2]), dtype=np.uint8)
        for index in range(len(content)):
            array[index] = 2 * (baselist.index(content[index]) ^ k)

    img_arr = array.reshape([dim, dim, 3])
    img = Img.fromarray(img_arr)
    img.save(fn2)

# extracting array from picture
# reshaping into an utilizable shape
# key autoselcted, if not blah blah


def decrypt(fn1, k):
    img = Img.open(fn1)
    data = np.asarray(img)
    if k == 0:
        k = min([200, 2 * (int((np.size(data) // 3)**0.5))])

    array = data.reshape([np.size(data)])
    for element in array:
        index = (element // 2) ^ k
        print(baselist[index], end='')


# main part of the programme
# infinte loop until the user chooses to quit
while(True):
    print("\n1: Encrypt \n2: Decrypt \n3: Set a default key \n4: Quit \n")
    inp = int(input())

    if inp == 4:
        sys.exit()

    elif inp == 3:
        key = int(input("Use this key for encryption (<255): "))

    elif inp == 1:
        file = input("File needed to be encrypted (without ext): ")
        out = input("Name of the output file (without ext): ")
        file += ".txt"
        out += ".png"
        encrypt(file, out, key)
        res = input("Delete the original file (y/n): ")
        if res == "y":
            os.remove(file)
    elif inp == 2:
        file = input("File needed to be decrypted (without ext): ")
        #out = input("Name of the output file (without ext): ")
        file += ".png"
        #out += ".txt"
        decrypt(file, key)
    else:
        print("-_- illiterate *****!!\n")
