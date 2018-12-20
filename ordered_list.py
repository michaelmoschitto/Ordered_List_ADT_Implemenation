class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           Do not have an attribute to keep track of size'''
        self.dummy = Node(None)
        self.dummy.next = self.dummy
        self.dummy.prev = self.dummy

    def is_empty(self):
        '''Returns back True if OrderedList is empty
            MUST have O(1) performance'''
        return self.dummy.next == self.dummy

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           If the item is already in the list, do not add it again
           MUST have O(n) average-case performance'''
        newNode = Node(item)
        if self.is_empty():
            self.dummy.next = newNode
            self.dummy.prev = newNode
            newNode.prev = self.dummy
            newNode.next = self.dummy
        else:
            currentNode = self.dummy

             #doesn't handle the edge case where it goes in the first or last spot

            for i in range(self.size()):
                # print(self.python_list())
                nextNode = currentNode.next
                if newNode.item < currentNode.next.item:
                    if i == 0:
                        self.dummy.next = newNode
                        newNode.prev = self.dummy
                    
                        nextNode.prev = newNode
                        newNode.next = nextNode
                        return
                    else:
                        currentNode.next = newNode
                        newNode.prev = currentNode

                        newNode.next = nextNode
                        nextNode.prev = newNode
                        return
                elif i == self.size() -1:
                    currentNode = currentNode.next
                    newNode.prev = currentNode
                    currentNode.next = newNode
                    newNode.next = self.dummy
                    self.dummy.prev = newNode
                currentNode = currentNode.next






    def remove(self, item):
        '''Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        if not self.is_empty():
            Node = self.dummy
            for i in range(self.size()):
                # Node = Node.next
                Node = Node.next
                if Node.item == item:
                    Node.prev.next = Node.next
                    Node.next.prev = Node.prev
                    return True
            return False
        else:
            raise IndexError('cannot remove from empty list')

    def index(self, item):
        '''Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        if not self.is_empty():
            Node = self.dummy
            for i in range(self.size()):
                Node = Node.next
                if Node.item == item:
                    return i
        return None



    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index >= self.size() or index < 0:
            raise IndexError('invalid index')
           
        if not self.is_empty():
            Node = self.dummy
            for i in range(index + 1):
                Node = Node.next
                nextNode = Node.next
                if i == index:
                    # if i == 0:
                    #     self.dummy.next = nextNode
                    #     nextNode.prev = self.dummy
                    #     return Node.item
                    # if i == self.size() - 1:
                    #     Node.prev.next = self.dummy
                    #     self.dummy.prev = Node.prev
                    #     return Node.item
                    # else:
                    Node.prev.next = nextNode
                    nextNode.prev = Node.prev.next
                    return Node.item

            

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_helper(self.dummy.next, item)

    def search_helper(self, node, item):
        if node.item == item:
            return True
        if node.next == self.dummy:
            return False
        return self.search_helper(node.next,item)



    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        pythonList = []
        Node = self.dummy.next
        while Node != self.dummy:
            pythonList.append(Node.item)
            Node = Node.next
        return pythonList


    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.reverse_helper(self.dummy.prev)

    def reverse_helper(self, node):
        print(node.prev.item)
        if node == self.dummy:
            return []
        return [node.item] + self.reverse_helper(node.prev)


    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.dummy.next,0)

    def size_helper(self,node,count):
        if node == self.dummy:
            return count
        return self.size_helper(node.next, count + 1)
