#IMPORTING MATH 
import math
x = 12
y = 9

#Return the square root of x
print('the square root of 4 is: ',math.sqrt(4))

#returns next larger integer (roundfigure)
print('The next larger number of 5.324 is: ',math.ceil(5.324))
print('The next larger number of 88.324 is: ',math.ceil(88.324))

#Returns negative of user input integer(positive)
#Returns positive of user input integer(negative)
print('positive to negative conversion of 2.0 is: ',math.copysign(2.0, -0.0))
print('positive to negative conversion of 8.0 is: ',math.copysign(8.0, -0.0))
print('positive to negative conversion of -2.0 is: ',math.copysign(-2.0, 0.0))
print('positive to negative conversion of -8.0 is: ',math.copysign(-8.0, 0.0))

#returns factorial 5! and 4!
print('the factorial of 5 is: ', math.factorial(5))
print('the factorial of 4 is: ', math.factorial(4))

#Returns integer part of user input float number 
print('the integer part of 23.78 is: ',math.floor(23.78))
print('the integer part of 88.78 is: ',math.floor(88.78))

#Return float value of modulus
#Returns the remainder of the division of x by y.
print('the modulus of 21.234 and 7.34 in float type is: ', math.fmod(21.234, 7.34))
print('the modulus of 23 and 7 in float type is: ', math.fmod(23, 7))


#returns GCD(Greatest Common Divisor) of two numbers
print('GCD value of two (36, 60) number is: ', math.gcd(36, 60))
print('GCD value of two (15, 25) number is: ', math.gcd(15, 25))

#Returns the absolute value of the float x and "returns absolute value of a numeric value"
print('absolute value of -2.56 is : ',math.fabs(-2.56))
print('absolute value of π is : ',math.fabs(math.pi))
print('absolute value of 110 is : ',math.fabs(110.56))

#return value of x is either True or False.
print("the math isfinite func: ",math.isfinite(1))
print("the math isfinite func: ",math.isfinite(752))

#Return e raised to the power of x or "returns exponential of x: e power x"
print('the exponential value of 13 is: ',math.exp(13))
print('the exponential value of 44.5 is: ',math.exp(44.5))

#Return the base b logarithm of x
print('the logarithm value of x=200 base b=10 is: ',math.log(200, 10))

#Returns the mathematical constant e = 2.718281…
print('The mathematical constant e is :',math.e)

# Return the natural logarithm of 1+x (base e)
print('the natural logarithm of 1+12 (base e): ',math.log1p(12))

#Return the base 2 logarithm of x
print('the base 2 logarithm of 28: ', math.log2(28))

#Return the base 10 logarithm of x
print('the base 10 logarithm of 13: ',math.log10(13))

# Return x**y (x to the power of y)
print('5 to the power of 4 is: ',math.pow(5, 4))

#Returns mathematical constant π = 3.141592…
print('The pi value is: ', math.pi)

#returns eucledean distance of x i.e.sqrt(x*x + y*y)
print('euclidean distance of ',x,' and ', y, 'is ',math.hypot(x, y))

#Returns sine value of x
print('sine value of ',x,'is: ',math.sin(x))

#Returns cosine value of x
print('cosine value of ',x,'is: ',math.cos(x))

#Return the tangent of x 
print('tangent value of ',x,'is: ',math.tan(x))


#Angular conversion
#Convert angle x from radians to degrees.
print('angle x from radians to degrees: ',math.degrees(x))

#Convert angle x from degrees to radians.
print('angle x from degrees to radians: ',math.radians(x))

'''
Hyperbolic functions
Hyperbolic functions are analogs of trigonometric functions that are 
based on hyperbolas instead of circles.
'''
#Return the hyperbolic cosine of x
print('hyperbolic cosine of x: ',math.cosh(x))

#Return the hyperbolic sine of x
print('hyperbolic sine of x: ',math.sinh(x))

#Return the hyperbolic tangent of x
print('hyperbolic tangent of x: ',math.tanh(x))

#Return the inverse hyperbolic cosine of x
print('inverse hyperbolic cosine of x: ', math.acosh(x))

#Return the inverse hyperbolic sine of x
print('inverse hyperbolic sine of x: ',math.asinh(x))

#Return the inverse hyperbolic tangent of x
#It returns the hyperbolic arc-tangent of the given number.
print('inverse hyperbolic tan of x: ',math.atanh(0.91))
print('inverse hyperbolic tan of x: ',math.atanh(0))


#isint()--integer
#isnan()--number


#use to remove the decimal values
print ("Output of Python trunc() Function: ",math.trunc(286.9999))
print ("Output of Python trunc() Function: ",math.trunc(5.69333))

#to sum up, all the values
print("Output of Python fsum() Function: ",math.fsum([25,23,12,56]))
print("Output of Python fsum() Function: ",math.fsum([.1,.1,.1,.1]))
i =  [1,2,3,4,5,6,7]
print("Output of Python fsum() Function: ",math.fsum((i)))


# sign will be copied
# Here sign of 5 is positive the return value will be 4.0 (positive)
print(math.copysign(4,5))
# Here sign of 5 is negative the return value will be 4.0 (Negative)
print(math.copysign(4,-5))


