## Author: Andrew Rogers
## Description: This program inputs an integer and outputs f(n)
## defined recursively in the homework.

## Methods:

def function(n):
    array = {}

    for i in range(0, int(n)+1):
        if i < 2:
            if i == 0:
                var = 1
            if i == 1:
                var = 2
        else:
            var = calculate_recursion(array, i)
            
        array[i] = var
        
    return array[int(n)]

def calculate_recursion(array, n):
    var = 0
    for i in range(2, int(n)+1):
        var += array[i-1]*array[i-2]
    return 2*var + 1

## Main:

print("Program written by: Andrew Rogers")
_inputsize = input("Please enter an integer: ")
_functionoutput = function(_inputsize)
print(f"f({_inputsize}) = {_functionoutput}")
