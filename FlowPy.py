# FlowPy - Tools for working with optical flow
# Optical flow is the displacement map of pixels between two frames. It is a low-level analysis used in many computer vision programs.

# PyPi: https://pypi.org/project/flowpy/
# pip install flowpy

# Features
"""
The main features of flowpy are:

    Reading and writing optical flows in two formats:
        .flo (as defined here)
        .png (as defined here)
    Visualizing optical flows with matplotlib
    Backward and forward warp
"""

# Examples a simple RGB plot
"""
This is the simplest example of how to use flowpy, it:
Reads a file using flowpy.flow_read.
Transforms the flow as an rgb image with flowpy.flow_to_rgb and shows it with matplotlib
"""

import flowpy
import matplotlib.pyplot as plt

flow = flowpy.flow_read("tests/data/kitti_occ_000010_10.flo")

fig, ax = plt.subplots()
ax.imshow(flowpy.flow_to_rgb(flow))
plt.show()


# Plotting arrows, showing flow values and a calibration pattern

# Flowpy comes with more than just RGB plots, the main features here are: - Arrows to quickly visualize the flow - 
# The flow values below cursor showing in the tooltips - A calibration pattern side by side as a legend for your graph


flow = flowpy.flow_read("tests/data/Dimetrodon.flo")
height, width, _ = flow.shape

image_ratio = height / width
max_radius = flowpy.get_flow_max_radius(flow)

fig, (ax_1, ax_2) = plt.subplots(
    1, 2, gridspec_kw={"width_ratios": [1, image_ratio]}
)

ax_1.imshow(flowpy.flow_to_rgb(flow))
flowpy.attach_arrows(ax_1, flow)
flowpy.attach_coord(ax_1, flow)

flowpy.attach_calibration_pattern(ax_2, flow_max_radius=max_radius)

plt.show()


