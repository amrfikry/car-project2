from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import  *

car_z = 0
z = .8*3
y = False

def myinit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60 , 1 , .1 , 50)
    gluLookAt(8,9,10,
              0,0,0,
              0,1,0)
    glClearColor(0,0.41176470588,0.58039215686,1)
    glClear(GL_COLOR_BUFFER_BIT)

def the_road():
    glColor3f(0.5, 0.5, 0.5)
    glScale(1.5,1,1)
    glBegin(GL_POLYGON)
    glVertex(5.5,5,-60)
    glVertex(3.5,0,20)
    glVertex(-3.5,0,20)
    glVertex(-15,5,-1500)
    glEnd()
    glLoadIdentity()
def grass():
    glColor3f(0.37647058823,0.50196078431,0.21960784313)
    glBegin(GL_POLYGON)
    glVertex(20 , 5 , -50)
    glVertex(-22 , 5 , -50)
    glVertex(-22 , 0 , 20)
    glVertex(20 , 0 , 20)
    glEnd()
def trees(x ,z):
    glColor3f(0.32549019607,0.19215686274,0.09411764705)
    glTranslate(x , 3 ,z)
    glScale(.1,.6,.1)
    glutSolidCube(6)
    glLoadIdentity()
    glColor3f(0,.7,0)
    glTranslate(x , 4.5 ,z)
    glutSolidSphere(1.5,15,15)
    glLoadIdentity()
def cubes(c , x , y ,z):
    glColor3f(c,c,c)
    glTranslate(x , y ,z)
    glScale(.4,.3,.8)
    glutSolidCube(3)
    glLoadIdentity()
def white_lines(z_line):
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    glVertex(.7,0 ,z_line )
    glVertex(-.7 ,0 , z_line)
    glVertex(-.7 ,0 ,z_line-3)
    glVertex(.7,0 ,z_line-3 )
    glEnd()
def arrowkey(key ,x,y):
    global car_z
    if key == GLUT_KEY_RIGHT:
        car_z += .5
    elif key == GLUT_KEY_LEFT:
        car_z -= .5
def draw_axies():
    glBegin(GL_LINES)
    glColor3f(0,0,1)
    glVertex(0 ,0,0)
    glVertex(0 ,0,10)
    glColor3f(0,1,0)
    glVertex(0 ,0,0)
    glVertex(0 ,10,0)
    glColor3f(1,0,0)
    glVertex(0 ,0,0)
    glVertex(10 ,0,0)
    glEnd()


angle = 0
move = 0
forward = True
moveBall = 0
forwardBall = True
def draw():
    global car_z
    global angle
    global move
    global forward
    global moveBall
    global forwardBall
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    grass()
    the_road()
    white_lines(12)
    white_lines(9)
    white_lines(3)
    white_lines(0)
    white_lines(-6)
    white_lines(-9)
    white_lines(-12)
    white_lines(-18)
    white_lines(-21)
    white_lines(-24)
    cubes(0 , 6.3 , 0 ,-z*4)
    cubes(1 , 6.3 , 0 ,-z*3)
    cubes(0 , 6.3 , 0 ,-z*2)
    cubes(1 , 6.3 , 0 ,-z)
    cubes(0 , 6.3 , 0 ,0)
    cubes(1 , 6.3 , 0 ,z)
    cubes(0 , 6.3 , 0 ,z*2)
    cubes(1 , 6.3 , 0 ,z*3)
