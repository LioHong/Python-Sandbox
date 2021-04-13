# -*- coding: utf-8 -*-
"""
Filename: three_dim_pandas.py
Date created: Fri Apr  9 15:27:16 2021
@author: Julio Hong
Purpose: Represent a three-dimensional grid using Pandas library. Serve as a prototype for a four-dimensional grid which probably would be in a 3D GUI.
Just a little project to get me used to coding again. I know this is one of the worst engines to use.
Why not do this in Excel/LibreCalc instead? Because I can't draw shapes.
It's like taking slices of a 3D shape. But this idea sounds more tedious the further I go.
At the very least this will be a way for me to generate a multi-index df with two vertical indexes and one column index. Took me about 1.5hr to achieve.
Steps: 
1. Input the dimensions of the grid
2. Display all layers of the grid
"""
import numpy as np
import pandas as pd
import itertools
# To adjust the dataframe appearance
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 200)

# Ask the user for the length, width and height of the grid
# Length is the horizontal dimension
# Width is the vertical dimension
# Height is the number of layers

def enter_lwh():
    # print('Please enter the length, width and height in the format [L, W, H].')
    # grid_lwh = input()
    # # Check that the input is a list of integers.

    # while type(grid_length) != int and type(grid_width) != int and type(grid_height) != int:
    #     if type(grid_length) != int:
    #         print('Please enter the length.')
    #         grid_length = input()
    #     if type(grid_width) != int:
    #         print('Please enter the width.')
    #         grid_width = input()
    #     if type(grid_height) != int:
    #         print('Please enter the height.')
    #         grid_height = input()
    #
    #
    # # User inputs the dimension.
    # # Check if the input is type int
    # # If not, raise an error and repeat.
    #
    # # Check that the inputted values are all integers
    # # Otherwise, repeat the loop.

    # This code is ok for getting user inputs.
    # Initialise as NoneType to start the loop
    grid_length, grid_width, grid_height = None, None, None
    # This can be adjusted for any number of dimensions.
    lwh_questions = [['Please enter the length.', grid_length],
                     ['Please enter the width.', grid_width],
                     ['Please enter the height.', grid_height]]

    # While loop repeats for number of desired dimensions i.e. 3.
    for qn_and_input in lwh_questions:
        while type(qn_and_input[1]) != int:
            print(qn_and_input[0])
            qn_and_input[1] = input()
            # Raise error if input is not type int
            # Kind of redundant with the double check but it's for the user.
            try:
                qn_and_input[1] = int(qn_and_input[1])
            except:
                # if type(qn_and_input[1]) != int:
                print('Input is not an integer. Please try again.')

    # Return the inputted dimensions.
    lwh_dim = [qn_and_input[1] for qn_and_input in lwh_questions]
    print('Your inputted grid dimensions are ' + str(lwh_dim))
    return lwh_dim

def grid_display():
    # lwh_dim = enter_lwh()
    # If the grid is too large then the points don't work? If any of the coords has value>10.
    # lwh_dim = [9, 10, 11]
    lwh_dim = [11, 11, 11]
    # lwh_dim = [10, 10, 10]
    # lwh_dim = [7, 8, 9]
    # lwh_dim = [5, 6, 7]
    dim_letters = ['x', 'y', 'z']
    dim_labels = []

    # Use the length and width to generate the 2D grid.
    # Then create multiple layers using the height.
    # Each layer will be a separate 2D grid.

    # Generate labels for x, y and z-coords based on the lwh_dim
    # Label columns as x0, x1, x2...
    # Label outer row index as z0, z1, z2...
    # Label inner row index as y0, y1, y2...
    for i in range(len(dim_letters)):
        temp_labels = [dim_letters[i] + str(j) for j in range(lwh_dim[i])]
        dim_labels.append(temp_labels)

    # Use a multi-index dataframe where the vertical axis is multi-indexed.
    idx = pd.MultiIndex.from_product([dim_labels[2], dim_labels[1]])
    df = pd.DataFrame(index=idx, columns=dim_labels[0])

    # Limitation is that the heights are reversed - they ascend downwards.
    # It's a vertically-flipped upper-left quadrant of a Cartesian plane
    # Anyway this view is not intuitive at all.

    return lwh_dim, dim_labels, df

# Drawing shapes. Solid vs Outline.
# Actually all I can think of are squares and cubes.
# How to draw inside? Slowly label each the dimensions and origin of each shape? Slow and clunky.

def draw_solid_cube():
    # Fill all the points within a volume with a symbol 'X'
    # Volume meaning an area that stretches over multiple z-layers.
    # To draw a cube, two points are required: The opposite corners.
    # Find the labels of the points to fill based on the two corners.
    lwh_dim, dim_labels, df = grid_display()
    cube_labels = []

    # I'm not going to put any loops for the input this time.
    # Input the list of numbers as #1,#2,#3
    print('What are the coords for the first corner?')
    corner_01 = [int(x) for x in input().split(',')]
    print('What are the coords for the second corner?')
    corner_02 = [int(x) for x in input().split(',')]

    # Insert a check that compares the coord to the max value on the respective axis.
    # If the coord is lower than or equal to the max value, use the coord value.
    # But if the coord is greater than the max value, use the max value instead.
    # Raise a warning also.

    # Truncate dim_labels to find cube_labels which represent the axis-values which will contain 'X'.
    for i in range(len(dim_labels)):
        temp_labels = dim_labels[i][corner_01[i]:corner_02[i]+1]
        cube_labels.append(temp_labels)

    # But what if both corners have coord values greater than max value?

    # Now to set value of the cells based on the labels
    # I can iterate over the cube_labels to get each 3D point.
    for x in cube_labels[0]:
        for y in cube_labels[1]:
            for z in cube_labels[2]:
                print(str(x) + ',' + str(y) + ',' + str(z))
                # df.loc works when the coord-value >10, while the other indexing method works when coord-value <=10.
                # df[x][z][y] = 'X'
                df.loc[(z, y), x] = 'X'

    return df

