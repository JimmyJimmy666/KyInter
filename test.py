# import KyInter
from KyInter.KySetups import Setup
from KyInter.KyCore import Position, Size
from KyInter.KyWidgets import MainWindow, Font, Label

# if you want a high definition, enter this
Setup.setHighDefinition(True)

# create a simple window
mainWindow = MainWindow()
mainWindow.setTitle("MyWindow") # set title
mainWindow.setSize(Size(400, 300)) # set size

# create a font
# family is modern "Microsoft YaHei" (Chinese)
# size is 12
# enable bold, italic, underline and overstrike
font = Font(family="Microsoft YaHei", 
            size=12, 
            bold=True, 
            italic=True, 
            underline=True, 
            overstrike=True
            )

# create a label
# use newly created font
label = Label(mainWindow, "COOL TEXT", font)
label.setPosition(Position(131, 117))

# finally, exec
mainWindow.exec()