####
    cubes(0 , -6.5 , 0 ,-z*21)
    cubes(1 , -6.5 , 0 ,-z*20)
    cubes(0 , -6.5 , 0 ,-z*19)
    cubes(1 , -6.5 , 0 ,-z*18)
    cubes(0 , -6.5 , 0 ,-z*17)
    cubes(1 , -6.5 , 0 ,-z*16)
    cubes(0 , -6.5 , 0 ,-z*15)
    cubes(1 , -6.5 , 0 ,-z*14)
    cubes(0 , -6.5 , 0 ,-z*13)
    cubes(1 , -6.5 , 0 ,-z*12)
    cubes(0 , -6.5 , 0 ,-z*11)
    cubes(1 , -6.5 , 0 ,-z*10)
    cubes(0 , -6.5 , 0 ,-z*9)
    cubes(1 , -6.5 , 0 ,-z*8)
    cubes( 0, -6.5 , 0 ,-z*7)
    cubes(1 , -6.5 , 0 ,-z*6)
    cubes(0 , -6.5 , 0 ,-z*5)
    cubes(1 , -6.5 , 0 ,-z*4)
    cubes(0 , -6.5 , 0 ,-z*3)
    cubes(1 , -6.5 , 0 ,-z*2)
    cubes(0, -6.5 , 0 ,-z*1)
    cubes(1 , -6.5 , 0 ,-z*0)
    cubes(0 , -6.5 , 0 ,z*1)
    cubes(1 , -6.5 , 0 ,z*2)
    cubes(0 , -6.5 , 0 ,z*3)
    glLoadIdentity()

    #theball
    glColor3f(1,0,0)
    glRotate(90,0,1,0)
    glTranslate(0 + moveBall -(.25*5),  0, 0)
    glutSolidSphere( .7, 10 , 10)
    glLoadIdentity()

    glColor3f(0,0,0)
    glRotate(90,0,1,0)
    glTranslate(2.5 - move , -2.5*.25 , 2.5*.5 +car_z)
    glRotate(-angle , 0 ,0 ,1)
    glutWireTorus(.2 , .7 , 50 , 50)
    glLoadIdentity()

    glColor3f(0,0,0)
    glRotate(90,0,1,0)
    glTranslate(-2.5 - move , -2.5*.25 , 2.5*.5 + car_z)
    glRotate(-angle , 0 ,0 ,1)
    glutWireTorus(.2 , .7 , 50 , 50)
    glLoadIdentity()

    glColor3f(0,0,0)
    glRotate(90,0,1,0)
    glTranslate(-2.5 - move , -2.5*.25 , -2.5*.5 + car_z)
    glRotate(-angle , 0 ,0 ,1)
    glutWireTorus(.2 , .7 , 50 , 50)
    glLoadIdentity()

    glColor3f(0,0,0)
    glRotate(90,0,1,0)
    glTranslate(2.5 - move , -2.5*.25 , -2.5*.5 + car_z)
    glRotate(-angle , 0 ,0 ,1)
    glutWireTorus(.2 , .7 , 50 , 50)
    glLoadIdentity()

    glColor3f(0,0,0.30196078431)
    glRotate(90,0,1,0)
    glTranslate(-move,0,car_z)
    glScale(1,.25,.5)
    glutSolidCube(5)
    glLoadIdentity()

    glColor3f(1,1,0)
    glRotate(90,0,1,0)
    glTranslate(-move-2.5,0,car_z+.7)
    glutSolidSphere(.3,10,10)
    glLoadIdentity()

    glColor3f(1,1,0)
    glRotate(90,0,1,0)
    glTranslate(-move-2.5,0,car_z-.7)
    glutSolidSphere(.3,10,10)
    glLoadIdentity()

    glColor3f(0,0,0.30196078431)
    glRotate(90,0,1,0)
    glTranslate(0 - move,  5*.25, car_z )
    glScale(.5 , .25 , .5)
    glutSolidCube(5)
    glLoadIdentity()

    glColor3f(1,1,1)
    glRotate(90,0,1,0)
    glTranslate(0 - move -(.25*5),  5*.25, car_z )
    glScale(0 , .25 , .5)
    glutSolidCube(5)
    glLoadIdentity()

    glColor3f(0,0,0)
    glRotate(90,0,1,0)
    glTranslate(0 - move -(.25*5),  5*.25, car_z )
    glScale(0 , .25 , .5)
    glutWireCube(5)
    glLoadIdentity()

    if forward:
        angle -= .1
        move += .009
        if move > 5.5:
            forward = False

    else:
        move -= .009
        angle += .1
        if move < -30:
            forward = True

    if forwardBall:
        moveBall += .03
        if moveBall > 35.5:
            forwardBall = False

    else:
        moveBall -= .03
        if moveBall < -8:
            forwardBall = True
    #draw_axies()
    trees(-6,0)
    trees(-6,-7)
    trees(-6,-14)
    trees(-6,-21)
    trees(-6,0)
    trees(-6,5)
    trees(7.5,5)
    trees(7.5,10)
    trees(7.5,5)
    glutSwapBuffers()
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutCreateWindow(b'test')
glutSpecialFunc(arrowkey)
glutDisplayFunc(draw)
glutIdleFunc(draw)
myinit()
glutMainLoop()