class Rule:

    # Elements are the '(' id ')' and stuff like this.    
    # Name is the name that will be used in generation of ply file. To be prettier.
    def __init__(self, elements, name):
        self.elements = elements
        self.name = name

    def getRule(self):
        return self.elements

    def addElement(self, element):
        self.elements.append(element)
