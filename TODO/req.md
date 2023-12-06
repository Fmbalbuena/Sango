# Sango

Sango is a golfing language, with useful functions. But to make the golfing language usable and easy to use, it requires to meet all of the conditions below:

## Chapter 1:

### Part 1: Types

i) It must have these types:
	1) Number
	2) String
	3) List
	4) Function
i2) It can optionally have these types:
	4) Boolean
ii) The type Number requires to meet one of those conditions:
	1) The Number having real or imaginary values.
	2) The Number being Zero
iii) The type String must meet one of those conditions:
	1) The String being empty String.
	2) The String having at least one character, in the UTF-8 range.
iv) The type List means an group of Numbers, Strings, Booleans or even Itself.
iv2) It doesn't have to be of the same type
v) The type Boolean must be one of those:
	1) True
	2) False
vi) The functions can be in the stack. For more info, see the part 2.

### Part 2: Functions

i) The functions can deal with types.
ii) The functions can be unimplemented for some types
iii) The functions can deal with another functions.

### Part 3: Commands

i) It must have these simple commands, in one character
	1) Addition: `+`
	2) Subtraction `-`
	3) Multiplication
	4) Power

### Part 4: NO-OP

i) The language Sango must only have 3 NO-OP commands or less.
ii) The comment doesn't count as NO-OP
ii2) The multi-char commands that don't do anything doesn't count as NO-OP
