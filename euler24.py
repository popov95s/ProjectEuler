import itertools

perms = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))

perms.sort()

print perms[999999]