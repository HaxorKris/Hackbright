Exercise 03: Interfaces, main loops revisited
=======

ref. https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise03

Description
-------
Now that we've finished our aritmetic functions in Exercise 2, we're going to implement the calculator. You will eventually need to copy your arithmetic.py file from Exercise 2 as you implement your own calculator, but you can use the one provided for now if you like. Do Exercise 3 in a separate directory so you get practice with creating and pushing repos. You can download your starting point for calculator.py by clicking on the filename, opening the Raw version and doing a File->Save Page As in Chrome.

Implement a REPL for a calculator in a file named 'calculator.py'. Your calculator will use the interface from the previous exercise:

    In the file arithmetic.py, these function signatures are required

    add(int, int) -> int
    Returns the sum of the two input integers

    subtract(int, int) -> int
    Returns the second number subtracted from the first

    multiply(int, int) -> int
    Multiplies the two inputs together

    divide(int, int) -> float
    Divides the first input by the second, returning a floating point

    square(int) -> int
    Returns the square of the input

    cube(int) -> int
    Returns the cube of the input

    power(int, int) -> int
    Raises the first integer to the power of the second integer and returns the value.

    mod(int, int) -> int
    Returns the remainder when the first integer is divided by the second integer.


A sample session of the calculator looks like this:
```    
Meringue:math chriszf$ python calculator.py
> + 1 2
3
> - 10 5
5
> * 2 3
6
> / 7 2
3.500000
> square 2
4
> cube 3
27
> pow 2 5
32
> mod 10 3
1
> q
Meringue:math chriszf$
```
We have provided a sample arithmetic.py with dummy stubs that do the wrong thing. When you've completed your REPL, copy your completed arithmetic.py from the previous exercise to the current directory and replace our stubs.

