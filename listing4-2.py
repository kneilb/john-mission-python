import pgzrun, time, random, math

WIDTH = 800
HEIGHT = 800

PLAYER_NAME = "John"
FRIEND1_NAME = "Felix"
FRIEND2_NAME = "Indiana"
current_room = 31

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar, images.soil]

MAP_WIDTH = 5
MAP_HEIGHT = 10
MAP_SIZE = MAP_WIDTH * MAP_HEIGHT
GAME_MAP = [ ["Room 0 - where objects are kept", 0, 0, False, False] ]

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

##############
## DRAW MAP ##
##############

def get_floor_type():
    if current_room in outdoor_rooms:
        return 2
    else:
        return 0

def generate_map():
    global room_map, room_width, room_height, room_name, hazard_map
    global top_left_x, top_left_y, wall_transparency_frame
    room_data = GAME_MAP[current_room]
    room_name = room_data[0]
    room_height = room_data[1]
    room_width = room_data[2]

    floor_type = get_floor_type()
    if current_room in range(1, 21):
        bottom_edge = 2
        side_edge = 2
    if current_room in range(21, 26):
        bottom_edge = 1
        side_edge = 2
    if current_room > 25:
        bottom_edge = 1
        side_edge = 1

    room_map = [[side_edge] * room_width]
    for y in range(room_height - 2):
        room_map.append([side_edge]
                        + [floor_type]*(room_width - 2) + [side_edge])
        middle_row = int(room_height / 2)
        middle_column = int(room_width / 2)

    if room_data[4]:
        room_map[middle_row][room_width - 1] = floor_type
        room_map[middle_row+1][room_width - 1] = floor_type
        room_map[middle_row-1][room_width - 1] = floor_type

    if current_room % MAP_WIDTH != 1:
        room_to_left = GAME_MAP[current_room - 1]
        if room_to_left[4]:
            room_map[middle_row][0] = floor_type
            room_map[middle_row + 1][0] = floor_type
            room_map[middle_row - 1][0] = floor_type
    
    if room_data[3]:
        room_map[middle_row][0] = floor_type
        room_map[middle_row + 1][0] = floor_type
        room_map[middle_row - 1][0] = floor_type

    if current_room <= MAP_SIZE - MAP_WIDTH:
        room_below = GAME_MAP[current_room+MAP_WIDTH]
        if room_below[3]:
            room_map[room_height-1][middle_column] = floor_type
            room_map[room_height-1][middle_column + 1] = floor_type
            room_map[room_height-1][middle_column - 1] = floor_type

pgzrun.go()
