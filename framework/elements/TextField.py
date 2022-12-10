from framework.elements.BaseElement import BaseElement


class TextField(BaseElement):

    def __init__(self, by_x, locator, name):
        super().__init__(by_x, locator, name)

    def receive_text(self):
        return self.get_text()

    def send_text(self, txt):
        self.send_key(txt)
