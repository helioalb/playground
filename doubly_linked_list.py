
class Node:
  def __init__(self, key, previous = None, next = None):
    self.key = key
    self.previous = previous
    self.next = next

class DoublyLinkedList:
  def __init__(self):
    self.head = None

  def add(self, key):
    if self.head is None:
      self.head = Node(key)
    elif key < self.head.key:
      self.head.previous = Node(key, None, self.head)
      self.head = self.head.previous
    else:
      cursor = self.head
      while cursor.key < key and cursor.next is not None:
        cursor = cursor.next

      cursor.previous.next = cursor.previous = Node(key, cursor.previous, cursor)

  def show(self):
    cursor = self.head
    while cursor is not None:
      print(cursor.key)
      cursor = cursor.next


doubly_linked_list = DoublyLinkedList()

doubly_linked_list.add(5)
doubly_linked_list.add(4)
doubly_linked_list.add(2)
doubly_linked_list.add(3)
doubly_linked_list.add(5)

doubly_linked_list.show()

