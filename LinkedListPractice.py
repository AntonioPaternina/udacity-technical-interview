"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        currentPosition = 1
        currentElement = self.head
        if currentElement is not None:
            nextElement = currentElement.next
            while nextElement is not None and currentPosition < position:
                currentPosition += 1
                currentElement = nextElement
                nextElement = currentElement.next

        if currentPosition == position:
            return currentElement
        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # get element just before the position
        elementBefore = self.get_position(position - 1)
        # if there is no element before then this will be head
        if elementBefore is None:
            if position == 0:
                self.head = new_element
            return
        # check if there is an element at the given position
        existingElement = elementBefore.next
        # if there is, new element must point to the existing element
        if existingElement is not None:
            new_element.next = existingElement
        # update previous element to point to new element
        elementBefore.next = new_element


    def delete(self, value):
        """Delete the first node with a given value."""
        # if the element is head, just delete it
        element_before = self.head
        current_element = self.head
        if current_element.value == value:
            if current_element.next is not None:
                self.head = current_element.next
            else:
                self.head = None
            return
        # if the element has a next then
        while current_element.next is not None:
            current_element = current_element.next
            if current_element.value == value:
                # the element before's next must be set to the next element
                element_before.next = current_element.next
                return

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
