import turtle

def tree(branchLen,t):
    if branchLen > 1:
        t.forward(branchLen)
        print('rotating right')
        t.right(20)
        tree(branchLen-15,t)
        print('rotating left')
        t.left(40)
        tree(branchLen-15,t)
        print('rotating right again') 
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(80,t)
    myWin.exitonclick()

main()
