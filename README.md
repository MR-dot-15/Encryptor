# Encryptor
Program capable of encrypting texts into png files, and decrypting them back. 

---

### Intention

Having an easy to use encryptor, time-taken to develop (and modifying) which would be just enough to finish a cup of coffee.

### How to use 

* The easiest way is to download the exe one (packed using Pyinstaller), and to run it. No intented malware included.
* Execute directly/ with cmd.
* 1. While encrypting, the text file (which will be encrypted) and the exe need to inside the same folder. 
  2. Input will be the text file name, **without the .txt part**.
  3. Output will be a png, the program will take its name as input (again, **without .png**).
* While decrypting, the being-in-the-same-folder condition needs to be satisfied. Output will get printed on cmd.
* **Role of 'Key':** Does some XOR stuff. The default setting is easy to use (but, obviously, less 'secured'). 

### Bug

You'll have an idea about it immediately after the first decryption. It's not gonna bother much, I'm too lazy now to fix it. 

### Module dependency:

* Os, Sys
* Numpy, Pillow
