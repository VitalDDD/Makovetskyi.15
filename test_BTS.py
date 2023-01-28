import pytest

class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None



    def __str__(self):
        return str(self.id_node)

    # Insert method to create nodes
    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    # findval method to compare the id_node with nodes
    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            return str(self.id_node) + ' is found'

    # Print the tree
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.id_node)
        if self.right:
            self.right.print_tree()



    # Insert method to create nodes from the list
    def insert_list(self, list):
        for i in list:
            if type(i) is int:
                if self.id_node:
                    if i < self.id_node:
                        if self.left is None:
                            self.left = Tree(i)
                        else:
                            self.left.insert(i)
                    elif i > self.id_node:
                        if self.right is None:
                            self.right = Tree(i)
                        else:
                            self.right.insert(i)
                else:
                    self.id_node = i

    # Findval method to search for the greatest nodes

    def findval_max(self, ls=[]):

        if self.left:
            self.left.findval_max()
        ls.append(self.id_node)
        if self.right:
            self.right.findval_max()
        ls.sort(reverse=True)

        return ls[0]



    # Findval method to search for the smallest nodes

    def findval_min(self, ls=[]):
        if self.left:
            self.left.findval_min()
        ls.append(self.id_node)
        if self.right:
            self.right.findval_min()
        ls.sort()

        return ls[0]

    # Deleting method nodes
    def del_val(self, del_val):

        # Шукаємо значення
        if del_val < self.id_node:
            if self.left is None:
                return str(del_val) + " Not Found"
            return self.left.del_val(del_val)
        elif del_val > self.id_node:
            if self.right is None:
                return str(del_val) + " Not Found"
            return self.right.del_val(del_val)

        # Значення знайдено
        else:

            # Випадок 1: вузол що видаляється не має нащадків
            if self.left is None and self.right is None:
                self.id_node = 0

            # Випадок 2: вузол що видаляється має двох нащадків
            elif self.left and self.right:

                rev=Tree(self.left)
                while rev.right:
                    rev = rev.right

                self.id_node = rev

                self.left = 0

            # Випадок 3: вузол що видаляється має одного нащадка
            else:
                child = Tree(self.left if self.left else self.right)
                self.id_node = child
                self.left = 0
                self.right = 0

        return self.id_node



tree = Tree(8)
tree.left = Tree(3)
tree.left.left = Tree(1)
tree.left.right = Tree(6)
tree.left.right.left = Tree(4)
tree.left.right.right = Tree(7)
tree.right = Tree(10)
tree.right.right = Tree(14)
tree.right.right.left = Tree(13)



def test_insert():
    tree.insert(18)
    assert tree.findval(18) == '18 is found'

def test_findval_min():
    assert tree.findval_min() == 1

def test_findval_max():
    assert tree.findval_max() == 18

def test_del_val():
    tree.del_val(13)
    assert tree.findval(13) == '13 Not Found'






