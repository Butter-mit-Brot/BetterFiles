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

Create html:
```Python
import BetterFiles as bf

bf.createHTML("file.html", "My Webpage", "Some Text to be there!")
print("created html")
```
Result:

![image](https://user-images.githubusercontent.com/83476809/126047573-faaabd76-e9ac-4d2e-9a4d-321b37abc76f.png)

Create JSON:
```Python
import BetterFiles as bf

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

bf.createJSON("myJson.json", myfamily, indent=4)
print("created JSON")
```
Result:

![image](https://user-images.githubusercontent.com/83476809/126047746-3d800e59-a8cc-467e-8fa0-cf9f5cb6fc06.png)

Copy Files:
```Python
import BetterFiles as bf

bf.copy("Note.txt", "Note-copy.txt")
print("copied")
```
Result:

![image](https://user-images.githubusercontent.com/83476809/126047506-44f1e4d7-eb4a-423b-8def-97269c2edc11.png)

Delete Files:
```Python
import BetterFiles as bf

bf.delete("myJson.json")
print("deleted")
```
Result:

![image](https://user-images.githubusercontent.com/83476809/126047787-94618d5d-41ec-4e02-878c-2d540a55e14b.png)

Create zip folder:
```Python
import BetterFiles as bf

bf.makeZIP("My Zip file.zip", "ABC.txt", "important.txt", "Note.txt")
print("Created Zip!")
```
Result:

![png](https://user-images.githubusercontent.com/83476809/126047866-13426604-65a8-4558-b72e-e5b39b05b08c.png)





