class learn:
    def __init__(self, name='', children={}):
        self.name = name
        self.children = children


# havegf = learn('havegf', {'hGF': 'yes', 'nGF': 'No'})

# edu = learn('edu', {'CSE': 'YES', 'EEE': 'NO', 'Mecha': havegf})

# marital = learn('marital', {'married': 'No', 'bachelor': edu})

# age = learn('age', {'<18': 'YES', '18-36': marital, '>55': 'No'})
age = learn()


def learner(root, node):
    if node not in root.children:
        return root
    if type(root.children[node]) != type(age):
        print(root.children[node])
        return None
        # return root.children[node]
    return root.children[node]
    # if type(node) != type(age):
    #     print(node)
    #     return
    # learner(root.children[node],)
    # root = root.children[node]

    # for child in root.children:
    #     if child == node:
    #         return child

    #     print(child, end=' >> ')
    #     learner(root, child)

# do here something like the while and pop
# and new node appear again take a requirement and
# check ... until both the stack is non-empty
# and returned node is type(learn)


def learned(lists, root):
    ftr = lists
    #  ['18-36', 'bachelor', 'EEE', 'hGF']
    newNode = root
    # age
    while(ftr):
        node = ftr.pop(0)
        newNode = learner(newNode, node)
        print('>>>checking and rolling')
