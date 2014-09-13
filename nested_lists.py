def double(l):
    if not l:
        return l

    new = []
    for item in l:
        if type(item) == type(9) or type(item) == (0.0):
            doubled_item = item * 2
            new.append(doubled_item)
        elif type(item) == type([]):
            new_list = double(item)
            new.extend(new_list)

    return new

def double2(l):

    if not l:
        return

    for item in l:
        if type(item) == type(9) or type(item) == (0.0):
            doubled_item = item * 2
            print 'huh'
            print doubled_item
        elif type(item) == type([]):
            double(item)

l = range(-3, 10)
l2 = [2,3,[],[[3,[],[3,3]]]]
l3 = [2, [[]], 2]

print double(l2)
double2(l3)