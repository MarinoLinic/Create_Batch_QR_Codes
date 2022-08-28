# Welcome! 
## This program generates QR codes from text. 

In this folder, you should be able to see a file called "qr.py". 
That's the program that will create QR codes for you.

Additionally, you can add a text file or create an image folder.
It is recommended you name the file "codes.txt" and the folder "images".

---
### TEXT FILE
You need to reference or create a file (either by yourself or once you run qr.py)
which will be used for creating QR codes.

[!] 	Please note that each new line corresponds with a new QR code. 
	The basic structure of your text file should look like this:

	(99)1000(01)5391538350015(8019)7129162622349
	(99)1000(01)5391538350015(8019)7126811273945
	(99)1000(01)5391538350015(8019)7127523507373

---
### QR.PY
You simply need to double click the qr.py file and follow instructions.

But before that, your machine has to have Python and the QRCodes module installed.

If you don't have them, YOU ONLY NEED TO DO ALL THIS ONCE. 

Go to the Windows search bar and type "Command prompt". Then click on the first result.
	- To check if you have python installed, just type "python --version".
	- If you don't get something like "Python 3.xx...", then you need to install it.

	- You can install Python here: https://www.python.org/downloads/ by clicking on "Install Python 3.xx")
		- Run the installation file in your Downloads folder.
		- Follow the default suggestions, ie. just press "next" when installing.)
		- After installing, type "python --version" once again to check it is working.)

	- While still in command prompt, type in another command: pip install qrcode[pil]
	
	- You can now run "qr.py" by double clicking.

When you begin running the qr.py file:
	- It will ask you to name the file your text codes are in. You can just press ENTER for "codes.txt".
		- If you do not have a file, it will create it and let you paste or write text inside.
		- Once you have pasted the contents, press ENTER (ie. new line) and write "exit".

	- If the file exists, it will ask you whether you want to edit the file. 
	  You can press "y" if you do and "n" if you don't. 
	  Once you press "y", all content will be deleted and you will be able to paste new content.
	  Press ENTER (ie. new line) and write "exit".

	- Then, it will ask you to name the folder where your images will be exported to.
		- If the folder doesn't exist, it will be created.

---

So, to recap for first timers:
1. Paste codes in codes.txt
2. Open Windows search, type in "Command prompt", and open it
3. Once in the prompt, type "python --version" to check if you have Python. If you don't -- install it.
4. Type "pip install qrcode[pil]"
5. Double click (run) qr.py
6. Follow instructions. (Create new file, edit file, etc.)
7. Open the images folder

If you have everything installed, the steps you need to take are only:
1. Paste codes in codes.txt
2. Double click (run) qr.py
3. Follow instructions (you can just take the default values and edit existing text files)
4. Open the images folder

If this has been a bit confusing, refer to the example screenshots.