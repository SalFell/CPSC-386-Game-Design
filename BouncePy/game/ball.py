# Salvador Felipe
# CPSC 386-01
# 2022-04-25
# sfel@csu.fullerton.edu
# @SalFell
#
# Lab 05-00
#
# File that defines the Ball and Circle classes.
#


"""A Ball class for the bouncing ball demo."""

import os.path
from random import randint
from math import isclose
import pygame
from game import rgbcolors


def random_velocity(min_val=1, max_val=3):
    """Generate a random velocity in a plane, return it as a Vector2"""
    # TODO
    rand_x = randint(min_val, max_val)
    rand_y = randint(min_val, max_val)
    if randint(0, 1):
        rand_x *= -1
    if randint(0, 1):
        rand_y *= -1

    return pygame.Vector2(rand_x, rand_y)


def random_color():
    """Return a random color."""
    return pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))


# This is the class we discussed in class. You can have this as a standalone
# definition of a circle's geometry or you can fold the Circle and Ball classes
# together into a single class definition. Your choice.
class Circle:
    """Class representing a circle with a bounding rect."""

    def __init__(self, center_x, center_y, radius):
        # TODO
        self._center = pygame.Vector2(center_x, center_y)
        self._radius = radius

    @property
    def radius(self):
        """Return the circle's radius"""
        # TODO
        return self._radius

    @property
    def center(self):
        """Return the circle's center."""
        # TODO
        return self._center

    @property
    def rect(self):
        """Return bounding Rect; calculate it and create a new Rect instance"""
        # TODO
        upper_left_x = self._center[0] - self._radius
        upper_left_y = self._center[1] - self._radius
        return pygame.Rect(upper_left_x, upper_left_y, self.width, self.height)

    @property
    def width(self):
        """Return the width of the bounding box the circle is in."""
        # TODO
        return 2 * self._radius

    @property
    def height(self):
        """Return the height of the bounding box the circle is in."""
        # TODO
        return 2 * self._radius

    def squared_distance_from(self, other_circle):
        """Squared distance from self to other circle."""
        # TODO
        # (head - tail). length
        return (other_circle._center - self._center).length_squared()

    def distance_from(self, other_circle):
        """Distance from self to other circle"""
        # TODO
        # (head - tail). length
        return (other_circle._center - self._center).length()

    def move_ip(self, x, y):
        """Move circle in place, update the circle's center"""
        # TODO
        self._center = self._center + pygame.Vector2(x, y)

    def move(self, x, y):
        """Move circle, return a new Circle instance"""
        # TODO
        new_center = self._center + pygame.Vector2(x, y)
        return Circle(new_center[0], new_center[1], self._radius)

    def stay_in_bounds(self, xmin, xmax, ymin, ymax):
        """Update the position of the circle so that it remains within the
        rectangle defined by xmin, xmax, ymin, ymax."""
        # TODO
        print(f'stay_in_bounds is called')
        if self.center.x + self.radius >= xmax:
            print('Right side hit.')
            self.center.x = xmax - self.radius
        if self.center.x - self.radius <= xmin:
            print('Left side hit.')
            self.center.x = xmin + self.radius
        if self.center.y + self.radius >= ymax:
            print('Bottom hit.')
            self.center.y = ymax - self.radius
        if (self.center.y - self.radius) <= ymin:
            print('Top hit.')
            self.center.y = ymin + self.radius


