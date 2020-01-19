# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 18:53:00 2020

@author: HP
"""

# conditional statements
a = "I am a human being."                                         # statement 1
b = "I am good."                                                  # statement 2
c = "Good graders study well."                                    # statement 3
d = "Humans love graders."                                        # statement 4
e = "Every human does not study well."                            # statement 5
g = "Is every human good grader?"                                 # statement to be proven

# initializing bool values for the given conditional statements
a_value = 0
b_value = 0
c_value = 0
d_value = 0
e_value = 0
f_value = 0
g_values = []                                                     # list to store all truth values of truth table
answer = 1;

# generating truth table with bool values of conditional statements
a_value = 0
for a_value in range(0,2):
    b_value = 0
    for b_value in range(0,1):
        c_value = 0
        for c_value in range(0,2):
            d_value = 0
            for d_value in range(0,1):
                e_value = 0
                for e_value in range(0,2):
                    g_value = 0
                    for g_value in range(0,2):
                        answer = ((not ((a_value) and (c_value and e_value))) or (g_value))
                        g_values.append(bool(answer))
                        g_value+=1
                    e_value+=1
                d_value+=1
            c_value+=1
        b_value+=1
    a_value+=1

# calculating tautology/contradiction
for i in g_values:
    answer*=i
    print(i)

# Answering based on truth table
print(u)
if answer == 1:
    print("The conditional statement provided is Tautology. Hence the answer is Yes.")
elif answer == 0:
    print("The conditional statement provided is Contradiction. Hence the answer is No.")