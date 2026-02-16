#!/usr/bin/env python
# coding: utf-8

# Q1 : Lists vs. Tuples in Python
# 
# In python lists are mutable while tuples are not mutable once created <br>
# This makes tuples a little bit faster than lists <br>
# But when we want to work with dynamic data modifying we need to use lists , and if we want to assure none modifyability we need to use tuples .<br>
# The non mutability gives tuple a little bit of an edge while iterating values .
# 

# Q2 . Iterators vs Generators
# 
# Iterators in python are object that contain countable number of values
#  and can be iterated up on . The iterator object implemnts __iter__() and __next__() methods .
# 
# tuples , lists , dicts and sets are iterable objects . They have the iter method
# 

# In[ ]:


mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple) # create an iterator object out of an iterable container

print(next(myit))
print(next(myit))
print(next(myit))


# A Generator is a function that when it is called it returns an iterator object .<br>
# Generators generate value on the fly , they dont store value in memory and thus they are memory efficient.<br>
# The function is only executed when we iterate over it , that means pausable , and state is saved after every yield <br>
# When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off .

# In[ ]:


def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)


# Q3 . What is the purpose of __init__ method in python ?
# 
# It is essentialy similar to constructor class in oop .<br>
# It is used to load and initialize values to instance variables of a class .

# Q4 . what is the task and function of mudules in python .
# 
# Modules in python are files that end with extenstion .py .
#  They are used to implement classes and functions .<br>
# Their main task is to assit in code reusability and structure .
#  This is done by importing files from one to another
#  <br> and use the code from the imported.

# Q5 . . Define the class Fireworks with the two subclasses firecrackers and rockets. Make sure that these two subclasses inherit at least two properties from their superclass and in turn define at least two more properties. define at least two more properties. Also define suitable __init__ and __str__ methods.

# In[ ]:


class Fireworks:
    def __init__(self,color, size):
        self.color=color
        self.size=size
    def __str__(self):
        return f"Firework color:{self.color},and size is {self.size}"
    
class Firecrackers(Fireworks):
    def __init__(self ,color,size,amount, noise):
        super().__init__(color,size)
        self.amount=amount
        self.noise=noise
    def __str__(self):
        return f'Firecracker color:{self.color},size:{self.size},amount:{self.amount},noise:{self.noise}'
    
class Rockets(Fireworks):
    def __init__(self,color,size,speed,height):
        super().__init__(color,size)
        self.speed=speed
        self.height=height
    def __str__(self):
        return f'Rocket color:{self.color},size:{self.size},speed:{self.speed},height:{self.height}'
    
firecracks = Firecrackers("Red","Medium",10,"Loud")
rockets = Rockets("Blue","Large","Fast",500)
print(firecracks)
print(rockets)


# Q6 : Define a regex or a suitable function that implements <br> 
# 1 . Takes str as input <br>
# 2 . Insert a space befor every capital letter 

# In[ ]:


import re

def insert_space(s):
    return re.sub(r"(?<!^)([A-Z])", r" \1", s)

print(insert_space("HelloWorldAgain"))


# In[ ]:


def insert_spaces(text):
    # Use regular expression to insert a space before each uppercase letter
    # The lookbehind assertion (?<!^) ensures no space is added at the start of the string
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
print(insert_spaces("HelloWorldAgain"))


# Q7 . Extract the date from a given url , extract in yyyy/mm/dd <br>
# and return in dd/mm/yyyy
# 
# use regex
# 

# In[ ]:


def extract_dates(text):
    # Regular expression pattern to match dates in YYYY/MM/DD format
    import re
    matches = re.search(r'/(\d{4})/(\d{2})/(\d{2})/',text)
    if matches:
        year, month, day = matches.groups()
        # use last two digits of year
        return f"{day}.{month}.{year[-2:]}"
    else:
        return None
date_text = "https://www.washingtonpost.com/2016/09/02/beckham/"
print(extract_dates(date_text))


# Q8 . You are supposed to develop a spam filter which words in texts with a sequence of asterisks (one per character). in texts. You have found the following program ruin on the Internet, which contains 8 errors. Find theseerrors and correct them.

# In[ ]:


class spamfilter():

    def__init__(self, spam_woerter)          # MISTAKE 1: missing space after `def`
                                             # MISTAKE 2: missing colon at end of definition
        self.wortliste = (                   # OK structurally
            spam_woerter
            if type(spam_woerter) == list
            else spam_woerter.split()
        )

    def star_generator(self, token):
        wrd == ”                             # MISTAKE 3: `==` used instead of assignment
                                             # MISTAKE 4: invalid (smart) quotation mark
        for x in token:
            wrd += ’*’                       # MISTAKE 4: invalid (smart) quotation mark
        return wrd

    def transcode(message):                  # MISTAKE 5: missing `self` parameter
        str = ”                              # MISTAKE 6: shadows built-in `str`
                                             # MISTAKE 4: invalid (smart) quotation mark
        for x in message.split():
            if x not in self.wortliste:      # MISTAKE 7: logic inverted (non-spam masked)
                str = self.star_generator(x) + ’ ’  # MISTAKE 4: invalid (smart) quotation mark
            else:
                str += x + ’ ’               # MISTAKE 4: invalid (smart) quotation mark
        yield str                            # MISTAKE 8: `yield` outside loop → yields once


# In[ ]:


class SpamFilter: # 1ST 
    def __init__(self, spam_words): #2ND 
        self.word_list = spam_words if type(spam_words) == list else spam_words.split()

    def __str__(self):
        return "The spam filter contains the following words :\n" + "\n".join(self.word_list)   

    def star_generator(self, token):
        word = "" #3RD 
        for x in token: 
            word += '*' 
        return word

    def transcode(self, message): #4TH 
        result = "" #5TH 
        for x in message.split(): 
            if x in self.word_list:
                result += self.star_generator(x) + ' ' #6TH 
            else:
                result += x + ' ' #7TH 
                return result.strip() #8TH

