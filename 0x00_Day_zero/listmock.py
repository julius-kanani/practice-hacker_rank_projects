#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 09:54:19 2022

@author: julius_kanani
"""


"""
Consider a list (list = []). You can perform the following commands:
    insert i e: Insert integer  at position.
    print: Print the list.
    remove e: Delete the first occurrence of integer.
    append e: Insert integer  at the end of the list.
    sort: Sort the list.
    pop: Pop the last element from the list.
    reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands 
where each command will be of the  types listed above. Iterate through each 
command in order and perform the corresponding operation on your list. """

if __name__ == '__main__':
    
    # get number of times a user wants to send commands to the list.
    N = int(input("Enter the number of times: "))
    
    # initialize list to be used.
    result_list = []
    
    # commands list supported in our program.
    commands = {
        "insert": lambda lst, index, element: lst.insert(index, element),
        "print": lambda lst: print(lst),
        "remove": lambda lst, element: lst.remove(element),
        "append": lambda lst, element: lst.append(element),
        "sort": lambda lst: lst.sort(),
        "pop": lambda lst: lst.pop(),
        "reverse": lambda lst: lst.reverse()
        }
    
    # Go through each line of input a user enters.
    for each_input in range(N):
        # get user input and split it where there is a space.
        command_input = input().split(" ")
        
        # get the command name
        command = command_input[0]
        
        # execute the command names with three arguments        
        try:
            commands[command](result_list, int(command_input[1]), 
                              int(command_input[2]))
        except IndexError:
            # execute command names with two arguments.
            try:
                commands[command](result_list, int(command_input[1]))
            except IndexError:
                # execute command names with one argument.
                commands[command](result_list)
            



