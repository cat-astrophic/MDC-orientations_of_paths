# This script provides a minimum dominator coloring and the dominator chromatic number of oriented paths

##############################################################################

# Importing required modules

import random
import numpy as np
import networkx as nx
import tkinter as tk
from matplotlib import pyplot as plt

##############################################################################

# Defining the MDC Algorithm for orientations of paths

# Creating a small function to use in the MDC Algorithm for creating new colors

def new_color(C, F):
    
    counter = int(C[len(C)-1][1:len(C)+1]) + 1
    color = 'c' + str(counter)
    C.append(color)
    F.append(color)
    return color

# Running the MDC Algorithm

def MDC(A):
    
    # Initializing information for MDC algorithm
    
    global C, F
    C = ['c0']
    F = []
    alpha = 0
    beta = 0
    
    # Create a standard adjacency matrix from the input arc list
    
    B = np.zeros((length,length))
    
    for a in A:
        
        B[a[0],a[1]] = 1    
    
    # Iterate through vertex set
    
    for i in range(len(B)):
        
        # If d^{-}(v_{i}) == 0, then color with 'c0'
        
        if B[(i-1)%length,i] == 0 and B[(i+1)%length,i] == 0:
            
            F.append('c0')
        
        # Else If there exists an in-neighbor of v_{i} which has out-degree one, then color v_{i} uniquely with a new color
        
        elif (B[(i-1)%length,i] == 1 and B[(i-1)%length,(i-2)%length] == 0) or (B[(i+1)%length,i] == 1 and B[(i+1)%length,(i+2)%length] == 0):
            
            new_color(C, F)
            alpha = 0
    
        # Else If alpha == 0
    
        elif alpha == 0:  

            # And if beta == 0, then color v_{i} uniquely with a new color, c_star, and set alpha and beta to one unless an exception is met
            
            if beta == 0:
                
                c_star = new_color(C, F)
                               
                # This handles the special case for P_6 and the case of 2-chains of the form (0,2,0)
                
                if length == 6 or (B[(i+1)%length,(i+2)%length] == 1 and (B[(i+3)%length,(i+2)%length] == 0 or B[(i+3)%length,(i+4)%length] == 0)):
                
                    alpha = 0
                
                else:
                    
                    alpha = 1
                
                beta = 1
                
            # But if beta == 1, then color v_{i} with c_star and set alpha to one
    
            elif beta == 1:
                
                F.append(c_star)
                alpha = 1
    
        # Else If alpha == 1, then color c_{i} uniquely with a new color andset alpha to zero
    
        else:
            
            new_color(C, F)
            alpha = 0

    # Output a colored graph whose title indicates the dominator chroamtic number of the given oriented path

    # Create an oriented path from the adjacency matrix

    P = nx.DiGraph()
    P.add_edges_from(A)

    # Defining the colormap == RAINBOW!!!!
    
    cm = plt.get_cmap('gist_rainbow')
    
    # Defining the positions for the vertices -- this layout is used to save space yet offer an intuitive image for a path
    
    pos = nx.circular_layout(P)
    
    # Color the vertices according to the output of the MDC Algorithm
        
    for i in range(len(P)):
        
        color = int(F[i][1]) / len(C)
        nx.draw_networkx_nodes(P, pos, nodelist = [i], node_color = [cm(color)], node_size = 600)
    
    # Draw the arcs

    nx.draw_networkx_edges(P, pos, width = 2, arrowsize = 25)
    
    # Display vertex labels
    
    labels = {}
    for i in range(len(P)):
        labels[i] = 'v' + str(i+1)

    nx.draw_networkx_labels(P, pos, labels, font_size = 13)
    
    # Display the oriented path with a minimum dominator coloring from the MDC Algorithm
    
    plt.axis('off')
    plt.title('Oriented path of length ' + str(length) + ' with dominator chromatic number ' + str(len(C)))
    plt.show(P)

##############################################################################

# The GUI

# Some functions for use in the GUI -- these create the adjacency matrices for the oriented path for each option

def get_length():
    
    global length
    length = int(length_entry.get())
    return length
    
def dipath_button_pressed():
    
    length = get_length()
    global A
    A = [(i,i+1) for i in range(length-1)]
    
