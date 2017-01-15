"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   Abstraction hides the "messy" parts or the minutiae behind the code. Using 
   descriptive naming allows for this because it allows the reader to understand 
   what is happening without having to go through every line of code. 

   Encapsulation refers to housing related attributes and methods of a class 
   together. 

   Polymorphism is the quality of being able to extend or modify instances of a 
   class.

2. What is a class?
    A class is an object that we can create and modify. It's structured, it can 
    house data and functions (methods), and are designed for re-usability. 

3. What is an instance attribute?
    An instance attribute is a variable which is defined for each specific
    instance rather than for an entire class. 

4. What is a method?
    A method is a function defined in a class. 

5. What is an instance in object orientation?
    An instance is a data structure created by a class. Calling upon a class 
    forms an instance of said class which contains all of the class attributes 
    as well as any instance attributes assigned during instantiation or after.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is defined for all instances instantiated by a specific 
   class. An instance attribute is defined for each instance upon or after it's 
   instantiation. 

   Class attributes are those that will apply to all instances of the class. 
   Instance attributes are those which will/may vary from instance to instance.
   For example, if you create a Cat class, you would probably define the variable 
   'species' as a class attribute and set it equal to "cat" since all instances 
   of the Cat class will presumably be cats. However, the variable 'name' will 
   likely be defined as an instance attribute since each instance of the Cat 
   class will likely have a different name.

"""


# Parts 2 through 5:
# Create your classes and class methods


class Student(object):
    """Holds student's basic information
    """

    def __init__(self, first_name=None, last_name=None, address=None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Holds questions and answers
    """

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        user_answer = raw_input(self.question +' > ')
        return user_answer.lower() == self.answer.lower()

    # def __repr__(self):
    #     return 'Q: {}\nA: {}'.format(self.question, self.answer)


class Exam(object):
    """Holds exam name and questions
    """

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question, answer):
        self.questions.append(Question(question, answer))

        

midterm = Exam('midterm')
midterm.add_question('What color is the sky?', 'Blue')
print midterm.questions[0].ask_and_evaluate()



