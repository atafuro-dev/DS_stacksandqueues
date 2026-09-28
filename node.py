# Implement your Node class here
class Node:
    def __init__(self, value): 
        self.value = value #has a value
        self.next = None #pointer to the next node



#Design Memo:
#Why is a stack the right choice for undo/redo
#   A stack is the right choice for undo/redo as it can easily track actions from the top node. Whether you choose to undo/redo an action,
#   the code can easily grab it from the top node. If there were a distinct order, or if you had to specificy the front or rear like a queue, I feel as if it
#   could complicate the commands. In that case, a queue would probably be more helpful, or a linked list if it were involved position changes/references.
#Why is a queue better suited for the help desk?
#   A queue is better suited for the help desk as it can accurately track a line of waiting customers/tasks. If you are tracking what/who is next, or who just joined or is currently waiting,
#   a queue easily keeps track. It relies on the front and rear nodes, and allows you to work through the queue in an order that aligns with the purpose of a help desk waiting list.
#How do your implementations differ from Python’s built-in lists?
#   These implementations different from Pythons's built-in lists as there is not necessarily an inedexed order, but rather a way to go about addressing the 'list' and having it naturally move through values.
#   Python lists follow the order they are inserted in, and while you can add, remove, or modify the values the lists are not necessarily structured in a way where they can be queries to naturally move through or alter values.
#   Using queues and stacks allows us to define an action, and call it to guide values through the process they are built in, edit them, and automatically update what is remaining. Queues and stacks can also be tailored to specific 
#   situations, just like our help desk scenario, where it almost seems as if the type of structure was made for the situation. I feel as if these implementaions take a python built-in list to a new level. In my mind, the built in python lists are the
#   basic edition, and the implementations written this week are the advanced/specific versions.
