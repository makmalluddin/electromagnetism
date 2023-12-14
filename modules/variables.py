import pygame
import os

pygame.init()

# Sprite addresses
(dirname, prom) = os.path.split(os.path.dirname(__file__))
magnet_address = dirname + '\\resources\\magnet.png'
icon_address = dirname + '\\resources\\icon.png'

# Sprites
sp_magnet = pygame.image.load(magnet_address)
icon = pygame.image.load(icon_address)

# Window variables
wind_width = 1200
wind_height = 800

simWindow = pygame.display.set_mode((wind_width, wind_height))
pygame.display.set_caption('KELOMPOK 2: SIMULASI ELEKTROMAGNETIK')
pygame.display.set_icon(icon)

# Color variables
background = (0, 0, 0)
magnetic_field_color = (97, 189, 194)
coil_color = (184, 115, 51)
# Lightbulb color will change during simulation
lightbulb_color = [35, 35, 0]

# Other variables
field_width = 330
field_height = 60
field_lines_thickness = 2
induction_min = 1
induction_max = 10

coil_width = 50
coil_height = 145
coil_min_height = 95
coil_max_height = 200
coil_spacing = 16
coil_thickness = 5
coil_min_num = 3
coil_max_num = 35
coil_line_lenght = 110

lightbulb_radius = 25

# Clock variable
clock = pygame.time.Clock()

# Text (author credits)
def write_author_name(simWindow):
    font = pygame.font.Font('freesansbold.ttf', 16)
    author_text = font.render('Kelompok 2: Pemkom 117', True, (255, 255, 255))
    author_text_rect = author_text.get_rect()
    author_text_rect.center = (wind_width * 0.9, wind_height * 0.95)

    simWindow.blit(author_text, author_text_rect)
