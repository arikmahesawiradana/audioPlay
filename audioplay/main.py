import setup

a = ['1.forward', '2.backward', '3.lost', '4.found', '5.kick']
print(a)
b = int(input("pilih: "))
if (b == 1):
    emp1 = setup.forward()
    emp1.play()
    print('go forward')
elif (b == 2):
    emp1 = setup.backward()
    emp1.play()
    print('go backward')
elif (b == 3):
    emp1 = setup.lost()
    emp1.play()
    print('I lost the ball')
elif (b == 4):
    emp1 = setup.found()
    emp1.play()
    print('I found a ball')
elif (b == 5):
    emp1 = setup.kick()
    emp1.play()
    print('kick to me')
else:
    print('no command')