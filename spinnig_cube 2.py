# -*- coding: utf-8 -*-
"""Spinnig cube.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ClgMTJOeJ761oaJzq_GzQQ4O4CDi9fDu
"""

!pip install pygame

import cv2
from google.colab.patches import cv2_imshow
from google.colab import output
import time 
import os, sys

os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame
import numpy as np
from math import*
white,black  = (255,255,255),(0,0,0)
scale, angle, height, length = 80, 0, 400, 300
pygame.display.set_caption("cube")
screen = pygame.display.set_mode((height,length))
x_angle = radians(15)
circle_pos = [height/2,length/2]
points = []
clock = pygame.time.Clock()
Projection_Matrix = np.matrix([
    [1,0,0],
    [0,1,0],
    [0,0,0]
])

def connect_point(i, j, points):
    pygame.draw.line(screen,white,(points[i][0],points[i][1]),(points[j][0],points[j][1]))

points.append(np.matrix([-1,1,1]))
points.append(np.matrix([1,1,1]))
points.append(np.matrix([-1,-1,1]))
points.append(np.matrix([1,-1,1]))
points.append(np.matrix([-1,1,-1]))
points.append(np.matrix([1,1,-1]))
points.append(np.matrix([-1,-1,-1]))
points.append(np.matrix([1,-1,-1]))


while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    screen.fill(black)
    rotation_x = np.matrix([
        [1, 0, 0],
        [0, cos(x_angle), -sin(x_angle)],
        [0, sin(x_angle), cos(x_angle)],
    ])
    rotation_y = np.matrix([
        [cos(angle), 0, sin(angle)],
        [0, 1, 0],
        [-sin(angle), 0, cos(angle)],
    ])
    rotation_z = np.matrix([
        [cos(angle), -sin(angle), 0],
        [sin(angle), cos(angle), 0],
        [0, 0, 1],
    ])
    angle += 0.03
    i = 0
    xy_pos = []
    for point in points:
        Rotation_2d = np.dot(rotation_x, point.reshape((3,1)))
        Rotation_2d = np.dot(rotation_y, Rotation_2d)
        Rotation_2d = np.dot(rotation_z, Rotation_2d)
        Projection = np.dot(Projection_Matrix, Rotation_2d)
        
        x = int(Projection[0][0] * scale) + circle_pos[0]
        y = int(Projection[1][0] * scale) + circle_pos[1]
        pygame.draw.circle(screen,white,(x,y),2)
        xy_pos.append([x,y])
        i += 1
    connect_point(0, 1, xy_pos)
    connect_point(1, 3, xy_pos)
    connect_point(3, 2, xy_pos)
    connect_point(2, 0, xy_pos)

    connect_point(0, 4, xy_pos)
    connect_point(1, 5, xy_pos)
    connect_point(3, 7, xy_pos)
    connect_point(2, 6, xy_pos)

    connect_point(4, 5, xy_pos)
    connect_point(5, 7, xy_pos)
    connect_point(7, 6, xy_pos)
    connect_point(6, 4, xy_pos)       
    
    #source:https://colab.research.google.com/drive/1xtiBrGeRHmXY3KSOixkZBf_rJIgBImJu?usp=sharing#scrollTo=zaOtyAurJGDR
    view = pygame.surfarray.array3d(screen)
    view = view.transpose([1, 0, 2])
    img_bgr = cv2.cvtColor(view, cv2.COLOR_RGB2BGR)

    cv2_imshow(img_bgr)
    time.sleep(0.25)
    output.clear()

