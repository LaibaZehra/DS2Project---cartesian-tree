class Node:
    def __init__(self,val,left = None,right = None,parent=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.parent=parent
class CartesianTree:
    def __init__(self,lst,start,end) -> None:
        self.root = self.constructree(lst,start,end,None)
        if not lst:
            return None
    def minimumelement(self,lst,start,end):
        min = start
        for i in range(start + 1 , end + 1):
            if lst[min] > lst[i]:
                min = i
        return min
    def constructree(self,inorder,start,end,parent):
        if start > end:
            return None
        
        index = self.minimumelement(inorder,start,end)
        root = Node(inorder[index])
        root.parent=parent
        root.left = self.constructree(inorder,start,index-1,root)
        root.right = self.constructree(inorder,index + 1,end,root)
       
        return root
    def find(self,value):
        return(self.find_value(self.root,value))
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
    def find_successor(self, node):
        if node.right.val< node.left.val:
            return node.right
        else:
            return node.left
    def delete(self, value):
        node = self.find(value)
        if node is None:
            return
        if node.left is not None and node.right is not None:
            successor = self.find_successor(node)
            node.val, successor.val = successor.val, node.val
            node = successor
        if node.left is not None:
            child = node.left
        else:
            child = node.right
            
        if child is not None:
            child.parent = node.parent
            
        if node.parent is None:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        while child is not None:
            parent = child.parent
            if parent is None:
                break
            
            if parent.val < child.val:
                parent.val, child.val = child.val, parent.val
                child = parent
            else:
                break
   
car = CartesianTree([4,1,8,2,5],0,4)
car.delete(2)