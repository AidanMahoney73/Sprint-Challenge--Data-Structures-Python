class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        pass

    # def reverse_list(self, node, prev):
    #     if node is None:
    #         return None

    #     if node.next_node is not None:
    #         self.reverse_list(node.next_node, node)
    #         node.set_next(prev)
    #     else:
    #         node.set_next(prev)
    #         self.head = node

if __name__ == "__main__":
    llist = LinkedList()
    llist.add_to_head(1)
    llist.add_to_head(2)
    llist.add_to_head(3)
    llist.add_to_head(4)
    llist.add_to_head(5)

    self.assertEqual(self.list.head.value, 5)
    self.list.reverse_list(self.list.head, None)
    self.assertEqual(self.list.head.value, 1)
    self.assertEqual(self.list.head.get_next().value, 2)
    self.assertEqual(self.list.head.get_next().get_next().value, 3)


    self.list.add_to_head(1)
    self.list.add_to_head(2)
    self.list.add_to_head(3)
    self.list.add_to_head(4)
    self.list.add_to_head(5)
    self.assertEqual(self.list.head.value, 5)
    self.list.reverse_list(self.list.head, None)
    self.assertEqual(self.list.head.value, 1)
    self.assertEqual(self.list.head.get_next().value, 2)
    self.assertEqual(self.list.head.get_next().get_next().value, 3)
