#!/usr/bin/python3

# Assignment 02-01
#
# Task: Implement cylinder volume formula:
#
# Formula: V=pi*r*r*h, where
#
#          V - volume of cylinder
#          pi - pi math constant
#          r - radius of the circular base
#          h - height of cylinder

inp_txt = ["radius of the circular base =", "height of cylinder ="]
pi = 3.14
r = float(input(inp_txt[0]))
h = float(input(inp_txt[1]))
V = h*pi*r**2

print(
    f"""
    Volume of cylinder with radius 
    r={r}
    and height 
    h={h}
    V={V}
    """)
