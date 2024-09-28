# Linked list operations
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_after_node(prev_node, data):
    if not prev_node:
        print("The given previous node must be in the LinkedList.")
        return
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return True
            current = current.next

        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


linked_list = LinkedList()

linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_beginning(5)
linked_list.insert_at_end(30)

print("Linked List:", linked_list.display())

insert_after_node(linked_list.head.next, 15)
print("Linked List after inserting 15 after 10:", linked_list.display())

linked_list.delete_node(20)
print("Linked List after deleting 20:", linked_list.display())

print("Is 15 in the list?", linked_list.search(15))
print("Is 100 in the list?", linked_list.search(100))
