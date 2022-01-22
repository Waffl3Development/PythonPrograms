# PythonPrograms
This Github repository is used for overall file, test file and reference file storage that may be referenced at any time, any libraries or incorporated files will also be stored here

These files are completely free to access and copy AS A REFERENCE for learning python

Linter info:
If you are using atom editor: https://atom.io/ I highly recommend installing linter this will check your code for errors every time you save your document, First you need to have python and atom editor installed if you do not then install them now

this can be done by either going to file -> settings -> install on windows, atom -> preferences -> install (Mac)  Edit -> Preferences -> install (Linux)

search linter and you should see something that pops up with the subtext "A Base Linter with Cow Powers"

next search for pylint and install linter-pylint (this is specifically for python it will be different for different programming languages)

this is now all good for atom however you will also need to install pylint using pip in python,

First open your terminal or command line (winKey then type cmd and hit enter or search for terminal on mac and linux) and type the word pip and hit enter

if it responds with "pip is not recognized as an internal or external command ... " or something similar continue, otherwise jump down to the *  

either copy and paste or type exactly:
  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
and hit enter

next type
  python3 get-pip.py
(you can also just use python instead but python3 makes sure it installs to python3 and not to another python instance, if no other instance is installed either will work)

exit your terminal or command prompt and relaunch them (this refreshes environmental variables) and type pip and hit enter

*
After making sure you have pip installed simply install pylint by typing
  pip install pylint
This should automatically download and configure pylint

Restart atom editor and any python files you open in atom will now have linter enabled

Finally you may notice that linter outputs a bunch of Info tags that take up space and are generally not helpful to fix this simply download the .pylintrc from my GitHub page and place it into the same folder as your .py files, this will tell linter to ignore those info tags and it should only show warnings and errors  
