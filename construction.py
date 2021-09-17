class AVLTree:
    class Node:
        def __init__(self,val,left=None,right=None,bal_fac=0,height=0):
            self.data=val
            self.left=left
            self.right=right
            self.bal_fac=bal_fac
            self.height=height
    def updateheightandBalance(self,node):
        if node.left==None:
            lh=-1
        else:
            lh=node.left.height
        if node.right==None:
            rh=-1
        else:
            rh=node.right.height
        node.bal_fac=lh-rh
        node.height=max(lh,rh)+1
    def rightRotation(self,A):
        B=A.left
        A.left=B.right
        B.right=A
        self.updateheightandBalance(A)
        self.updateheightandBalance(B)
        return B
    def leftRotation(self,A):
        B=A.right
        A.right=B.left
        B.left=A
        self.updateheightandBalance(A)
        self.updateheightandBalance(B)
        return B
    def getRotation(self,node):
        self.updateheightandBalance(node)
        if node.bal_fac==2:
            if node.left.bal_fac==1:
                #LL Structure-> call for right rotation
                return self.rightRotation(node)
            elif node.left.bal_fac==-1:
                # LR Structure
                #left rotation on B node
                node.left=self.leftRotation(node.left)
                return self.rightRotation(node)

        elif node.bal_fac==-2:
            if node.right.bal_fac==1:
                #RR Structure
                node.right=self.rightRotation(node.right)
                return self.leftRotation(node)
            elif node.right.bal_fac==-1:
                # RL Structure
                return self.leftRotation(node)
        node=self.getRotation(node)
        return node
    def add_node_bst(self,node,data):
        if node==None:
            return self.Node(data)
        if data<node.left.data:
            node.left=self.add_node_bst(node.left,data)
        else:
            node.right = self.add_node_bst(node.right, data)
        node=self.getRotation(node)
        return node
    def display(self,root):
        if root == None:
            return
        str1 = ""
        if root.left == None:
            str1 += "."
        else:
            str1 += str(root.left.data)
        str1 += "<--" + str(root.data) + "--> "
        if root.right == None:
            str1 += "."
        else:
            str1 += str(root.right.data)
        print(str1)
        self.display(root.left)
        self.display(root.right)
    def remove_node(self,root,node,data):
        if node==None:
            return None
        if data < node.left.data:
            node.left = self.remove_node(node.left, data)
        elif data > node.left.data:
            node.right = self.remove_node(node.right, data)
        else:
            if node.left==None and node.right==None:
                return None
            elif node.left==None:
                return node.right
            elif node.right==None:
                return node.left
            else:
                temp=node.left
                while temp.right!=None:
                    temp=temp.right
                node.data=temp.data
                node.left=self.remove_node(node.left,temp.data)

        return node

def fun():
