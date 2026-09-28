# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    #adds value to the end of the queue
    def enqueue(self, value):
        new_node = Node(value) #initializes a new instance of the Node Class
        if not self.front: #if no items in the queue, the front and rear are set as this node
            self.front = new_node
            self.rear = new_node
        else: #if there are items in the queue, the rear is set to the new node and it points to the item that just was the rear
            self.rear.next = new_node
            self.rear = new_node
    #removes value from the queue (only the front)
    def dequeue(self):
        if not self.front: #since we only remove from the front, the removed node is always in the front pointer 
            return None
        removed_node = self.front
        self.front = self.front.next #if last node removed, the rear should be updated as well

        if not self.front:
            self.rear = None
        return removed_node.value
   
   #viewing the front value using peek but does NOT remove it
    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None
    #rinting the queue (starting from the front)  
    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is empty")
            return
        while current:
            print(f"- {current.value}")
            current = current.next #updates current to the next value


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name) #collecting the name and adds it to the queue
            
            print(f"{name} added to the queue.")
        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            customer = queue.dequeue()  

            if customer:
                print(f"{customer} has been helped.")
            else: print("No customers are waiting.")


        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            customer = queue.peek()

            if customer:
                print(f"Next customer: {customer}") #views the front without removing it
            else:
                print("No customers are waiting.")


        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()