class Ball:
    """A class representing a moving ball."""

    default_radius = 25

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, 'data')
    # Feel free to change the sounds to something else.
    # Make sure you have permssion to use the sound effect file and document
    # where you retrieved this file, who is the author, and the terms of
    # the license.
    bounce_sound = os.path.join(data_dir, 'Boing.aiff')
    reflect_sound = os.path.join(data_dir, 'Monkey.aiff')

    def __init__(self, name, center_x, center_y, sound_on=True):
        """Initialize a bouncing ball."""
        # The name can be any string. The best choice is an integer.
        self._name = name
        # Yes, we could define the details about our geometry in the Ball
        # class or we can define the geometry in an instance variable.
        # It is up to you if you want to separate them out or integrate them
        # together.
        self._circle = Circle(center_x, center_y, Ball.default_radius)
        self._color = random_color()
        self._velocity = random_velocity()
        self._sound_on = sound_on
        self._bounce_count = randint(5, 10)
        self._is_alive = True
        self._draw_text = False
        font = pygame.font.SysFont(None, Ball.default_radius)
        self._name_text = font.render(str(self._name), True, rgbcolors.BLACK)
        try:
            self._bounce_sound = pygame.mixer.Sound(Ball.bounce_sound)
            self._bounce_channel = pygame.mixer.Channel(2)
        except pygame.error as pygame_error:
            print(f'Cannot open {Ball.bounce_sound}')
            raise SystemExit(1) from pygame_error
        try:
            self._reflect_sound = pygame.mixer.Sound(Ball.reflect_sound)
            self._reflect_channel = pygame.mixer.Channel(3)
        except pygame.error as pygame_error:
            print(f'Cannot open {Ball.reflect_sound}')
            raise SystemExit(1) from pygame_error

    def toggle_draw_text(self):
        """Toggle the debugging text where each circle's name is drawn."""
        self._draw_text = not self._draw_text

    def draw(self, surface):
        """Draw the circle to the surface."""
        pygame.draw.circle(surface, self.color, self.center, self.radius)
        if self._draw_text:
            surface.blit(
                self._name_text,
                self._name_text.get_rect(center=self._circle.center),
            )

    def wall_reflect(self, xmin, xmax, ymin, ymax):
        """Reflect the ball off of a wall, play a sound if the sound flag is on."""
        # TODO
        # if overlapping, move ball so its not overlapping, then bounce
        print(f'wall_reflect is called')
        if (
            self.center.x + self.radius >= xmax
            or (self.center.x - self.radius) <= xmin
        ):
            print('Sides hit.')
            self._velocity.x = self._velocity.x * -1
            Ball.reflect_sound
        if (
            self.center.y + self.radius >= ymax
            or (self.center.y - self.radius) <= ymin
        ):
            print('Top or bottom hit.')
            self._velocity.y = self._velocity.y * -1
            Ball.reflect_sound

    def bounce(self, other_ball):
        """Bounce the ball off of another ball, play a sound if the ball is not alive."""
        # TODO
        # if overlapping, move ball so its not overlapping, then bounce
        if self.is_alive:
            self._bounce_count -= 1
            other_ball._bounce_count -= 1
        if self._bounce_count <= 0:
            self._is_alive = False
        if other_ball._bounce_count <= 0:
            other_ball._is_alive = False
        norm = self.circle.center - other_ball._circle.center
        self._velocity = self._velocity.reflect(norm)
        Ball.bounce_sound

    def collide_with(self, other_ball):
        """Return true if self collides with other_ball."""
        # TODO
        dist = self._circle.distance_from(other_ball.circle)
        return dist <= (self.radius + other_ball.radius)

    def separate_from(self, other_ball):
        """Separate a ball from the other ball so they are no longer overlapping."""
        # TODO
        # Remember alive balls must have velocity vectors of length > 0
        # and non alive balls must have velocity vectors of length == 0
        # separation = 2r - d
        distance_between_centers = self._circle.distance_from(
            other_ball._circle
        )
        ideal_dist = self.radius + other_ball.radius
        move_dist = ideal_dist - distance_between_centers
        half_dist = move_dist / 2
        if not other_ball.is_alive or not self.is_alive:
            factor = 2
        else:
            factor = 1

        velocity = -self.velocity
        scaled_vel = velocity * half_dist * factor
        self._circle.move_ip(*scaled_vel)

        velocity = -other_ball.velocity
        scaled_vel = velocity * half_dist * factor
        other_ball._circle.move_ip(*scaled_vel)

        # need some more code for when other_ball is dead

    @property
    def name(self):
        """Return the ball's name."""
        # TODO
        return self._name

    @property
    def rect(self):
        """Return the ball's rect."""
        # TODO
        return self._circle.rect

    @property
    def circle(self):
        """Return the ball's circle."""
        # TODO
        return self._circle

    @property
    def center(self):
        """Return the ball's center."""
        # TODO
        return self._circle.center

    @property
    def radius(self):
        """Return the ball's radius"""
        # TODO
        return self._circle.radius

    @property
    def color(self):
        """Return the color of the ball."""
        # TODO
        return self._color

    @property
    def velocity(self):
        # TODO
        return self._velocity

    @property
    def is_alive(self):
        """Return true if the ball is still alive."""
        # TODO
        if self._is_alive:
            return True

    def toggle_sound(self):
        """Turn off the sound effects."""
        # TODO
        if self._bounce_sound and pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()
        else:
            if self._bounce_sound:
                try:
                    pygame.mixer.music.load(self._bounce_sound)
                except pygame.error as pygame_error:
                    print('Cannot open the mixer?')
                    raise SystemExit('broken!!') from pygame_error
                pygame.mixer.music.play(-1)

        if self._reflect_sound and pygame.mixer.music.get_busy():
            pygame.mixer.music.fadeout(500)
            pygame.mixer.music.stop()
        else:
            if self._reflect_sound:
                try:
                    pygame.mixer.music.load(self._reflect_sound)
                except pygame.error as pygame_error:
                    print('Cannot open the mixer?')
                    raise SystemExit('broken!!') from pygame_error
                pygame.mixer.music.play(-1)

    def too_close(self, x, y, min_dist):
        """Is the ball too close to some point by some min_dist?"""
        # TODO
        return math.isclose(x, y, min_dist)

    def stop(self):
        """Stop the ball from moving."""
        # TODO
        self._velocity = pygame.Vector2(0, 0)

    def set_velocity(self, x, y):
        """Set the ball's velocity."""
        # TODO
        self._velocity = pygame.Vector2(x, y)

    def update(self):
        """Update the ball's position"""
        # TODO
        self._circle.move_ip(*self._velocity)
        print(str(self))

    def __str__(self):
        """Ball stringify."""
        # TODO
        return f'Ball(name = {self.name}, center = {self.circle.center},\
          color = {self._color}, velocity = {self._velocity}, is_alive = {self._is_alive}'
