import qrcode
from PIL import Image
from os.path import exists
import os


def writing_file(address):
    print("\nPaste codes here, AND TYPE \"EXIT\" WHEN YOU'RE DONE: \n")
    f = open(address, "w")
    while True:
        inpt = input()
        if inpt.lower() == "exit":
            break
        else:
            f.write("{}\n".format(inpt))
    f.close()


inpt = input(
    "Insert the address/name of your text file (ignore this prompt for the default value): "
)

if inpt == "":
    text_address = "codes.txt"
    print("Your text file: {}".format(text_address))
else:
    text_address = inpt
    print("Your text file: {}".format(text_address))

if len(text_address) < 4:
    text_address += ".txt"

elif not text_address[-3] == "." and not text_address[-4] == ".":
    text_address += ".txt"

print("\n")

if not exists(text_address):
    writing_file(text_address)
else:
    inpt = input(
        "Would you like to edit the file? \nIf you press \"y\", contents will be deleted and you will be able to enter new text. (Y/N): "
    )
    if inpt.lower() == "y":
        writing_file(text_address)

print("\n")

inpt = input(
    "Insert the address/name of your images folder (ignore this prompt for the default value): "
)

if inpt == "":
    folder_address = "images"
    print("Your folder is called: {}".format(folder_address))
else:
    folder_address = inpt
    print("Your folder is called: {}".format(folder_address))

if not exists(folder_address):
    print("Folder doesn't exist. Creating...")
    os.mkdir(folder_address)

print("\n")

text_file = open(text_address, "r")
lista = text_file.read().splitlines()
text_file.close()

for i in range(len(lista)):
    if lista[i].lower() == "exit":
        continue

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,  # velicina slike
        border=2,
    )

    qr.add_data(lista[i])
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("{}/image_{}.png".format(folder_address, lista[i]))

print("Success!")
