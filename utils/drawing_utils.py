import cv2
import numpy as np
import mediapipe as mp
from PIL import Image, ImageFont, ImageDraw

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

class Draw():
    """ Helper class for drawing utilities """
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.font = ImageFont.truetype('../data/fonts/arial.ttf', self.height//24, encoding="unic")
        self.font = ImageFont.load_default()

    def bbox(self):
        """ Draw bbox """
        pass

    def skeleton(self, image, pose_results):
        """ Draw skeleton with pose landmarks """
        mp_drawing.draw_landmarks(
                    image,
                    pose_results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
        return image

    def pose_text(self, image, estimated_pose):
        """ Write text in image """
        pil_img = Image.fromarray(image)
        pil_draw = ImageDraw.Draw(pil_img)
        text_width, _ = pil_draw.textsize(estimated_pose.upper(), font=self.font)
        pil_draw.text(((self.width - text_width) / 2, self.height//16 + 20), estimated_pose.upper(),
                    (255, 255, 255), font=self.font)
        image = np.array(pil_img)
        return image

    def overlay(self, image):
        """ Draw overlay in image """
        alpha = 0.5
        overlay = image.copy()
        cv2.rectangle(overlay, (0, self.height//16), (self.width, self.height//8) , (25,25,25) , -1)
        image = cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0)
        return image

    def draw_line(self, image, coord1, coord2):
        """ Draw a line in image """
        cv2.line(image, coord1, coord2, thickness=4, color=(255, 255, 255))
        return image
