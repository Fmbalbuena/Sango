# Sango

Text version `0.0.1`

Sango is a golfing language, with useful functions. But to make the golfing language usable and easy to use, it requires to meet all of the conditions below:


## Chapter 1: Types and elements

### Part 1: Types

**i)** It must have these types:

 1) Number
 2) String
 3) List
 4) Function

**i2)** It can optionally have these types:

 4) Boolean

**ii)** The type Number requires to meet one of those conditions:

 1) The Number having real or imaginary values.
 2) The Number being Zero

**iii)** The type String must meet one of those conditions:

 1) The String being empty String.
 2) The String having at least one character, in the UTF-8 range.

**iv)** The type List means an group of Numbers, Strings, Booleans or even Itself.

**iv2)** The elements of a list doesn't have to be of the same type.

**v)** The type Boolean must be one of those:

 1) True
 2) False

**vi)** The functions can be in the stack. For more info, see the part 2.

**vii)** For more info for every type, see the parts 5-7

**viii)**

### Part 2: Functions

**i)** The functions can deal with types.

**ii)** The functions can be unimplemented for some types

**iii)** The functions can deal with another functions.

### Part 3: Elements

**i)** The language must have these simple elements, in one character

 1) Addition
 2) Subtraction
 3) Multiplication
 4) Power

### Part 4: NO-OP

**i)** The language Sango must only have 3 single-char NO-OP commands or less.

**ii)** The comment syntax doesn't count as NO-OP

**ii2)** The multi-char commands that don't do anything doesn't count as NO-OP

### Part 5: Strings

**i)** The strings can be enclosed in any char, but it must be one char.

**ii)** When the function that has implementation for strings, the strings can't be assumed to be other types.

### Part 6: Numbers

**i)** The Numbers can have decimal points.

**i2)** If the Number has decimal point, the decimal point must be this char: `.`

**ii)** The numbers can be separated by NO-OP or elements.

**iii)** If two or more digits are joined, it forms one integer.

**iv)** The decimal number can be `I.I` or `.I` where I is the integer, as explained above.

**v)** The earliest decimal point has the high priority

**v2)** Example, The code below

    123.324.435

The code above would read as:

    123.324 .435

### Part 7: Lists

**i)** In this language, Lists aren't mutable.

**ii)** Lists aren't sets.

## Chapter 2: Syntax

### Part 1: Control Flow

**i)** The language has While, If, For statements in one char.

**ii)** If statement can be ternary.