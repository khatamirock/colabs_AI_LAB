import math
from collections import Counter
def logger(val, total, predc='', brnc='', coln=''):
    try:
        val = int(val)/total
        # print(coln,brnc,end= '  ')
        return (val*math.log2(val), 1)
    except:
        # print('(NO branch!!) ', coln,' ' ,brnc,'  ',predc)
        return (0, predc)

# col='age',cat='18-36'


def edgechecker(col, coln, cat):

    loctotal = len(col)
    bc_cnt = Counter(col['BC'])
    # print(total,col)
    no = logger(bc_cnt['yes'], loctotal, 'NO')
    yes = logger(bc_cnt['no'], loctotal, 'YES')
    main_inf_gain = -(no[0]+yes[0])

    if no[1] != 1:
        return no[1]
    elif yes[1] != 1:
        return yes[1]

    return main_inf_gain*(loctotal/20)


def ig2(col, coln, brnc, total):

    loctotal = len(col)
    bc_cnt = Counter(col['BC'])
    # print(loctotal,bc_cnt,total)
    no = logger(bc_cnt['yes'], loctotal, 'NO', brnc, coln)[0]
    yes = logger(bc_cnt['no'], loctotal, 'YES', brnc, coln)[0]
    main_inf_gain = -(no+yes)
    return main_inf_gain*(loctotal/total)

#


def runner(data):
# TODO can cause error... Use the data.columns method
    cols = set(['age', 'edu', 'incm', 'Mart stt'])

    tempstore = {}
    total = len(data)
    class_gain = ig2(data, 'BC', '', total)
    print(class_gain)
    # print(total)

    for col in cols:

        age_cata = Counter(data[col])

        age_ig = 0
        for cat in age_cata:
            # print(cat)
            dd = data[data[col].str.contains(cat)]
            age_ig += ig2(dd, col, cat, total)
        print('information gain for  ' + col + ' = ', class_gain - age_ig)
        tempstore[col] = class_gain - age_ig

    max(tempstore)

    arr = sorted(tempstore.items(), key=lambda x: x[1])
    return arr[-1]
