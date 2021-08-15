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


