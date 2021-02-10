# Mouse Nudger
Ever want to stop your computer from going to sleep temporarily (like when you're downloading a large file overnight) or just want to step away from your computer but *seem* like you're still there (like when you're cooking during a meeting but still listening)?

Enter the Mouse Nudger! It'll move your mouse ever so slightly to stop your computer from going to sleep and programs from marking you as away.

## Virtual Environment and Required Modules Setup
```
$ virtualenv env
$ source env/bin/activate

$ pip install -r requirements.txt
```
To exit the virtual environment:
```
$ deactivate
```

## Parameters
You can update these parameters in the [nudger.py](nudger.py) file to customize it to your liking.

|Parameter|Description|
|--|--|
|time_to_wait|Amount of time in seconds that the program will wait before nudging the mouse again.|
|lower_threshold|Used as the minimum value when calculating the random amount of pixels to move.|
|upper_threshold|Used as the maximum value when calculating the random amount of pixels to move.|

## Running It
Run the nudger with the following:
```
$ python nudger.py
```
It will print out the current position of the mouse and then how much it moved the mouse each time it nudges.
```
(env) ➜  mouse-nudger python nudger.py
Mouse is at position 927, 687.
Moved mouse -4 units horizontally and -11 units vertically.
Moved mouse 11 units horizontally and -11 units vertically.
Moved mouse 8 units horizontally and 3 units vertically.
```
To stop the program, click on the output area and press `CTRL + C`.