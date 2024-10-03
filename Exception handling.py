try:
    print()
except NameError:
    print("Variable x is not defined")
except:
    print("sometimes else went wrong")
else:
    print("ok done")
finally:
    print("the exception is finished")

x = -1
if x < 0:
    raise Exception("sorry,no number below zero")
