import math
class Node:
    def __init__(self,val,left = None,right = None) -> None:
        self.val = val
        self.left = left
        self.right = right
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


        

