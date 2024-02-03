
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

  def create_forward_iterator(self):
    return ForwardIterator(self)

  def create_backward_iterator(self):
    return BackwardIterator(self)

class ForwardIterator:

  def __init__(self, doubly_linked_list):
    self.cursor = doubly_linked_list.head

  def next(self):
    if self.cursor is not None:
      current = self.cursor
      self.cursor = self.cursor.next
      return current

  def has_next(self):
    return self.cursor is not None

class BackwardIterator:

  def __init__(self, doubly_linked_list):
    self.cursor = doubly_linked_list.tail

  def next(self):
    if self.cursor is not None:
      current = self.cursor
      self.cursor = self.cursor.previous
      return current

  def has_next(self):
    return self.cursor is not None

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
  iterator = doubly_linked_list.create_forward_iterator()

  while iterator.has_next():
    print(iterator.next().key)

  print('backward')
  iterator = doubly_linked_list.create_backward_iterator()

  while iterator.has_next():
    print(iterator.next().key)

if __name__ == "__main__":
  main()
