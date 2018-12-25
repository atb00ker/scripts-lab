def calculate:
    height = int(input("Enter the original height: "))
    width = int(input("Enter the original width: "))
    aspect = width/height
    print ("\nThe Orginal aspect ratio is ", aspect ,"\nThe Orginal size is",(width*height)/1000000)
    newheight = (99990000/aspect)**(1/2)
    newwidth =aspect*newheight
    print ("\nNew height will be", newheight)
    print ("New width will be", newwidth)
    print ("New size will be",(newheight*newwidth)/1000000)

if __name__ == '__main__':
    calculate()
