import numpy as np

#############################################
#                                           #
#    ONLY NEED TO EDIT THIS FILE!           #
#                                           #
#############################################

gifs_parameters = {
    "num_iterations": 10,  # How many iterations of the (G - ) IFS?
    "num_nodes": 1,        # If =1 then regular IFS; if >1 then G-IFS.
    "polygon_order": 49,  # What is the order of the regular polygon the IFS is applied to the vertices of?
    # (Must be positive integer and should be at least 3 for interesting graphic.)

    "initial_angle": 0.0,  # do you want to rotate the starting polygon from the first vertex on the positive x-axis?
    "alpha": [np.pi / 1.3],  # list of any other parameters, can be empty

    # Now to define the functions that map between the nodes:
    "contractions": [
        {
            "edge": [0, 0],
            "function_x": lambda x, y, alpha: 0.7 * x + 0.8,
            "function_y": lambda x, y, alpha: 0.41 * y + 0.7 + 0.2 * np.cos(x * x),
        },
        {
            "edge": [0, 0],
            "function_x": lambda x, y, alpha: 0.61 * x + 2.8,
            "function_y": lambda x, y, alpha: 0.9 * y + 0.133,
        },
        {
            "edge": [0, 0],
            "function_x": lambda x, y, alpha: 0.83 * x + 0.1,
            "function_y": lambda x, y, alpha: 0.47 * np.abs(y)**0.4 - 1.2
        },
    ],
}
