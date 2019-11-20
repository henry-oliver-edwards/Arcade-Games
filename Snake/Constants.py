# Constants for the game

# Colours in (R, G, B) Format
Black = (0, 0, 0)   # Background Colour
White = (255, 255, 255)
Red = (255, 0, 0)   # Cube Colour
Green = (0, 255, 0)   # Snake Body Colour
DarkerGreen = (5, 84, 19)   # Snake Head Colour

# Starting Resolution
DefaultResolution = (1280, 720)

# "Speed" the game runs at (time between game interactions/updates)
GameSpeed = 250

# Starting Size
StartingSize = 3

# Sneak segment width and height, based on resolution (default = 40, 40)
# Sneak gap between segments
SnakeWidth = DefaultResolution[0] / 128
SnakeHeight = DefaultResolution[1] / 72
SnakeGap = 5

# Score Size
ScoreSize = 50
