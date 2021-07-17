# BetterFiles
A python package to create and maintain Files much easier and "better".

BetterFiles is a library to work with Files!

<hr>

### Installation

Ensure you have at least Python 3.

 ```
 pip install BetterFiles
 or
 pip3 install BetterFiles
 ```

<hr>

### Usage

Import the package!

```Python 
import BetterFiles as bf
```
1 example:
```Python
import BetterFiles as bf

text = "My wonderful Text!"

bf.createF("File.txt", text)
print("created!")
```
Result:
![image](https://user-images.githubusercontent.com/83476809/126047432-1e0119a1-a77c-4d02-afff-976b2aba6ea6.png)

<hr>

### Some examples

Copy Files:
```Python
import BetterFiles as bf

bf.copy("Note.txt", "Note-copy.txt")
print("copied")
```
Result:
![image](https://user-images.githubusercontent.com/83476809/126047506-44f1e4d7-eb4a-423b-8def-97269c2edc11.png)

