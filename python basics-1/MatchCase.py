#match case compare given variable to a pattern
X=int(input('ENter a num:'))
match X:
      case 0:
        print('X is Zero')
      case 4:
        print('X is Four')
      case _ if X!=10:
          print(X)
           

