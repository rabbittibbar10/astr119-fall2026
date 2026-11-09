Spec: visualize_danger(n,R_new=3, saveas=...) in squarespare.py
This is a prompt problem. Write the whole visualize_danger function from my specification below; do not leave TODO blocks, and do not change product_remaining or product_visible. Radii are in units of the core radius: core edge r = 1, full roll r = R_new

Drawing:
-Roll seen end-on: concentric circles centered at (0,0), nothing else drawn
-Core: disc of radius 1 filled light grey ('0.8'), black outline
-n filled rings, each holding 1/n of the paper (not of the width), shown as unfilled blck circles (line width 1.5) on a white background
-boundary k (k=1...n) is a circle of radius product_visible(k/n, R_new)
-dont hard code anything, pass R_new through. Check (n=5, R_new = 3):1.612, 2.049, 2.408, 2.720, 3.000.

Axes
-keep black rectangle frame around plot, dont include ticks, tick labels or gridlines
-equal aspect ratio to make sure circles are round
-limits: set the limits so the whole roll fits with a small margin

Title
one line with font size 14 : "{n as a word} equal amounts of paper (core at one third of the radius)" for example : "five equal amounts of paper (core at one third of the radius)".
If R_new is not 3, replace 'one third' with 1/{R_new:g}
Dont add any other labels or annotations 

Expected Output:
8x6 inch figure on one axes saved to saveas. Keep the starters save/close code and the calls for n = 5,3,9

Make sure none of the following happens:
-evenly spaced radii. The outermost ring must be the thinnest
-oval circles
-any part of the roll cut off