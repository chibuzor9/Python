class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # method to create a linked list
    def create_linked_list(self):

        # take input for node data
        data1 = int(input('Enter data for the first node: '))
        data2 = int(input('Enter data for the second node:'))
        data3 = int(input('Enter data for the third node:'))
        data4 = int(input('Enter data for the fourth node:'))

        # create 4 nodes with input values
        node1 = Node(data1)
        node2 = Node(data2)
        node3 = Node(data3)
        node4 = Node(data4)

        # set head field to the first node
        self.head = node1
        
        # link the nodes
        node1.next = node2
        node2.next = node3
        node3.next = node4

    # method to traverse and print the nodes
    def traverse_linked_list(self):
        current =  self.head

        while current:
            print(f'{current.data}', end=' -> ')
            current = current.next
        
        print('None')
        

linked_list = LinkedList()

# create a linked list
linked_list.create_linked_list()

# print the linked list
linked_list.traverse_linked_list()