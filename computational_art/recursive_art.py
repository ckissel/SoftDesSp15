""" Caleb Kissel Project 2 """

import math
import random
from PIL import Image

"""Overall good job! Work on adding tests and more comments to your code. Check my comments for more specific
feedback"""


#Function Definitions
def prod(a,b):
    return a*b
def avg(a,b):
    return .5*(a+b)
def cos_pi(a):
    return math.cos(math.pi*a)
def sin_pi(a):
    return math.sin(math.pi*a)
def squarert(a):
    return math.sqrt(abs(a))
def square(a):
    return a**2
def x0(a,b):
    return a
def y0(a,b):
    return b
blocks={0:"prod",1:"avg",6:"cos_pi",7:"sin_pi",4:"squarert",5:"square",2:"x0",3:"y0"}
args={"prod":2,"avg":2,"cos_pi":1,"sin_pi":1,"squarert":1,"square":1,"x0":2,"y0":2}

#I really like how you made all of these split into seperate unctions. Great coding practice! :)

# However...you might want to wrap these variables blocks and args inside build_random_function rather than
# out in the open. People try to avoid having too many global variables in their file so that it won't clash
# and conflict with other variable names. If it's defined in a function, it's only locally defined to that function,
# which is all you need here. Also..there might be a python defined thing called args already - I may be wrong
# but just be careful with that 


def build_random_function(min_depth, max_depth):
    # print 'buildrandomfunc'
    """ Builds a random function of depth at least min_depth and depth
        at most max_depth (see assignment writeup for definition of depth
        in this context)

        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function
        returns: the randomly generated function represented as a nested list
                 (see assignment writeup for details on the representation of
                 these functions)
    """
    depth = random.randint(min_depth, max_depth)
    if depth==1:                                #if this is the bottom call, return x or y
        return [blocks[random.randint(0,3)]]
    myFunc=blocks[random.randint(0,7)]
    params=args[myFunc]
    finalList=[]
    finalList+=[myFunc] #append or extend instead of += as better practice when modifying variables in place
    for i in range(0,params):
        finalList+=[build_random_function(depth-1,depth-1)]
    return finalList

    #Nice. Add some comments and doctests though
    

def evaluate_random_function(f, x, y):
    """ Evaluate the random function f with inputs x,y
        Representation of the function f is defined in the assignment writeup

        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function
        returns: the function value

        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02
    """
    if len(f)==1:    #check base case
        # print f[0],"BASE"
        if f[0]=="x0":
            return x0(x,y)
        if f[0]=="y0":
            return y0(x,y)
        if f[0]=="prod":
            return prod(x,y)
        if f[0]=="avg":
            return avg(x,y)
        if f[0]=="square":
            return square(x,y)
        if f[0]=="squarert":
            return squarert(x,y)
        return 'error1'
            #done checking base case. Only need to provide for possible base cases
    # print f[0], "NORMAL"
    if f[0]=="x0":
        return x0(evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))
    if f[0]=="y0":
        return y0(evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))
    if f[0]=="prod":
        return prod(evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))
    if f[0]=="avg":
        return avg(evaluate_random_function(f[1],x,y),evaluate_random_function(f[2],x,y))
    if f[0]=="cos_pi":
        return cos_pi(evaluate_random_function(f[1],x,y))
    if f[0]=="sin_pi":
        return sin_pi(evaluate_random_function(f[1],x,y))
    if f[0]=="square":
        return square(evaluate_random_function(f[1],x,y))
    if f[0]=="squarert":
        return squarert(evaluate_random_function(f[1],x,y))
    
    return 'error'

    #Good. Add tests though!

def remap_interval(val, input_interval_start, input_interval_end, output_interval_start, output_interval_end):
    """ Given an input value in the interval [input_interval_start,
        input_interval_end], return an output value scaled to fall within
        the output interval [output_interval_start, output_interval_end].

        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values
        returns: the value remapped from the input to the output interval

        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    x=(float(val)-float(input_interval_start))
    y=(float(input_interval_end)-float(input_interval_start))
    z=x/y
    return output_interval_start+(z*(output_interval_end-output_interval_start))

    #nice and concise. Good job.


def color_map(val):
    """ Maps input value between -1 and 1 to an integer 0-255, suitable for
        use as an RGB color code.

        val: value to remap, must be a float in the interval [-1, 1]
        returns: integer in the interval [0,255]

        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """ Generate test image with random pixels and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """ Generate computational art and save as an image file.

        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    
    red_function = build_random_function(7,15)
    green_function = build_random_function(7,15)
    blue_function = build_random_function(7,15)
    
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                    color_map(evaluate_random_function(red_function, x, y)),
                    color_map(evaluate_random_function(green_function, x, y)),
                    color_map(evaluate_random_function(blue_function, x, y))
                    )

    im.save(filename)


if __name__ == '__main__':
    import doctest
    # print evaluate_random_function([["x0"],["y0"],["x0"]],1,0)
    #doctest.testmod()
    # Create some computational art!
    # TODO: Un-comment the generate_art function call after you
    #       implement remap_interval and evaluate_random_function
    # print evaluate_random_function(red_function,1,0)
    generate_art("example5.png",500,500)
    # Test that PIL is installed correctly
    # TODO: Comment or remove this function call after testing PIL install
    # test_image("noise.png")
