class Student(object):
    
    def __init__(self, first_name, last_name, address):
        """Initialize student information"""
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(Student):

    def __init__(self, question, correct_answer):
        """Initialize question and correct answers"""
        self.question = question
        self.correct_answer = correct_answer

class Exam(Question):

    def __init__(self, name, question, correct_answer):
        """Initialize exam"""
        self.name = name
        self.questions = []
        super(Exam, self).__init__(question, correct_answer)

# Need help with the rest of Part 3

#Part 1:

# 1) The 3 are:
#     a. Polymorphism - Is the ability to create functions that can be applicable to other subclasses  with different types instead of having conditionals on every subclass to identify each type.
#     b. Encapsulation - this allows the relevant features/functionalities of the classes to be near each other and thus easy to find
#     c. Abstraction - is the ability to give a class an abstract attribute that can be applicable to many classes with their own separate features. This would help create less clutter.
# 2) Class is the construction of a container which has functions, methods and attributes. You can create any class you want. Example: class Farm() -> This is how you create a class and within the class you can add all the building blocks like functions, methods and attributes.
# 3) An instance attribute is a variable pertaining to an individual instance created within  a class.
# 4) A method is part of a class and acts similar to a function. The method takes a class instance 'self' and other arguments when defined. It can also be called on an instance like this: 'instance.method()'.
# 5) An instance is a newly created object in a class. Example: fluffy = Pet() -> fluffy  is a newly created instance for the class Pet. This process is called instantiation.
# 6) An instance attribute takes precedence over the class attribute because all instances inherit class attributes whereas the instance attribute is unique to its specific instance. Example:

# Class creation:
#  class Zoo(object):
#     pet_type = "zebra"

# Instantiation 1:
# fluffy = Zoo()
# fluffy.pet_type = 'cub'

# In this case my instance has a unique attribute that does not satisfy it's class attribute, therefore it will override what the class attribute has and be relevant to the instance.

# Instantiation 2:
# Milky = Zoo()
# Milky.pet_type => zebra

# However, if my second newly created instance doesn't have specified attribute, it will inherit it's class's attribute as it's own. This is very helpful and saves the user from redundancy.
