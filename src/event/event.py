class Event:
    """
    entity:
        0 - some entity in tiling
        1 - map
        2 - game
    action for entity:
        0 - move left
        1 - move right
        2 - move up
        3 - move down
    action for map:
        0 - save map
        1 - load map
    option for the game:
        0 - new game
    indices - pair (x, y) if entity is some object in tiling
    """
    def __init__(self, entity, action):
        self.entity = entity
        self.action = action
        self.indices = None
