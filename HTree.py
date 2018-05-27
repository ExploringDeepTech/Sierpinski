from drawingpanel import *
panel = DrawingPanel(500,500)
canvas = panel.canvas

def draw_htree(n):
	'''n denotes the recursion depth'''
	draw_htree_rec_helper(n, 200, 250, 250)

def drawH(size, centerx, centery):
	canvas.create_line(centerx - size/2, centery - size/2, centerx - size/2, centery + size/2)
	canvas.create_line(centerx + size/2, centery - size/2, centerx + size/2, centery + size/2)
	canvas.create_line(centerx - size/2, centery, centerx + size/2, centery)

def draw_htree_rec_helper(n, size, centerx, centery):
	'''draw an htree centered at centerx, centery of height = width = size'''
	if n == 1:
		drawH(size, centerx, centery)
		return
	drawH(size, centerx, centery)
	draw_htree_rec_helper(n - 1, size / 2, centerx - size/2, centery - size/2)
	draw_htree_rec_helper(n - 1, size / 2, centerx + size/2, centery - size/2)
	draw_htree_rec_helper(n - 1, size / 2, centerx + size/2, centery + size/2)
	draw_htree_rec_helper(n - 1, size / 2, centerx - size/2, centery + size/2)

def main():
	draw_htree(4)

main()