def no_ones_button_pressed():
    
    length = get_length()
    global A
    A = [(i,i+1) if i%2 == 1  else (i+1,i) for i in range(length-1)]

def random_button_pressed():
    
    length = get_length()
    global A
    r = [random.randint(0,1) for i in range(length-1)]
    A = [(i,i+1) if r[i] == 0 else (i+1,i) for i in range(length-1)]

def left_termination(A, mod2, i):

    A.append((i+1,i))
    mod2.destroy()

def right_termination(A, mod2, i):

    A.append((i,i+1))
    mod2.destroy()

def manual_button_pressed(mod):
    
    length = get_length()
    mod.destroy()
    global A
    A = []

    for i in range(length-1):
        
        # Creating the second GUI
        
        mod2 = tk.Tk()
        
        # Title
        
        mod2.title('Gemerate a Minimum Dominator Coloring of a User Generated Oriented Path')
        
        # Initial text instructions
        
        orient_instructions = tk.Label(mod2, text = 'Choose the orientation of the arc')
        orient_instructions.place(x = 300, y = 10)
        
        # Two buttons with arrows pointing outward as user options
        
        left_button = tk.Button(mod2, text = 'v_i <-- v_i+1', width = 40, command = lambda:[left_termination(A, mod2, i)])
        left_button.place(x = 100, y = 100)
        right_button = tk.Button(mod2, text = 'v_i --> v_i+1', width = 40, command = lambda:[right_termination(A, mod2, i)])
        right_button.place(x = 500, y = 100)
        
        # Setting window size
        
        mod2.geometry('1000x300')
            
        # Executing the second GUI
    
        mod2.mainloop()

# Creating the first GUI

mod = tk.Tk()

# Title

mod.title('Gemerate a Minimum Dominator Coloring of a User Generated Oriented Path')

# Initial text instructions

instructions = tk.Label(mod, text = 'Please select your orientation:', fg = 'black', bg = 'orange', font = 'Helvetica 14 bold', width = 30)
instructions.place(x = 40, y = 7.5)

# Entry for path length

length_text = tk.Label(mod, text = 'Path length:', font = 'Helvetica 11')
length_text.place(x = 60, y = 41.5)
length_entry = tk.Entry(mod)
length_entry.insert(0,1)
length_entry.place(x = 180, y = 42.5)

# Comment for path length entry

length_instructions = tk.Label(mod, text = 'Enter the length of the path here (path length is the size of the vertex set)')
length_instructions.place(x = 350, y = 43)

# Buttons for options to either select: directed path, no ones path, random path, or manually create an oriented path

dipath_button = tk.Button(mod, text = 'Directed Path', width = 40, command = lambda:[dipath_button_pressed(), mod.destroy()])
dipath_button.place(x = 40, y = 70)
no_ones_button = tk.Button(mod, text = 'No Ones Path', width = 40, command = lambda:[no_ones_button_pressed(), mod.destroy()])
no_ones_button.place(x = 40, y = 100)
random_button = tk.Button(mod, text = 'Random Path', width = 40, command = lambda:[random_button_pressed(), mod.destroy()])
random_button.place(x = 40, y = 130)
manual_button = tk.Button(mod, text = 'Custom Path', width = 40, command = lambda:[manual_button_pressed(mod)])
manual_button.place(x = 40, y = 160)

# Comments providing a brief description of what each button does

dipath_instructions = tk.Label(mod, text = 'Select this to create a directed path of the given path length')
dipath_instructions.place(x = 350, y = 73)
no_ones_instructions = tk.Label(mod, text = 'Select this to create a path with no vertices of out-degree one (except one end vertex if the path length is even)')
no_ones_instructions.place(x = 350, y = 103)
random_instructions = tk.Label(mod, text = 'Select this to create a randomly oriented path of the given path length')
random_instructions.place(x = 350, y = 133)
manual_instructions = tk.Label(mod, text = 'Select this to choose the orientation of each edge in the path')
manual_instructions.place(x = 350, y = 163)

# Setting window size

mod.geometry('1000x300')

##############################################################################

# Executing the program

mod.mainloop()
MDC(A)

