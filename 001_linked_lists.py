# Class structure for all problems:
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

class SinglyLinkedListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 001

# Print the elements of a linked list
# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem

def printLinkedList(head):
    while head.next:
        print(head.data)
        head = head.next
    print(head.data)

# 002

# Insert a node at the tail of a linked list
# https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem

def insertNodeAtTail(head, data):
    inputHead = head

    if head == None:
        return SinglyLinkedListNode(data)

    while head.next:
        head = head.next
    
    head.next = SinglyLinkedListNode(data)

    return inputHead

# 003

# Insert a node at the head of a linked list
# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem

def insertNodeAtHead(llist, data):
    if llist is None:
        return SinglyLinkedListNode(data)
    else:
        newHead = SinglyLinkedListNode(data)
        # added .next node on a separate line
        # HackerRank class to create new node doesn't accept a next node parameter
        newHead.next = llist
        return newHead

# 004

# Insert a node at a specific position in a linked list
# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem

def insertNodeAtPosition(head, data, position):
    if position == 0:
        newHead = SinglyLinkedListNode(data)
        newHead.next = head
        return newHead

    initialHead = head

    while position > 1:
        head = head.next
        position -= 1

    savedNext = head.next

    head.next = SinglyLinkedListNode(data)
    head.next.next = savedNext

    return initialHead

# 005

# Delete a node
# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

def deleteNode(head, position):
    if position == 0:
        return head.next

    initialHead = head

    while position > 1:
        head = head.next
        position -= 1

    # head now needs to reference head.next.next
    # but need to build in error checking in case we're deleting the last node

    if head.next.next:
        head.next = head.next.next
    else:
        head.next = None

    return initialHead

# 006

# Print in reverse
# https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

""" buggy initial attempt """
# the first element of each reversed linked list is printing out twice

# def reverseInputList(head):
#     newList = SinglyLinkedListNode(head.data)

#     while head.next:
#         print("in reverse input list", head.data)
#         head = head.next
#         newList = insertNodeAtPosition(newList, head.data, 0)

#     newList = insertNodeAtPosition(newList, head.data, 0)

#     return newList

# def reversePrint(head):
#     reversedList = reverseInputList(head)
#     printLinkedList(reversedList)

""" corrected code """
# didn't need to insert node after the while loop in reverseInputList()

def reverseInputList(head):
    newList = SinglyLinkedListNode(head.data)

    while head.next:
        head = head.next
        newList = insertNodeAtPosition(newList, head.data, 0)
    return newList

def reversePrint(head):
    reversedList = reverseInputList(head)
    printLinkedList(reversedList)

# 006

# Reverse a linked list
# https://www.hackerrank.com/challenges/reverse-a-linked-list/problem

def reverse(head):
    newList = SinglyLinkedListNode(head.data)

    while head.next:
        head = head.next
        newList = insertNodeAtPosition(newList, head.data, 0)
    return newList

# NOTE: This is basically reverseInputList() from 005

# 007

# Compare two linked lists
# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

def compare_lists(llist1, llist2):
    while llist1.next and llist2.next:
        if llist1.data == llist2.data:
            llist1 = llist1.next
            llist2 = llist2.next
        else:
            return 0

    if llist1.next is None and llist2.next:
        return 0
    elif llist1.next and llist2.next is None:
        return 0

    if llist1.data != llist2.data:
        return 0
    else:
        return 1

# 008

# Merge two sorted linked lists
# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

# initial bug
# lists to merge are 4, 5, 6 and 1, 2, 10
# current output is 1, 4, 4, 5, 6, 10
# I had a typo in the second while loop - was assigning head1.data when I should have been assigning head2.data
# fixed

def mergeLists(head1, head2):
    # return the other list if either list is None
    if head1 is None:
        return head2
    elif head2 is None:
        return head1

    # start a newList with the lowest data point
    if head1.data <= head2.data:
        newList = SinglyLinkedListNode(head1.data)
        head1 = head1.next
    else:
        newList = SinglyLinkedListNode(head2.data)
        head2 = head2.next

    # save pointer to head of newList to return
    initialNewList = newList

    while head1 and head2:
        if head1.data <= head2.data:
            newList.next = SinglyLinkedListNode(head1.data)
            head1 = head1.next
        else:
            newList.next = SinglyLinkedListNode(head2.data)
            head2 = head2.next
        newList = newList.next

    if head1 is None:
        newList.next = head2
    else:
        newList.next = head1

    return initialNewList

# 009

# Get node value
# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

# initial code had a bug - did not take into account the positionFromTail in the second while loop comparison

def getNode(head, positionFromTail):
    listLength = 0

    listCounterHead = head
    while listCounterHead.next:
        listCounterHead = listCounterHead.next
        listLength += 1

    while listLength - positionFromTail > 0:
        head = head.next
        listLength -= 1

    return head.data

# 010

# Delete duplicate-value nodes from a sorted linked list
# https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list/problem

# initial struggle:
# I was doing the reassignment of next at the same step of "incrementing" next
# So if there were multiple duplicates in a row, the code would remove one, but then skip over another

def removeDuplicates(head):
    newHead = head

    while head.next:
        if head.data == head.next.data:
            head.next = head.next.next
        else:
            head = head.next
    
    return newHead

# 011


