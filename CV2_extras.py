#  cv2-extras - A Python library for higher level OpenCV functions used in image analysis and computer vision

# PyPi: https://pypi.org/project/cv2-extras/

# pip install cv2-extras


import cv2_extras as cv2x

"""
Functions:

    fill_holes(mask)
    filter_contours_by_size(mask, min_size=1024, max_size=None)
    find_border_contours(contours, img_h, img_w)
    fill_border_contour(contour, img_shape)

    find_border_by_mask(signal_mask,
        contour_mask, max_dilate_percentage=0.2, dilate_iterations=1)

    find_contour_union(contour_list, img_shape)

    generate_background_contours(hsv_img,
        non_bg_contours, remove_border_contours=True, plot=False)

    elongate_contour(contour, img_shape, extend_length)
    calculate_nonuniform_field(single_channel)
    correct_nonuniformity(single_channel, mask=None)
    color_transfer(ref_img, target_img, clip=True, preserve_paper=True)

"""

