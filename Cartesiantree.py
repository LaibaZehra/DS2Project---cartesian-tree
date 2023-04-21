
class Node:
    def __init__(self,val,data,left = None,right = None,parent=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.parent=parent
        self.data=data
class CartesianTree:
    def __init__(self,lst,start,end,data) -> None:
        self.dic=data
        self.root = self.constructree(lst,start,end,None)
        if not lst:
            return None
    def minimumelement(self,lst, start, end):
        min_idx = start
        for i in range(start + 1, end + 1):
            if lst[min_idx] > lst[i]:
                min_idx = i
        return min_idx
        # return start + lst[start:end+1].index(min(lst[start:end+1]))

    def constructree(self,inorder,start,end,parent):
        if start > end:
            return None
        
        index = self.minimumelement(inorder,start,end)
        root = Node(inorder[index],self.dic[inorder[index]])
        root.parent=parent
        root.left = self.constructree(inorder,start,index-1,root)
        root.right = self.constructree(inorder,index + 1,end,root)
       
        return root
    def find(self,value):
        return(self.find_value(self.root,value))

    def search(self,value):
        if value!=None:
            ans=self.find(value)
            return ans.data
        return None
    
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
    def inorder(self):
        result = {}
        self._inorder(self.root, result)
        return result
    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        
        result[node.val]=node.data
        # print(result)
        self._inorder(node.right, result)

# create the Cartesian tree
# dic={1:['aplha'],2:["fnbr"],4:["po"],5:["uy"],8:["tc"]}
# car = CartesianTree([4, 1, 8, 2, 5], 0, 4,dic)
# val=car.inorder()
# print(val)
# # test find method
# print(car.find(4))  # output: 
# print(car.find(10))  # output: None

# # test delete method
# car.delete(8)
# print(car.inorder())  # output: [1, 2, 4, 5]