# Outline would involve finding all the corners and drawing straight lines between them, which is more tedious.
def draw_framed_cube():
    # My intuition was correct. This framed function was way harder to write than the solid function.

    # A cube has 12 edges.
    # Either draw the solid cube and remove the interior and faces. Or draw each of the edges.
    # A cube has 8 corners. Permutations of the three coord value-pairs: 2**3.
    # Two corners remain the same except for one value. All points along the line between those corners also differ in one value only.
    # Expected results: Top and bottom layers of the frame should be squares. Interior layers should only show the four corners.

    lwh_dim, dim_labels, df = grid_display()
    cube_labels = []

    # COPY-PASTED. PACKAGE LATER.
    # I'm not going to put any loops for the input this time.
    # Input the list of numbers as #1,#2,#3
    print('What are the coords for the first corner?')
    corner_01 = [int(x) for x in input().split(',')]
    # corner_01 = [1,1,1]
    print('What are the coords for the second corner?')
    corner_02 = [int(x) for x in input().split(',')]
    # corner_02 = [3,4,5]

    cube_corners = [corner_01, corner_02]
    cube_edges = {}

    # Insert a check that compares the coord to the max value on the respective axis.
    # If the coord is lower than or equal to the max value, use the coord value.
    # But if the coord is greater than the max value, use the max value instead.
    # Raise a warning also.

    # A cube has 8 corners. Permutations of the three coord value-pairs: 2**3.
    def corners(corner, temp):

        # Add the points of the edge between the initial corner and the temp corner.
        # Each point will +1 to the value that changes between the initial corner and temp corner.
        # Select the delta-point based on the index.
        # +1 to the delta-point.
        # Create a new edge-point.
        # Can use a for-loop, but I'd prefer list comprehension.

        # Assume that corner_02 has higher absolute coord values. range() doesn't do negative step unless an argument is passed.
        # Oh... I need to find out which is lower and add the value to that. Or do negative step.
        # Find the arithmetic difference between corners
        delta_corner = np.array(temp) - np.array(corner)
        # Find the direction based on which corner is larger.
        delta_check = np.min(delta_corner)
        # If the TCA has greater value.
        if delta_check >= 0:
            index = np.where(delta_corner == np.max(delta_corner))[0][0]
            # Initialise as empty list to allow appending later.
            cube_edges[(tuple(corner), tuple(temp))] = []
            for j in range(1, np.max(delta_corner)):
                edge_point = corner.copy()
                edge_point[index] += j
                cube_edges[(tuple(corner), tuple(temp))].append(edge_point)

        # If the TCA has lower value.
        else:
            index = np.where(delta_corner == delta_check)[0][0]
            cube_edges[(tuple(corner), tuple(temp))] = []
            for j in range(1,-delta_check):
                edge_point = temp.copy()
                edge_point[index] += j
                cube_edges[(tuple(corner), tuple(temp))].append(edge_point)

    for i in range(len(corner_01)):
        temp_corner_alpha = corner_01.copy()
        temp_corner_alpha[i] = corner_02[i]

        temp_corner_beta = corner_02.copy()
        temp_corner_beta[i] = corner_01[i]

        cube_corners.append(temp_corner_alpha)
        cube_corners.append(temp_corner_beta)

        # This only gets 6 out of 12 edges.
        corners(corner_01, temp_corner_alpha)
        corners(corner_02, temp_corner_beta)

    # From one corner, use each of the three adjacent corners as a reference point.
    # Find the edges connected to each corner.
    adjacent_corners = [cube_corners[2*k] for k in range(1,4)]

    # Take the index of the corner and then also ignore the indexed coord.
    # Run a check if the coord has the same index as the corner.
    for idx in range(len(adjacent_corners)):
        new_ref = adjacent_corners[idx]
        for j in range(len(new_ref)):
            if j != idx:
                new_corner = new_ref.copy()
                new_corner[j] = corner_02[j]
                corners(new_ref, new_corner)

    # For each value in the dict, check whether any of the values is greater than the grid dimensions.
    lwh_dim_array = np.array(lwh_dim)
    nofill_points = []

    def draw_point_on_grid(point):
        point_array = np.array(point)
        # Compare the point against the grid dimensions (baseline).
        draw_check = point_array - lwh_dim_array
        draw_max = np.max(draw_check)
        if draw_max <= 0:
            coords = []
            # Traverse the point coords.
            for idx in range(len(point)):
                # dim_labels[j][k], where j is the idx and k is the point coord.
                coords.append(dim_labels[idx][point[idx]])

            # Fill the point on the grid.
            # df[coords[0]][coords[2]][coords[1]] = 'X'
            df.loc[(coords[2], coords[1]), coords[0]] = 'X'

        # If the difference has any positive values, store the point in a list and don't fill.
        else:
            nofill_points.append(point)

    # First input all the corner points.
    for corner in cube_corners:
        draw_point_on_grid(corner)
    # Then input all the edge points.
    for point_pair in cube_edges:
        for edge_point in cube_edges[point_pair]:
            draw_point_on_grid(edge_point)

    return df
