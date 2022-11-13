import learn
typ = learn.learn()


def treebuild(root, space):
    if type(root) != type(typ):
        return

    spc = ' '*(space)
    mline = len(root.name)+4

    print(spc+'-', root.name)
    for child in root.children:
        charlen = len(child)
        ysn = root.children[child]
        if ysn == 'YES' or ysn == 'NO':
            print('|', spc, '+', '-'*mline, '-{}=>({})'.format(child, ysn))

        else:
            print('|', spc, '+', '-'*mline, '-{}'.format(child))
            treebuild(ysn, mline+len(spc)+charlen+2)
