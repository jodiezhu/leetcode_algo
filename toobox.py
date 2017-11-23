##Python Basic Syntex
name="Jodie"#string name #in single or double quotes
#Comment
#Multi-line comments
print(name)

#A varable has to start with a letter, then _ or letter
#5 main data types: Numbers, strings lists tuples, dictionaires (maps)
#7 Arithmetic operators : + (plus) -(minus) * (multiplication) / (division) % (Modulus) ** (Exponent - left operand raised to the power of right) //(Floor division - division that results into whole number adjusted to the left in the number line) 
#e.g.
x = 15
y = 2

# Output: x // y = 3  #after comma, It is exactly what's going on
print('x // y =',x//y)

# Output: x % y = 1
print('x % y =',x%y)

# Output: x ** y = 50625
print('x ** y =',x**y)

##Format using print
print("\"I am the best") #If i want to put a quote in the output
multi_line_quote='''Neven give
up'''
print(multi_line_quote)
print("\n" * 3) #back slash n for new lines
print(multi_line_quote)


##List: create a list of value and manipulate them
color_list=["red","pink","yellow","blue"] #keep everything neat
print("My first color is",color_list[0])
