# Copyright (c) [2024] [thireks GmbH]
# All rights reserved.

import pandas as pd

# load data from file
filename = "recorded_data_file.csv"
df = pd.read_csv(filename)

# Define the post-processing function
def post_processing(value):
    if value > 0:
        return (0.0019 * value * value) + 0.5031 * value
    elif value < 0:
        return -(0.0019 * value * value) + 0.5031 * value
    else:
        return 0

# Apply the function to the DataFrame column
df['steering_angle'] = df['potentiometer'].apply(post_processing)

# Plot Steering Angle
df.plot(x='timestamp', y='steering_angle')



