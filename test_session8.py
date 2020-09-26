import inspect
import os.path
import re
import pytest
import session8
from session8 import *

README_CONTENT_CHECK_FOR = [
    'checker_wrapper',
    'fib_wrapper',
    'counter_simple',
    'counter_specific',
    'closure',
    'fibonacci', 
    'global', 
    'dictionary'
]

def test_readme_exists():
    '''
    Test 1 : tests if readme file exists.
    '''
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    '''
    Test 2 : tests if readme file is descriptive enough.
    '''
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 300, "Make your README.md file interesting! Add atleast 400 words"

def test_readme_proper_description():
    '''
    Test 3 : tests if reame file has all the key functions explained. 
    '''
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    '''
    Test 4 : tests if readme file has proper formatting.
    '''
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_q1():
    def somefunc():
        '''
        This documentation has more than 50 characters. It is true.
        '''
        return False
    
    checkdoc = checker_wrapper()
    assert checkdoc(somefunc) == True, "Documentation has less than 50 characters!"

def test_q1_2():
    def someotherfunc():
        """This documentation has less than 50 characters."""
        return False
    checkdoc = checker_wrapper()
    assert checkdoc(someotherfunc) == False , "Documentation has more than 50 characters!"
    
def test_q2():
    next_fib_num = fib_wrapper()
    assert next_fib_num(610) == 987, " Next Fibonacci function implemented incorrectly!"

def test_q2_2():
    with pytest.raises(ValueError):
        next_fib_num = fib_wrapper()
        next_fib_num(61)

def test_q3():
    counter_add = counter_simple(add)
    assert counter_add(3,4) == 7, "Addition not implemented correctly!"

def test_q3_2():
    counter_add = counter_simple(add)
    assert someDict['add'] == 1, "Dictionary implemented incorrectly!"

def test_q3_3():
    counter_mult = counter_simple(mult)
    counter_mult(7,10)
    assert someDict['mult'] == 1, "Dictionary implemented incorrectly!"

def test_q3_4():
    counter_div = counter_simple(div)
    counter_div(7,10)
    assert someDict['div'] == 1, "Dictionary implemented incorrectly!"
    
def test_q4():
    someDict2 = {}
    counter_add = counter_specific(add,someDict2)
    someDict2 = counter_add(3,4)
    assert someDict2['add'] == 1, "Dictionary implemented incorrectly!"

def test_q4_2():
    someDict2 = {}
    counter_mult = counter_specific(mult,someDict2)
    someDict2 = counter_mult(3,4)
    assert someDict2['mult'] == 1, "Dictionary implemented incorrectly!"
    
def test_q4_3():
    someDict2 = {}
    counter_div = counter_specific(div,someDict2)
    someDict2 = counter_div(3,4)
    assert someDict2['div'] == 1, "Dictionary implemented incorrectly!"

def test_q4_4():
    someDict2 = {}
    counter_mult = counter_specific(mult,someDict2)
    someDict2 = counter_mult(3,4)
    counter_div = counter_specific(div,someDict2)
    someDict2 = counter_div(3,4)
    assert someDict2['div'] == 1 and someDict2['mult'] == 1 , "Dictionary implemented incorrectly!"

def test_q4_5():
    someDict2 = {}
    counter_mult = counter_specific(mult,someDict2)
    someDict2 = counter_mult(3,4)
    counter_div = counter_specific(div,someDict2)
    someDict2 = counter_div(3,4)
    counter_add = counter_specific(add,someDict2)
    someDict2 = counter_add(3,4)
    assert someDict2['div'] == 1 and someDict2['mult'] == 1 and someDict2['add'] == 1 , "Dictionary implemented incorrectly!"
    
def test_q1_closure():
    def somefunc():
        '''
        This documentation has more than 50 characters. It is true.
        '''
        return False
    checkdoc = checker_wrapper()
    checkdoc(somefunc)
    assert len(checkdoc.__closure__)

def test_q1_closure2():
    def somefunc():
        '''
        This documentation has more than 50 characters. It is true.
        '''
        return False
    with pytest.raises(TypeError):
        len(somefunc.__closure__)

def test_q2_closure():
    next_fib_num = fib_wrapper()
    assert len(next_fib_num.__closure__)

def test_q3_closure():
    counter_add = counter_simple(add)
    assert len(counter_add.__closure__) == 2
    
def test_q4_closure():
    somedict3 = {}
    counter_add = counter_specific(add,somedict3)
    assert len(counter_add.__closure__) == 3