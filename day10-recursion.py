def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mult(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": mult, "/": div}

def calculator():
  num1 = float(input("What is the first number?: "))
  continue_flag = "y"
  while (continue_flag == "y"):
      for key in operations:
          print(key)
      operation = input("Pick an operation from above : ")
      num2 = float(input("What is the next number?: "))
      answer = operations[operation](num1, num2)
      print(f"{answer} {operation} {num2} = {answer}")
      continue_flag = input(
          f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or 'exit' to exit the program.: "
      )
      if(continue_flag == "y"):
        num1 = answer
      elif(continue_flag == "n"):
        calculator()
      else:
        return

calculator()
    
