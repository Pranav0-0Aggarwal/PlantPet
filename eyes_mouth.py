import pygame
from pygame.locals import *

class Eye:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        self.shape = "circle"

left_eye = Eye(40, (0, 0, 0))  # Red
right_eye = Eye(40, (0, 0, 0))  # Red

class Eyes:
    def __init__(self, distance):
        self.distance = distance

eyes = Eyes(60)

class Mouth:
    def __init__(self, image_path, position_offset):
        self.image_path = image_path
        self.position_offset = position_offset

mouth = Mouth("/Users/pranavaggarwal/Desktop/Screenshot 2023-05-29 at 6.18.23 PM.png", (-110,0))

def draw_eyes(squinted=False):
    pygame.init()

    display_width = 640
    display_height = 480

    display = pygame.display.set_mode((display_width, display_height))

    mouth_image = pygame.image.load(mouth.image_path)

    scaled_mouth = pygame.transform.scale(mouth_image, (left_eye.radius * 8, left_eye.radius * 4))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        display.fill((255, 255, 255))  # White

        mouse_pos = pygame.mouse.get_pos()

        disx = mouse_pos[0] - display_width / 2
        disy = mouse_pos[1] - display_height / 2

        scale_factor_x = 1 - abs(disx) / (display_width / 2)
        scale_factor_y = 1 - abs(disy) / (display_height / 2)

        new_radius_lx = int(left_eye.radius * scale_factor_x)
        new_radius_ly = int(left_eye.radius * scale_factor_y)

        new_radius_rx = int(right_eye.radius * scale_factor_x)
        new_radius_ry = int(right_eye.radius * scale_factor_y)

        eye_pos1 = (display_width // 2 - eyes.distance, display_height // 2)
        eye_pos2 = (display_width // 2 + eyes.distance, display_height // 2)

        pygame.draw.ellipse(display, left_eye.color,
                            (eye_pos1[0] - new_radius_lx, eye_pos1[1] - new_radius_ly,
                            new_radius_lx * 2, new_radius_ly * 2))


        pygame.draw.ellipse(display, right_eye.color,
                            (eye_pos2[0] - new_radius_rx, eye_pos2[1] - new_radius_ry,
                            new_radius_rx * 2, new_radius_ry * 2))
            

        mouth_position = (display_width // 2 + mouth.position_offset[0] - left_eye.radius, display_height // 2 + mouth.position_offset[1] + left_eye.radius)
        
        display.blit(scaled_mouth, mouth_position)
        
        pygame.display.flip()

    pygame.quit()

draw_eyes()
