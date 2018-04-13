import os
import tempfile
import logging

# external libs
import cv2

# my lib
import frames

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def write_frame(output_directory_path, frame, image_np):
    """
    :param output_directory_path: String of path to directory to write numpy array image to with filename
     "frame_%s.JPEG" where %s is frame passed as parameter. Path string can be relative or absolute.
    :param frame: int, frame number
    :param image_np: numpy array image to write to file
    """

    # if image output directory does not exist, create it
    if not os.path.exists(output_directory_path):
        logger.info("Creating output frames directory...")
        os.makedirs(output_directory_path)

    image_file_name = "%d.JPEG" % frame
    output_file = os.path.join(output_directory_path, image_file_name)

    logger.info("Writing Frame %d..." % frame)
    cv2.imwrite(output_file, image_np)  # BGR color


def create_animation(output_video_path, cycle_function):
    """
    :param output_video_path:
    :param cycle_function:
    :return: exit code
    """
    logger.info("Creating animation...")

    # temporary frames directory
    with tempfile.TemporaryDirectory() as frames_directory_path:
        logger.info("Created Temporary Frames Directory: %s" % frames_directory_path)
        frame = 1
        continue_animation = True
        while continue_animation:
            new_image, continue_animation = cycle_function(frame)
            write_frame(frames_directory_path, frame, new_image)
            frame += 1

        # convert frames directory to video
        logger.info("Converting animation to video...")
        frames.to_video(frames_directory_path, output_video_path)

    logger.info("Finished creating animation.")
    return 0
