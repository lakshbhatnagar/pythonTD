# importing modules
import hou
import sys
from PySide2.QtWidgets import *

# Native hou command
def houdiniPopup():
    hou.ui.displayMessage("Working!")
    pass

# PySide Code
## Creating Pyside Widget
window = QWidget()

## Setting Window Title
window.setWindowTitle("PySide2 Window")

## Setting Window Size
window.setFixedHeight(600)
window.setFixedWidth(1000)

## Creating PySide PushButton
button = QPushButton("Test Button", window, clicked=houdiniPopup)

# Execute Window
window.show()
