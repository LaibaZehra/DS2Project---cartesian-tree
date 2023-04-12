import math
class Node:
    def __init__(self,val,left = None,right = None,parent = None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class CartesianTree:
    def __init__(self,lst,start,end) -> None:
        self.root = self.constructree(lst,start,end)
        if not lst:
            return None
    def minimumelement(self,lst,start,end):
        min = start
        for i in range(start + 1 , end + 1):
            if lst[min] > lst[i]:
                min = i
        return min
    def display(self,root):
        if root is None:
            return
        self.display(root.left)
        print(root.val)
        self.display(root.right)
    def constructree(self,inorder,start,end):
        if start > end:
            return None
        index = self.minimumelement(inorder,start,end)
        root = Node(inorder[index])
        root.left = self.constructree(inorder,start,index-1)
        root.right = self.constructree(inorder,index + 1,end)
        return root


    def insert(self, value):
        # create a new node with the given value
        new_node = Node(value)
        
        # if the tree is empty, make the new node the root of the tree
        if self.root is None:
            self.root = new_node
            return
        
        # find the last node on the rightmost path whose value is less than the new node's value
        parent = None
        current = self.root
        while current is not None and current.val <= new_node.val:
            parent = current
            current = current.right
            
        # make the new node the right child of the parent node
        new_node.parent = parent
        new_node.right = current
        if parent is None:
            self.root = new_node
        else:
            parent.right = new_node
        
        # fix the Cartesian tree properties
        while new_node.parent is not None and new_node.parent.val > new_node.val:
            # swap the values of the new node and its parent
            new_node.parent.val, new_node.val = new_node.val, new_node.parent.val
            # move up to the parent node
            new_node = new_node.parent


    def find(self,value):
        print(self.find_value(self.root,value))
    def find_value(self,root, value):
        if root is None:
            return None
        if root.val == value:
            return root
        if root.left is not None and root.left.val <= value:
            result = self.find_value(root.left, value)
            if result is not None:
                return result
        if root.right is not None and root.right.val <= value:
            result = self.find_value(root.right, value)
            if result is not None:
                return result
        return None
        

