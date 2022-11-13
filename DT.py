import pandas as pd
import learn
import treebuilder
from utilty import *


data = pd.read_csv('DT2.csv', sep=',')
data.head(7)


node = runner(data)
node = learn.learn(name=node[0])


def visiter(data, node):

    # node.name='age'
    for cat in Counter(data[node.name]):  # branch[0]

        col, cat = node.name, cat
        # here if branch is 0 add child [predc]
        # else create a node in the name {branch[0]} and add it to this root

        dat = data[data[col].str.contains(cat)]
        print(dat)
        xx = edgechecker(dat, col, cat)
        if xx == 'YES' or xx == 'NO':
            print('xx>>>>', end=' ')
            node.children[cat] = xx
        else:
            newnodeName = runner(dat)
            print(newnodeName)
            newnode = learn.learn(newnodeName[0], {})
            node.children[cat] = newnode
            print(node.children, newnode.children)
            visiter(dat, newnode)
            # node = learn()
        print('>>>>>>>', col, cat, xx)


visiter(data, node)
print(node, node.name, node.children)

feature = ['36-55', 'master', 'high', 'single']
print('+++++++++++++++++++++++++++++++++++++++++ result')
learn.learned(feature, node)
print(data.columns)
treebuilder.treebuild(node, 0)
