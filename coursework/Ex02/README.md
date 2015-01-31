Exercise 02: Math and functions
=======

ref. https://github.com/hackbrightacademy/Hackbright-Curriculum/tree/master/Exercise02

Description
-------
We have provided a program, calculator.pyc that implements a basic prefix calculator.  To download the file from github, click on the file, then click on "Raw" to download the file (the browser may place it in your Downloads folder). You will also need arithmetic.py. To download it, click on the filename above, then click "Raw". Then just do File->Save Page As in Chrome and put it in your project directory (i.e. don't work in your Downloads directory). You need both files in the same place to do this exercise.

A pyc is a special python file.  It's python code that has been "compiled" into machine code. You can still run the program, but you can't view the original source of the program.  If you try and look at the file on your terminal (e.g. "cat calculator.pyc") you probably get a bunch of gross garbage outputted.  That's okay, because the computer still knows how to run it.

As you create and run more python programs, you may notice .pyc files get created.  That's fine, they're making things run faster.  However they're not your source code and you probably don't want to check them into version control (git).

Run it with the following command from your shell:

    python calculator.pyc

The calculator lets a user add, subtract, multiply, divide, square a number, cube a number, and find the square root.

Calculator uses the following interface:

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

    Meringue:math chriszf$ python calculator.pyc
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

We have provided a sample arithmetic.py with a function that matches the signature for 'add', although it returns an incorrect value. Your job is to make it return the correct value, then provide the remaining interface.

