class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the pointer
        prev = current            # Move prev to current node
        current = next_node       # Move to the next node
    
    return prev  # New head of the reversed linked list

# Helper function to print the linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

print("Original Linked List:")
print_linked_list(head)

# Reverse the linked list
reversed_head = reverse_linked_list(head)

print("Reversed Linked List:")
print_linked_list(reversed_head)
