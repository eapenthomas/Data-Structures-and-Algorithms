stack = []
def push_element():
    data = int(input("Enter the Data to be inserted :"))
    stack.append(data)
    print("Stack : ",stack)
def pop_element():
    if not stack:
        return print("Stack is empty !! ")
    data = stack.pop()
    print(data," is popped from the stack")
    print("Stack : ",stack)
def top():
    print("Stack peep : ",stack[-1])


while True:
    print("\n1. Push \n2. Pop\n3. Top \n4. Exit")
    choice = int(input("Enter the Choice : "))
    if choice ==1:
        push_element()
    elif choice ==2:
        pop_element()
    elif choice ==3:
        top()
    else:
        break