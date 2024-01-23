
class Node:
  def __init__(self, key, previous = None, next = None):
    self.key = key
    self.previous = previous
    self.next = next

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add(self, key):
    if self.head is None:
      self.head = self.tail = Node(key)
    elif key < self.head.key:
      self.head.previous = Node(key, None, self.head)
      self.head = self.head.previous
    else:
      cursor = self.head
      while cursor.next is not None and cursor.next.key <= key:
        cursor = cursor.next

      if cursor.next is None:
        self.tail = cursor.next = Node(key, cursor, cursor.next)
      else:
        cursor.next = cursor.next.previous = Node(key, cursor, cursor.next)

  def show_forward(self):
    cursor = self.head
    while cursor is not None:
      print(cursor.key)
      cursor = cursor.next

  def show_backward(self):
    cursor = self.tail
    while cursor is not None:
      print(cursor.key)
      cursor = cursor.previous

def main():
  doubly_linked_list = DoublyLinkedList()

  doubly_linked_list.add(5)
  doubly_linked_list.add(4)
  doubly_linked_list.add(2)
  doubly_linked_list.add(3)
  doubly_linked_list.add(4)
  doubly_linked_list.add(5)
  doubly_linked_list.add(6)
  doubly_linked_list.add(1)
  doubly_linked_list.add(7)
  doubly_linked_list.add(8)

  print('forward')
  doubly_linked_list.show_forward()

  print('backward')
  doubly_linked_list.show_backward()

if __name__ == "__main__":
  main()
