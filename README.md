# empty-square-sequence
Function that returns the number of blank squares in a square grid filled in by circles in a cross pattern.

from https://edabit.com/challenge/MeScMZ7GqAgyfvNKp:

    The Empty Square Sequence
    In the image below, squares are either empty or filled with a circle.

    [0][0]
    [0][0]

    [0][][][0]
    [][0][0][]
    [][0][0][]
    [0][][][0]

    [0][][][][][0]
    [][0][][][0][]
    [][][0][0][][]
    [][][0][0][][]
    [][0][][][0][]
    [0][][][][][0]

    Steps vs Empty Squarest

    Create a function that takes a number step (which equals HALF the width of a square) 
    and returns the amount of empty squares. The image shows the squares with step 1, 2 
    and 3. The return value is the number of cells not on a diagonal, which is 0 for the 
    first square, 8 for the second, and 24 for the third.

    Examples
    empty_sq(1) ➞ 0
    empty_sq(3) ➞ 24
    empty_sq(10) ➞ 360

    Notes
    - Test input will always be a positive integer.
    - The width of the square will always be even.



