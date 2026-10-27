# 1.3.1
# 1. No
# 2. By using double //
# 3. ** means power or exponent of the value on the right side 2**-1 = 0.5


# 1.3.2
# 1. Creates a new string with 15 "spam " chained together
# 2. Using triple """ """ or ''' '''
# 3. By using "" or '' in combination "My name is 'Alexander'" for example
# 4. a) 'Hello', b) 'Hello', c) '!'
# 5. len(string)
# 6. string[3] = "h"


# 1.3.3
# 1. a) r == [99, 1, 2, 3, 4, 5, 6, 7], b) s == [100, 1, 2] 
# c) t == [100, 1, 2, 3, 4, 5, 6, 7], d) Yes it will refer to the same object
# 2. len(list)
# 3. 3


# 1.3.4
# 1. It swaps values between a and b
# 2. x = 1; while x < 10: print(x); x+=1;


# 1.4.1
# 1. It has to do with how indentation is interpreted when the code gets compiled


# 1.4.2
# 1. for anim in animal: print(anim);
# 2. Because if we manipulate the original list the iteration would be compromised


# 1.4.3
# 1. for i in range(0,100): print(i)
# 2. x = list(range(0,100))


# 1.4.4
# 1. if we use the 'break' within the for loop the else statement will NOT be run


# 1.4.5
# 1. You use the pass statement


# 1.4.6
# 1. def hello(n: int): for i in range(0,n): print("parrot")
# 2. f will refer to the function we made earlier, or throw an error if no reference to hello exists
# 3. Most everything is stored on the heap
# 4. you can access it by simply referring to it, but if you want to modify it you need to use the 'global' keyword
# 5. animal.append("flea")


# 1.4.7
# 1. 5
# 2. Displays the built in documentation string for print()
# 3. By using triple """ and add text that describes the function


# 1.4.8
# 1. Spaces
# 2. Inserts 4 space characters


# 1.5.1
# 1. a) a.count(1), b) It will not create a new list
# 2. .pop takes the element at the end of the list. [1,2,3] will remain
# 3. [3,4,8,9]
# 4. If you add or remove things to the start of a list it will need to shift n elements one step O(n)


# 1.5.2
# 1. neither of b,c,d
# 2. t will be unpacked and x,y,z will be assigned the values found in t


# 1.5.3
# 1. yeses = {"yes", "yeah", "jop", "ok"}; def ask(answ): if answ in yeses: print("you answered yes");
# 2. set("string")
# 3. set([1,1,2,2,3,3])


# 1.5.4
# 1. x = ["one","two","three"]; for e in x: print(e);
# 2. x = {1:"hej", 2:"hello", 3:"wow"}; for key, value in x.items(): print(f"{key}:{value}");


# 1.5.5
# 1. if 20 <= age <= 65: print("Vad jobbar du med?")
# 2. 'and'


# 1.5.6
# 1. a) TRUE, b) FALSE, c) TRUE, d) FALSE, e) TRUE


# 1.6.1
# 1. 
from prog import getLotto

print(getLotto())


# 1.7.1
# 1. It replaces the empty brackets with the values foud in the parentheses from .format()


# 1.7.2
# 1.

with open("Lab_1/texts.txt", "r") as file:
    for line in file:
        print(line.strip())