## Problem
* Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 200
* Write a closure that gives you the next Fibonacci number - 100
* We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts - 250
* Modify above such that now we can pass in different dictionary variables to update different dictionaries - 250

## Solution
### Question 1 - ```checker_wrapper```
This function checks if a given function has a valid documentation length (of greater than 50 characters). This is implemented with a closure. ```count``` variable is the free variable. We implement tests to check if the function is implementing closures using ```__closure__``` attribute, boundary tests are also performed. 

### Question 2 - ```fib_wrapper```
This function checks if a given number is a fibonacci number, if it is it returns the next fibonacci number else it throws a ```ValueError```. This is implemented with a closure. ```fib_num``` variable is the free variable. We implement tests to check if the function is implementing closures using ```__closure__``` attribute, boundary tests are also performed. 

### Question 3 - ```counter_simple```
This function counts the number of times a function is being called with the help of dictionary. This is implemented with a closure. ```cnt``` variable is the free variable, ```someDict``` is implemented as a global variable. We implement tests to check if the function is implementing closures using ```__closure__``` attribute, boundary tests are also performed. 

### Question 4 - ```counter_specific```
This function counts the number of times a function is being called with the help of dictionary that the user inputs. This is implemented with a closure. ```cnt``` variable is the free variable. We implement tests to check if the function is implementing closures using ```__closure__``` attribute, boundary tests are also performed. 




