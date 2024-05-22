# Code written by Chibuzor Emmanuel

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    # method to append a node at the end
    def append_node(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    # method to insert a node at the beginning
    def insert_node_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    # method to insert a node at a specific position
    def insert_node_at_position(self, data, position):
        new_node = Node(data)
        current = self.head
        
        for i in range(1, position -1 ):
            current = current.next if current else None

        if current:
            # Did this to avoid NoneType object has no attribute 'next': Linting Errors
            new_node.next = current.next
            current.next = new_node

    # universal insert method
    def insert_node(self, data, position=None):
        # if no position is given
        # or position exceeds the length of the list
        # insert at the end
        if position is None or position >= self.get_length():
            self.append_node(data)
        elif position == 0:
            self.insert_node_at_beginning(data)
        else:
            self.insert_node_at_position(data, position)
        
    # method to get the length of the linked list
    def get_length(self):
        current = self.head
        length = 0
        
        while current:
            length += 1
            current = current.next

        return length

    # traverse the list
    @property # this is a decorator REMEMBER!!
    def display(self):
        current = self.head

        while current:
            print(f'{current.data}', end=' -> ')
            current = current.next

        print(None)
    
    # method to concatenate two linked lists
    # self is the first linked list
    # list2 is the second list 
    def concatenate(self, list2):

        # handle if the first linked list is empty
        if not self.head:
            self.head = list2.head
            return
        
        current = self.head 

        # traverse the linked list
        while current.next:
            current = current.next
        
        # link the last node of list1 to
        # the first node of list2 
        current.next = list2.head
    
    def find_largest(self):
        # condition to handle empty linked list
        if not self.head:
            return None
        
        current = self.head
    
        # initialize the value of head as largest
        largest = current.data
    
        # iterate until the last node
        while current:
            # update largest if necessary
            if current.data > largest:
                largest = current.data

            current = current.next

        return largest

    # reverse linked list (simple)
    def reverse_elements(self):
        # new list to copy the values
        values = []
        current = self.head

        # copy values of linked list to the new list
        while current:
            values.append(current.data)
            current = current.next

        current = self.head

        # iterate through the new list in reverse order
        for value in reversed(values):
            # copy the reversed value to the original list
            if current:
                current.data = value
                current = current.next
    
    # reverse linked list (complex)
    def reverse_linked_list(self):
    
        prev_node = None
        current = self.head

        if current:
            next_node = current.next
    
        while True:
            if current:
                current.next = prev_node
                        
                prev_node = current
                current = next_node
                if next_node:
                    next_node = next_node.next
                    
            if next_node == None:
                if current:
                    current.next = prev_node
                    break
    
        self.head = current  


def main():
    # Couldn't cram everything up here
    # Break a leg!! 
    pass

if __name__ == '__main':
    main()