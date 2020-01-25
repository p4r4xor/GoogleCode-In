from manimlib.imports import *
import numpy as np
import itertools as it
from copy import deepcopy
import sys
from manimlib.constants import *
from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Polygon
from manimlib.once_useful_constructs.region import  region_from_polygon_vertices, region_from_line_boundary

A_COLOR = GREEN_D
B_COLOR = BLUE
C_COLOR = RED_D
TRI_COLOR = PURPLE_A
COLOR = [GREEN_D, BLUE, RED_D]
SCALE = 2/5
SHIFT_UP = -1
SHIFT_RIGHT = 0
CIRCLE_COLOR = WHITE
SIZE = 1/4
TRANS_UP = -2.5
TRANS_RIGHT = 0

class GeometricSeries(Scene):
	def construct(self):
		gci = TextMobject("Animate math using manim - Fedora Project")
		gci_me = TextMobject("Made by paraxor :)")
		text = TextMobject("Infinite Geometric Series")
		gci.shift(1.5*UP)
		gci_me.shift(0.5*DOWN)
		text.shift(2.5*UP)
		gci.scale(1)
		text.scale(1)
		gci_me.scale(1)
		self.play(Write(text), run_time = 2)
		self.play(Write(gci), run_time = 2)
		self.play(Write(gci_me), run_time = 2)
		self.play(FadeOutAndShift(gci, UP), run_time = 2)
		self.play(FadeOutAndShift(gci_me, UP), run_time = 2)
		self.wait()
		UNIT = 4
		RATIO = 2/3
		line = []
		power = []
		plus = []
		lengths = [TextMobject("$S$"), TextMobject("$1$"), TextMobject("$r$"), TextMobject("$1-r$"), TextMobject("$1$")]
		lengths[0].set_color(BLUE)
		lengths[1].set_color(BLUE)
		lengths[3].set_color(RED_D)
		lengths[4].set_color(RED_D)
		TICK_LENGTH = 0.1
		x = -UNIT/(2*(1-RATIO))
		y = -2.5
		LOW = 6
		NUM = 12
		COORD = np.array([
			[x, y, 0],
			[-x, y, 0],
			[x, y+UNIT, 0],
			[x+UNIT, y+UNIT*RATIO, 0],
			[x+UNIT, y+UNIT, 0],
			[x+UNIT, y, 0],
			[4, 2, 0],
			[1, 1, 0],
		])
		tick = [Line([x, y-TICK_LENGTH, 0], [x, y+TICK_LENGTH, 0])]
		power.append(TextMobject("$r^0$"))
		power.append(TextMobject("$r^1$"))
		power.append(TextMobject("$r^2$"))
		power.append(TextMobject("$r^3$"))
		power.append(TextMobject("$r^4$"))
		power.append(TextMobject("$r^5$"))
		lengths[0].move_to([0, y-0.5, 0])
		lengths[1].move_to([x-0.5, y+UNIT/2, 0])
		lengths[2].move_to([x+UNIT-0.5, y+UNIT*RATIO/2, 0])
		lengths[3].move_to([x+UNIT+1, y+UNIT*RATIO+UNIT*(1-RATIO)/2, 0])
		lengths[4].move_to([x+UNIT/2, y+UNIT+0.5, 0])
		for i in range(LOW, NUM):
			power.append(TextMobject("$.$"))
		self.play(FadeIn(tick[0]), run_time = 0.2)
		for i in range(NUM):
			line.append(Line([x, y, 0], [x+UNIT*(RATIO**i), y, 0]))
			power[i].move_to([x+UNIT*(RATIO**i)/2, y-0.5, 0])
			x += UNIT*(RATIO**i)
			tick.append(Line([x, y-TICK_LENGTH, 0], [x, y+TICK_LENGTH, 0]))
			plus.append(TextMobject("$+$").move_to([x, y-0.5, 0]))
			if i == 5:
				power[i].shift(0.1*RIGHT)
			if i < 3:
				self.play(
					ShowCreation(line[i]),
					FadeInFrom(power[i], LEFT),
					FadeIn(tick[i+1]),
				)
			elif i < LOW:
				self.play(
					ShowCreation(line[i]),
					FadeInFrom(power[i], LEFT),
					FadeIn(tick[i+1]),
					run_time = 0.75,
				)
			else:
				self.play(
					ShowCreation(line[i]),
					FadeInFrom(power[i], LEFT),
					FadeIn(tick[i+1]),
					run_time = 0.5,
				)
		line.append(Line([x, y, 0], [UNIT/(2*(1-RATIO)), y, 0]))
		line.append(Line([-UNIT/(2*(1-RATIO)), y+UNIT, 0], [UNIT/(2*(1-RATIO)), y, 0]))
		square = Square().scale(UNIT/2).move_to([-UNIT/(2*(1-RATIO))+UNIT/2, y+UNIT/2, 0]).rotate(PI/2)
		triangle = Polygon(*COORD[[2, 0, 1]], color = BLUE, fill_color = BLUE, fill_opacity = 0.5)
		updatedtriangle = Polygon(*COORD[[3, 5, 1]], color = RED_D, fill_color = RED_D, fill_opacity = 0.5)
		equals = TextMobject("$=$").move_to(COORD[6])
		frac_L = Line(COORD[6]+1.5*LEFT, COORD[6]+0.5*LEFT)
		frac_R = Line(COORD[6]+1.5*RIGHT, COORD[6]+0.5*RIGHT)
		self.play(ShowCreation(square), run_time = 2)
		self.play(ShowCreation(line[NUM+1]), run_time = 2)
		self.play(ShowCreation(line[NUM]), run_time = 0.2)
		for i in range(LOW-1):
			self.play(FadeIn(plus[i]), run_time = 0.5)
		self.play(
			FadeInFrom(lengths[1], LEFT),
			FadeInFrom(lengths[4], DOWN),
			FadeOutAndShift(text, UP),
			run_time = 2,
		)
		self.play(
			ShowCreation(triangle),
			run_time = 2,
		)
		self.play(
			triangle.scale, RATIO,
			triangle.shift, UNIT/2*RIGHT+UNIT*(1-RATIO)/2*DOWN,
			FadeInFrom(lengths[2], LEFT),
			run_time = 2,
		)
		self.play(
			FadeInFrom(lengths[3], RIGHT),
			run_time = 1.5,
		)
		self.play(
			GrowFromCenter(updatedtriangle),
			run_time = 1.5,
		)
		self.play(
			updatedtriangle.scale, (1-RATIO)/RATIO,
			updatedtriangle.shift, UNIT/2*LEFT+UNIT*(RATIO-1/2)*UP,
			run_time = 1,
		)
		self.play(
			Rotating(updatedtriangle, radians = -PI, about_point = COORD[3], rate_func = smooth, run_time = 3),
			run_time = 2,
		)
		self.play(
			triangle.scale, 1/RATIO,
			triangle.shift, UNIT/2*LEFT+UNIT*(1-RATIO)/2*UP,
			run_time = 2,
		)
		self.play(
			FadeIn(lengths[0]),
			FadeOutAndShift(power[0], RIGHT),
			FadeOutAndShift(power[1], RIGHT),
			FadeOutAndShift(power[2], RIGHT),
			FadeOutAndShift(power[3], LEFT),
			FadeOutAndShift(power[4], LEFT),
			FadeOutAndShift(power[5], LEFT),
			FadeOutAndShift(power[6], LEFT),
			FadeOutAndShift(power[7], LEFT),
			FadeOutAndShift(power[8], LEFT),
			FadeOutAndShift(power[9], LEFT),
			FadeOutAndShift(power[10], LEFT),
			FadeOutAndShift(power[11], LEFT),
			FadeOutAndShift(plus[0], RIGHT),
			FadeOutAndShift(plus[1], LEFT),
			FadeOutAndShift(plus[2], LEFT),
			FadeOutAndShift(plus[3], LEFT),
			FadeOutAndShift(plus[4], LEFT),
			run_time = 2,
		)
		self.play(
			FadeIn(equals),
			FadeIn(frac_L),
			lengths[0].move_to, COORD[6]+0.35*UP+LEFT,
			lengths[1].move_to, COORD[6]+0.35*DOWN+LEFT,
			run_time = 3,
		)
		self.play(
			FadeIn(frac_R),
			lengths[4].move_to, COORD[6]+0.35*UP+RIGHT,
			lengths[3].move_to, COORD[6]+0.35*DOWN+RIGHT,
			run_time = 3,
		)
		self.play(
			FadeOutAndShiftDown(lengths[1]),
			FadeOutAndShiftDown(frac_L),
			lengths[0].move_to, COORD[6]+LEFT,
			run_time = 2,
		)
		self.play(
			equals.move_to, COORD[7],
			lengths[0].move_to, (COORD[7]+LEFT),
			lengths[4].move_to, (COORD[7]+0.7*UP+2*RIGHT),
			frac_R.move_to, (COORD[7]+2*RIGHT),
			lengths[3].move_to, (COORD[7]+0.7*DOWN+2*RIGHT),
			run_time = 3,
		)
		self.play(
			equals.scale, 2,
			lengths[0].scale, 2,
			lengths[4].scale, 2,
			frac_R.scale, 2,
			lengths[3].scale, 2,
		)
		self.wait(2)

