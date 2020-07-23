class BinaryTreeNode():
    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right
class BinaryTree(object):
    def __init__(self, root=None):
        self.root=root
    def preorder(self, root):
        if (root is None):
            return
        print(root.data, sep='-->', end='-->')
        self.preorder(root.left)
        self.preorder(root.right)

import re
phoneNumRegex=re.compile(r'(\(\d{4}\))(\d{3}-\d{4})')
mo=phoneNumRegex.search('My name is aadhar and my number is (0522)423-3190')
batregex=re.compile(r'\|(bat)(woman|man|mobile|girl)\|')
mo1=batregex.search('My superhero is |batwoman| and |batman|')
wildcardsregex=re.compile(r'.*')
mo2=wildcardsregex.findall("the bat ate the rat in a flat")

print(mo2)