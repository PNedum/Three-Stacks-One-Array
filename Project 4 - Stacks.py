from tkinter import *
from tkinter import font
from tkinter import ttk
# We use OOP to implement the stack operations
class ThreeStacks:
    # We initialize a stack class of size n
    def __init__(self, n):
        # We set initial total number of elements in all the stacks to 0.
        # As we have not pushed in anything into the stack
        self.size = 0
        # Next we create an array of size n, with initial values of 0
        self.array = [0] * n
        # Next we create an array of top values that stores the current values of the different tops of the stacks.
        # We use size 4 as we intend to call the stack number from 1 instead of 0.
        self.top_stk = [-1] * 4
        # Next we create an array in an array of 4. Each of these arrays stores all the values of tops of the different
        # stacks when a push operations is done.
        self.top_list = [[0] for _ in range(4)]
        # Finally, we create another array that stores all the indexes of all the stack elements of each stack.
        self.arr = []

    # We define the push operation. It takes a value and the stack number and performs a push operation to that stack.
    def push(self, value, st):
        # This takes the initial index to be pushed into as zero.
        index = 0
        # This first checks if the stack is full by calling the isFull function
        # and returns the statement 'Stack is Full' if true.
        # If the stack is not full it proceeds to push the item into the stack.
        if self.isFull():
            return 'Stack is full'
        else:
            # This checks if the given index already has an element assigned to it. If it does it increments it by one.
            # The while loop ensures that the value is within the limit of the length of the array. If the index has not
            # been assigned, we break the loop.
            while index < (len(self.array) - 1):
                if index in self.arr:
                    index = self.size + 1
                else:
                    break
            # Next, we append the top of the given stack to the array that stores the tops of that stack.
            self.top_list[st].append(self.top_stk[st])
            # Next, we update the value of the top with the given index.
            self.top_stk[st] = index
            # We then assign the given value to that index in the stack array.
            self.array[index] = value
            # Next we increment the size of the overall stack by one.
            self.size = self.size + 1
            # Then we save that index to the array that contains all the instances of indexes that has been used.
            self.arr.append(index)

    # We define a pop function. This removes the top item of a given stack.
    def pop(self, st):
        # We first check if the stack is empty. If it is so, we print that the given stack is empty.
        # Else, we proceed to pop.
        if self.isEmpty(st):
            return "Stack " + str(st) + " is empty"
        else:
            # First we save the value of the given top of the stack we want to pop.
            value = self.array[self.top_stk[st]]
            # Next, we remove that top index to the array that contains all the instances of indexes that has been used.
            self.arr.remove(self.top_stk[st])
            # Next, we assign the last top stored in the top_list array as the new top.
            self.top_stk[st] = self.top_list[st][(len(self.top_list[st]) - 1)]
            # Next, we remove this new top value index from the top_list array.
            self.top_list[st] = self.top_list[st][:-1]
            # Next, we decrement the size of the stack.
            self.size = self.size - 1
            # We then return the value of the popped item to the console.
            return value

    # This function shows the top of a given stack
    def peek(self, st):
        # If the top of a given stack is -1, this returns that the stack is empty.
        # Else it returns the element of that array index as the output.
        if self.top_stk[st] == -1:
            return "Stack " + str(st) + " is empty"
        else:
            return self.array[self.top_stk[st]]

    # This checks if a given stack is empty by checking the value of the top of that stack. If -1, then stack is empty.
    def isEmpty(self, st):
        return self.top_stk[st] == -1

    # This checks if the stack is full by checking if the size of items pushed is equal to the length of the stack.
    def isFull(self):
        return self.size == len(self.array)



