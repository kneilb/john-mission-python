import pgzrun, time, random, math

WIDTH = 800
HEIGHT = 800

PLAYER_NAME = "John"
FRIEND1_NAME = "Felix"
FRIEND2_NAME = "Indiana"

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT
GAME_MAP = [ ["Room 0 - where unused objects are kept", 0, 0, False, False] ]

outdoor_rooms = range(1, 26)
for planetsectors in range(1, 26):
    GAME_MAP.append( ["The dusty planet surface", 13, 13, True, True] )

###################
## THE MAP STUFF ##
###################

GAME_MAP += [
    ["The airlock", 13, 5, True, False],
    ["The engineering lab", 13, 13, False, False],
    ["Poodle mission control", 9, 13, False, True],
    ["The viewing gallery", 9, 15, False, False],
    ["The crew's bathroom", 5, 5, False, False],
    ["The airlock entry bay", 7, 11, True, True],
    ["Left elbow room", 9, 7, True, False],
    ["Right elbow room", 7, 13, True, True],
    ["The science lab", 13, 13, False, True],
    ["The greenhouse", 13, 13, True, False],
    [PLAYER_NAME + "'s sleeping quarters", 9, 11, False, False],
    ["West corridor", 15, 5, True, True],
    ["The briefing room", 7, 13, False, True],
    ["The crew's community room", 11, 13, True, False],
    ["Main mission control", 14, 14, False, False],
    ["The sick bay", 12, 7, True, False],
    ["West corridor", 9, 7, True, False],
    ["Utilities control room", 9, 9, False, True],
    ["Systems engineering bay", 9, 11, False, False],
    ["Security portal to mission control", 7, 7, True, False],
    [FRIEND1_NAME + "'s sleeping quarter", 9, 11, True, True],
    [FRIEND2_NAME + "'s sleeping quarter", 9, 11, True, True],
    ["The pipeworks", 13, 11, True, False],
    ["The chief scientist's office", 9, 7, True, True],
    ["The robot workshop", 9, 11, True, False]
]

assert len(GAME_MAP)-1 == MAP_SIZE, "YOU FOOL IT IS RUINED!!!"

pgzrun.go()