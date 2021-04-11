#  **scratchcloud V3**

A [python](https://www.python.com) interface for using [scratch](https://scratch.mit.edu) cloud variables

Created by [@Classfied3D](https://scratch.mit.edu/users/Classfied3D) and [@PikachuB2005](https://scratch.mit.edu/users/PikachuB2005)
## Getting Started
For ScratchCloud to work, I recommend using a site such as [repl.it](https://replit.com) , 
It works offline as well, but you need to have node.js and npm installed

To start, use the code from [here](https://replit.com/@Classfied3D/scratchcloud-V3) to create a module in the same directory as your program.
Then, you must login to your scratch account with your project ID:

```python
import scratchcloud
cloud = scratchcloud.CloudSession(12345678, 'Username', 'password')
```
I recommend that, intead of putting your scratch password in the code, as all free repls are public, put it in a .env file in the same directory as your main code like this:
### The .env file:
```
password=thisismypassword
```
### The main.py file:
```python
import scratchcloud, os
cloud = scratchcloud.CloudSession(12345678, 'Username', os.environ.get('password'))
```
## Reading cloud variables
* `cloud.getVars(history=1000)` -Returns every cloud variable in the project as a list
* `cloud.getVar(varName, history=1000)` -Returns the value of the cloud variable stated as a string
* `cloud.waitUntilVar(varName, varValue, history=1000)` -Waits until a cloud variable is a certain value
## Editing cloud variables
* `cloud.setVar(varName, varValue)` -Sets the cloud variable in the project stated
* `cloud.changeVar(varName, changeBy)` -Changes the cloud variable in the project stated by a certain value
# Similar modules
* [scratchapi](https://github.com/PolyEdge/scratchapi) -a module for interacting with the scratch website, however some of is broken since the scratch 3.0 update
* [websockets](https://github.com/aaugustin/websockets) -could be used to edit cloud variables
* [scratch3api](https://replit.com/@PikachuB2005/Scratch-3-API-remake) -an updated version of the original [scratchapi](https://github.com/PolyEdge/scratchapi) made by [@PikachuB2005](https://scratch.mit.edu/users/PikachuB2005)
* [scratch-api](https://github.com/trumank/scratch-api) -a node.js module that is used in this module to edit cloud variables
