Visitor is design pattern is a way of separating an algorithm from an object structure on which it operates. 
A practical result of this separation is the ability to add new operations to existing object structures without modifying the structures. 
It is one way to follow the open/closed principle.

In essence, the visitor allows adding new virtual functions to a family of classes, without modifying the classes. 
Instead, a visitor class is created that implements all of the appropriate specializations of the virtual function. 
The visitor takes the instance reference as input, and implements the goal through double dispatch.

Other example on Python.

from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class CarElement:
    __metaclass__ = ABCMeta
    @abstractmethod
    def accept(self, visitor):
        raise NotImplementedError(NOT_IMPLEMENTED)

class Body(CarElement):
    def accept(self, visitor):
        visitor.visitBody(self)

class Engine(CarElement):
    def accept(self, visitor):
        visitor.visitEngine(self)

class Wheel(CarElement):
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        visitor.visitWheel(self)

class Car(CarElement):
    def __init__(self):
        self.elements = [
            Wheel("front left"), Wheel("front right"),
            Wheel("back left"), Wheel("back right"),
            Body(), Engine()
        ]

    def accept(self, visitor):
        for element in self.elements:
            element.accept(visitor)
        visitor.visitCar(self)

class CarElementVisitor:
    __metaclass__ = ABCMeta
    @abstractmethod
    def visitBody(self, element):
        raise NotImplementedError(NOT_IMPLEMENTED)
    @abstractmethod
    def visitEngine(self, element):
        raise NotImplementedError(NOT_IMPLEMENTED)
    @abstractmethod
    def visitWheel(self, element):
        raise NotImplementedError(NOT_IMPLEMENTED)
    @abstractmethod
    def visitCar(self, element):
        raise NotImplementedError(NOT_IMPLEMENTED)

class CarElementDoVisitor(CarElementVisitor):
    def visitBody(self, body):
        print("Moving my body.")
    def visitCar(self, car):
        print("Starting my car.")
    def visitWheel(self, wheel):
        print("Kicking my {} wheel.".format(wheel.name))
    def visitEngine(self, engine):
        print("Starting my engine.")

class CarElementPrintVisitor(CarElementVisitor):
    def visitBody(self, body):
        print("Visiting body.")
    def visitCar(self, car):
        print("Visiting car.")
    def visitWheel(self, wheel):
        print("Visiting {} wheel.".format(wheel.name))
    def visitEngine(self, engine):
        print("Visiting engine.")

car = Car()
car.accept(CarElementPrintVisitor())
car.accept(CarElementDoVisitor())
