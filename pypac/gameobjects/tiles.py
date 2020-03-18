from pypac.client.graphics import tile_sheet
from pypac.gameobjects.base import GameObject
from pypac.gameobjects import listing


@listing.register
class WallSingle(GameObject):
    base_img = tile_sheet.get_region(3, 0)
    type_id = "wall_single"


@listing.register
class WallRowLeft(GameObject):
    base_img = tile_sheet.get_region(3, 1)
    type_id = "wall_row_left"


@listing.register
class WallRowMiddle(GameObject):
    base_img = tile_sheet.get_region(3, 2)
    type_id = "wall_row_middle"


@listing.register
class WallRowRight(GameObject):
    base_img = tile_sheet.get_region(3, 3)
    type_id = "wall_row_right"


@listing.register
class WallColTop(GameObject):
    base_img = tile_sheet.get_region(2, 0)
    type_id = "wall_col_top"


@listing.register
class WallColMiddle(GameObject):
    base_img = tile_sheet.get_region(1, 0)
    type_id = "wall_col_middle"


@listing.register
class WallColBottom(GameObject):
    base_img = tile_sheet.get_region(0, 0)
    type_id = "wall_col_bottom"


@listing.register
class WallTopLeft(GameObject):
    base_img = tile_sheet.get_region(0, 1)
    type_id = "wall_top_left"


@listing.register
class WallTopMiddle(GameObject):
    base_img = tile_sheet.get_region(0, 2)
    type_id = "wall_top_middle"


@listing.register
class WallTopRight(GameObject):
    base_img = tile_sheet.get_region(0, 3)
    type_id = "wall_top_right"


@listing.register
class WallCenterLeft(GameObject):
    base_img = tile_sheet.get_region(1, 1)
    type_id = "wall_center_left"


@listing.register
class WallCenterMiddle(GameObject):
    base_img = tile_sheet.get_region(1, 2)
    type_id = "wall_center_middle"


@listing.register
class WallCenterRight(GameObject):
    base_img = tile_sheet.get_region(1, 3)
    type_id = "wall_center_right"


@listing.register
class WallBottomLeft(GameObject):
    base_img = tile_sheet.get_region(2, 1)
    type_id = "wall_bottom_left"


@listing.register
class WallBottomMiddle(GameObject):
    base_img = tile_sheet.get_region(2, 2)
    type_id = "wall_bottom_middle"


@listing.register
class WallBottomRight(GameObject):
    base_img = tile_sheet.get_region(2, 3)
    type_id = "wall_bottom_right"