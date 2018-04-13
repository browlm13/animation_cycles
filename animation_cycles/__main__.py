

# external libs
import numpy as np
import cv2

# my libs
from animation_cycles.utils import create_animation


def cycle_function(frame_number):

    # create blank image
    height, width = 400,400
    image_np = np.zeros((height,width,3), np.uint8)

    # ball start radius and center
    start_radius = 70
    center = (int(height/2), int(width/2))

    radius = int(start_radius * 1/frame_number*10)

    cv2.circle(image_np, center, radius, (255,0,0), thickness=2)

    continue_animation = True
    if frame_number > 100:
        continue_animation = False

    return image_np, continue_animation


# output video file
output_video_file = "test.mp4"

create_animation(output_video_file, cycle_function)
