def num_of_blank_squares(step):
    '''Returns the number of blank squares in a square grid filled in by
    circles in a cross pattern.
    Example:
    [0][][][0]
    [][0][0][]
    [][0][0][]
    [0][][][0]
    or:
    [0][][][][0]
    [][0][][0][]
    [][][0][][]
    [][0][][0][]
    [0][][][][0]
    '''
    # if the side length is even, half the side will be a whole integer
    if step%1 == 0:
        num_of_circles = step*4
        area = (step*2)**2
        return area-num_of_circles

    # The side length can also be odd, meaning half the side will be a 
    # decimal ending in .5
    elif step%0.5 == 0:
        num_of_circles = ((step-0.5)*4)+1
        area = (step*2)**2
        return int(area - num_of_circles)

    # Raises ValueError if 'step' is not a valid input
    else:        
        raise ValueError('''parameter should be half of a whole number side of 
            a square''')