# This builds the GUI
if __name__ == '__main__':
    class app:
        def __init__(self, master):
            self.master = master
            self.master.geometry("1000x350")
            self.master.title("Three Stack Implementation")
            self.create_stack()

        # This function builds the stack UI
        def create_stack(self):
            for i in self.master.winfo_children():
                i.destroy()
            self.titleFont = font.Font(family=" Calibri ", size=14)
            self.title = Label(self.master, text="Three Stack Implementation", font=self.titleFont)
            self.title.pack(side=TOP)


            # This creates the first frame and buttons
            self.frame1 = Frame(self.master, width=300, height=300)
            self.frame1.pack()

            # This creates the about button
            self.about = ttk.Button(self.frame1, text="About", command=self.intro)
            self.about.pack()

            # This prompts the user to enter the length of array.
            self.prompt = Label(self.frame1, text='Enter length of array:')
            self.prompt.pack()

            # This receives input for the length
            self.txt_entry = Entry(self.frame1, bd=1)
            self.txt_entry.pack(side=TOP)

            # This button creates the stack.
            self.create_btn = ttk.Button(self.frame1, text="Create Stack", command=self.stack_ops)
            self.create_btn.pack()

            self.lbl = Label(self.frame1, text=" ")
            self.lbl.pack(side=TOP)


        # This function prints the application information.
        def intro(self):
            self.res = "This application allows you to implement three stacks in one array"
            print(self.res)
            self.lbl.configure(text=self.res, font=self.titleFont)

        # This function defines the push, pop and top function UIs.
        def stack_ops(self):
            # This tries to catch none integer values.
            try:
                self.stack_size = int(self.txt_entry.get())
            except:
                return
            # This destroys the initial interface
            for i in self.master.winfo_children():
                i.destroy()

            # This creates the stack.
            self.stack = ThreeStacks(self.stack_size)

            # This creates a new frame.
            self.frame2 = Frame(self.master, width=300, height=300)
            self.frame2.pack()
            self.title2 = Label(self.frame2, text='Stack Operations', font=self.titleFont)
            self.title2.pack()


            # This block of codes define the entry and buttons of the push function.
            self.push_prompt = Label(self.frame2, text='Enter value to push into stack:')
            self.push_prompt.pack()

            self.push_entry = Entry(self.frame2, bd=1)
            self.push_entry.pack(side=TOP)

            self.push_prompt2 = Label(self.frame2, text='Enter stack value is to be pushed into:')
            self.push_prompt2.pack()

            self.push_entry2 = Entry(self.frame2, bd=1)
            self.push_entry2.pack(side=TOP)

            self.push = ttk.Button(self.frame2, text="Push", command=self.stack_push)
            self.push.pack()


            # This block of codes define the entry and buttons of the pop function.
            self.pop_prompt1 = Label(self.frame2, text='Enter stack value is to be popped:')
            self.pop_prompt1.pack()

            self.pop_entry1 = Entry(self.frame2, bd=1)
            self.pop_entry1.pack(side=TOP)

            self.pop = ttk.Button(self.frame2, text="Pop", command=self.stack_pop)
            self.pop.pack()


            # This block of codes define the entry and buttons of the top function.
            self.top_prompt = Label(self.frame2, text='Enter stack value to view top item:')
            self.top_prompt.pack()

            self.top_entry = Entry(self.frame2, bd=1)
            self.top_entry.pack(side=TOP)

            self.top = ttk.Button(self.frame2, text="Top", command=self.stack_top)
            self.top.pack()


            # This is the exit button.
            self.exit_button = ttk.Button(self.frame2, text="Exit", width=20, command=exit)
            self.exit_button.pack(side=TOP)

            self.lbl2 = Label(self.frame2, text=" ")
            self.lbl2.pack(side=TOP)

        # This defines what happens when you press the push button. It pushes items to the stack.
        def stack_push(self):
            try:
                self.push_value = int(self.push_entry.get())
                self.stack_number = int(self.push_entry2.get())
            except:
                return
            # This catches exceptions if the number input is not within range of stacks.
            if self.stack_number not in range(1, 4):
                return print("Enter values of 1, 2 or 3")
            else:
                self.stack.push(self.push_value, self.stack_number)


        # This defines what happens when you press the pop button. It pops items to the stack.
        def stack_pop(self):
            try:
                self.stack_number = int(self.pop_entry1.get())
            except:
                return
            # This catches exceptions if the number input is not within range of stacks.
            if self.stack_number not in range(1, 4):
                self.res = "Enter values of 1, 2 or 3"
                print(self.res)
            else:
                self.res = self.stack.pop(self.stack_number)
                print(self.res)
            self.lbl2.configure(text=self.res, font=self.titleFont)


        # This defines what happens when you press the top button. It displays the top items in a stack.
        def stack_top(self):
            try:
                self.stack_number = int(self.top_entry.get())
            except:
                return
            # This catches exceptions if the number input is not within range of stacks.
            if self.stack_number not in range(1, 4):
                self.res = "Enter values of 1, 2 or 3"
                print(self.res)
            else:
                self.res = self.stack.peek(self.stack_number)
                print(self.res)
            self.lbl2.configure(text=self.res, font=self.titleFont)


    root = Tk()
    app(root)
    root.mainloop()
