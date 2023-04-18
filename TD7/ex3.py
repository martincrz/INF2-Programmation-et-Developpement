import collections

def fermant(c):
    if c=='{' :
        return '}'
    if c=='(' :
        return ')'
    if c=='[' :
        return ']'

def fctn(txt):
    pile=collections.deque()
    for caract in txt:
        if caract in ['{','(','[']:
            pile.append(caract)
        elif caract in ['}',')',']']:
            if caract==fermant(pile[-1]):
                pile.pop()
            else:
                print('KO')
                return False
    if len(pile)==0:
        print('OK')
        return True
    else:
        print('KO')
        return False




def exo3():
    txt=["{[(3+2)*5+(6-7)*(12+4)]/[2+4]}/14"]
    txt2=["())]]]"]
    fctn(txt)
    fctn(txt2)

if __name__ == '__main__':
    exo3()
