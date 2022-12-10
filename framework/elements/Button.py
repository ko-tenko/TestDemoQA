from framework.elements.BaseElement import BaseElement


class Button(BaseElement):
    def __init__(self, by_x, locator, name):
        super().__init__(by_x, locator, name)
