"""
CSC 131
Chapter 8 - GUI (Graphical User Interfaces)
"""
from breezypythongui import EasyFrame


class LabelDemo(EasyFrame):
    """
    Displays a greeting in a window
    """

    def __init__(self):
        """
        Set up the window and the label
        """
        EasyFrame.__init__(self)
        self.addLabel(text="Hello world!", row=0, column=0)


def main() -> None:
    """
    Instantiates and pops up the window
    :return: None
    """
    LabelDemo().mainloop()
