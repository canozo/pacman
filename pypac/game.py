import pyglet
from pyglet import gl
from pyglet.math import Mat4

from pypac import gameobjects, services
from pypac.ai import GhostAI
from pypac.client import input
from pypac.components.controllers import NPC, Player

GRID_SIZE = 16


class Game(object):
    def __init__(self):
        self.game_objects = []
        self.game_objects_batch = pyglet.graphics.Batch()
        self.grid_size = GRID_SIZE
        self.factory = services.LameFactory(self)
        self.inputs = []
        self.level = None
        self.level_loader = services.LevelLoader(self)
        self.level_batch = pyglet.graphics.Batch()
        self.locator = services.LocatorService(self)
        self.players = []
        self.npcs = []
        self.window = None

    def on_draw(self):
        self.window.clear()
        self.level_batch.draw()
        self.game_objects_batch.draw()

    def on_key_press(self, symbol, modifiers):
        for input_ in self.inputs:
            input_.on_key_press(symbol, modifiers)

    def on_key_release(self, symbol, modifiers):
        for input_ in self.inputs:
            input_.on_key_release(symbol, modifiers)

    def update(self, dt):
        for player in self.players:
            player.update()

        for npc in self.npcs:
            npc.update()

        self._collide_objects()

    def _collide_objects(self):
        tuples = [(game_object, game_object.rectangle) for game_object in self.game_objects]
        for i in range(len(tuples) - 1):
            game_object, rectangle = tuples.pop(0)
            for other_object, other_rectangle in tuples:
                if rectangle.intersects(other_rectangle):
                    game_object.collide_with(other_object)
                    other_object.collide_with(game_object)

    def start(self):
        self._initialize_opengl()
        self._initialize_keyboard_players()
        self._initialize_joystick_players()
        self._initialize_ui()
        self._initialize_projection()
        self._start_level()
        # TODO: schedule interval is too short on windows but fine on macos?
        pyglet.clock.schedule_interval(self.update, 1 / 1000)
        pyglet.app.run()

    def _initialize_keyboard_players(self):
        # keyboard_1 = input.Keyboard(input.KeyboardMapping.default())
        # self.inputs.append(keyboard_1)
        keyboard_2 = input.Keyboard(input.KeyboardMapping.alternate())
        self.inputs.append(keyboard_2)

    def _initialize_ui(self):
        self.window = pyglet.window.Window(448, 496)
        self.window.event(self.on_draw)
        self.window.event(self.on_key_press)
        self.window.event(self.on_key_release)

    def _initialize_projection(self):
        # self.window.view = self.window.view.scale((1.5, -1.5, 0))
        self.window.projection = Mat4.orthogonal_projection(
            -300, 724, 650, -150, -1, 1
        )

    def _initialize_joystick_players(self):
        joysticks = pyglet.input.get_joysticks()
        for joystick in joysticks:
            joystick.open()
            joystick_mapping = input.JoystickMapping.default()
            joystick_input = input.Joystick(joystick, joystick_mapping)
            self.inputs.append(joystick_input)

    def _initialize_opengl(self):
        # Set antialiasing
        gl.glEnable(gl.GL_LINE_SMOOTH)
        gl.glEnable(gl.GL_POLYGON_SMOOTH)
        gl.glHint(gl.GL_LINE_SMOOTH_HINT, gl.GL_NICEST)

        # Set alpha blending
        gl.glEnable(gl.GL_BLEND)
        gl.glBlendFunc(gl.GL_SRC_ALPHA, gl.GL_ONE_MINUS_SRC_ALPHA)

        gl.glViewport(0, 0, 1024, 800)

    def _start_level(self):
        # TODO This is another object's responsability
        # TODO Maybe a game director?
        self.level = self.level_loader.load_level("level-1")
        ghost_classes = (gameobjects.GhostPink, gameobjects.GhostTeal, gameobjects.GhostRed, gameobjects.GhostPeach)
        for i, ghost_class in enumerate(ghost_classes):
            x = 32 * i if i % 2 == 0 else 464 - 32 * i
            ghost = ghost_class(self, x, 464)

            self.game_objects.append(ghost)
            self.npcs.append(NPC(ghost, GhostAI))

        for _input in self.inputs:
            pacman = gameobjects.Pacman(self, 16, 16)
            self.game_objects.append(pacman)
            self.players.append(Player(pacman, _input))
