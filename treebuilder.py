from PIL import Image, ImageDraw
from rich.tree import Tree
from rich import print
from learn import learn
age = learn()


strappend = ''
postures = []


def linePrinter(lst):
    prevpos = 0
    global strappend
    for pos in postures:
        strappend += ' '*(pos-prevpos+1)+'|'
        # print(' '*(pos-prevpos+1), end='|')
        prevpos = pos

    return prevpos


def treebuild(root, space):
    global strappend
    if type(root) != type(age):
        return strappend

    mline = len(root.name)
    prevpos = linePrinter(postures)
    spc = ' '*(space-prevpos)
    strappend += spc+'-' + root.name+'\n'

    # print(spc+'-', root.name)
    for i, child in enumerate(root.children):
        spc = ' '*(space-prevpos)
        charlen = len(child)
        ysn = root.children[child]
        prevpos = linePrinter(postures)

        if ysn == 'YES' or ysn == 'NO':
            strappend += spc+' +'+'-' * mline + \
                '-{}=>({})'.format(child, ysn) + '\n'
            # print(spc, '+', '-' *
            #       mline, '-{}=>({})'.format(child, ysn))

        else:
            strappend += spc + ' |+' + '-' * \
                mline + '-{}'.format(child)+'\n'
            # print(spc, '|+', '-'*mline, '-{}'.format(child))
            postures.append(space)
            if i == len(root.children)-1:
                postures.remove(space)
            treebuild(ysn,  mline+len(spc)+charlen+2)
            if postures:
                postures.pop(-1)
    return strappend


def imageBuild(str):
    print(strappend)
    image = Image.new("RGB", (800, 700), "white")
    d1 = ImageDraw.Draw(image)
    # font = ImageFont.truetype(size=42)
    d1.text((28, 36), strappend, fill='green')
    # image.show()
    image.save("treeGen.jpg")
