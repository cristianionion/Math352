import matplotlib.pyplot as plt

# https://cubic-bezier.com/ helped with visualizing the function

# bezier idea from https://javascript.info/bezier-curve
# helped with cubicbeziercurve function

# cubicbeziercurve takes in t to calculate curve from the first point to the last one
# cubicbeziercurve also takes in 8 values that create the 4 control points

def cubicbeziercurve(t,x1,y1,x2,y2,x3,y3,x4,y4):

    # calculates first coordinate point's impact
    p1x = pow((1-t),3) * x1
    p1y = pow((1-t),3) * y1

    # calculates second coordinate point's impact
    p2x = 3*pow((1-t),2)*t*x2
    p2y = 3*pow((1-t),2)*t*y2
    
    # calculated third coordinate point's impact
    p3x = 3*(1-t)*pow(t,2)*x3
    p3y = 3*(1-t)*pow(t,2)*y3

    # calculates fourth coordinate point's impact
    p4x = pow(t,3)*x4
    p4y = pow(t,3)*y4

    # this is the final coordinates for a point at time t 
    coordinates = (p1x +p2x +p3x +p4x, p1y +p2y +p3y +p4y)

    # returns the point
    return coordinates


# t stores an interval [0, 0.02, 0.04,....., 0.98, 1]
t = []
for i in range(51):
    x = i/50
    t.append(x)




print("Enter 1 for premade curves or 2 for manual entry")
# gives option of looking at a few curves I hardcoded or a new curve made by the user
choice = int(input())

if choice == 2:
    # instructions for standard input to create the 4 control points
    print("Enter 8 coordinate points like: ")
    print("x1")
    print("y1")
    print("x2")
    print("y2")
    print("...")
    print("...")
    print("...")
    print("y4")


    # creates the 4 control points
    points = []
    for i in range(8):
        p = input()
        p = float(p)
        points.append(p)

    # empty lists to store coordinates from cubicbeziercurve
    x = []
    y = []

    # runs cubicbeziercurve with respect to t for all elements in t
    for i in range(len(t)):
        p = cubicbeziercurve(t[i],points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7])
        x.append(p[0])
        y.append(p[1])
    # plots curve
    plt.plot(x,y)


# hardcoded curves
elif choice == 1:
    points = [0,0,0.1,0.9,0.6,0.2,1,1]
    points1 = [1,0.3,0.3,0.1,0.2,0.9, 0,0.2]
    points2 = [0.5,0,0.1,1,0.7,0.2,0.3,0.1]
    x = []
    y = []

    # calculates curves for the three sets of control points and plots them
    for i in range(len(t)):
        p = cubicbeziercurve(t[i],points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7])
        x.append(p[0])
        y.append(p[1])
    plt.plot(x,y)
    x2 = []
    y2 = []

    for i in range(len(t)):
        p = cubicbeziercurve(t[i],points1[0],points1[1],points1[2],points1[3],points1[4],points1[5],points1[6],points1[7])
        x2.append(p[0])
        y2.append(p[1])
    plt.plot(x2,y2)
    x3 = []
    y3 = []

    for i in range(len(t)):
        p = cubicbeziercurve(t[i],points2[0],points2[1],points2[2],points2[3],points2[4],points2[5],points2[6],points2[7])
        x3.append(p[0])
        y3.append(p[1])   
    plt.plot(x3,y3)
    plt.legend(['[0,0],[0.1,0.9],[0.6,0.2],[1,1]', '[1,0.3],[0.3,0.1],[0.2,0.9],[0,0.2]',
     '[0.5,0],[0.1,1],[0.7,0.2],[0.3,0.1]'], loc='upper left')


# show results!
plt.show()