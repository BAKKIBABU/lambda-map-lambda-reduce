# '''lambda returnts the squares'''
# '''lambda map'''
# list1=[1,2,3,4,5]
# list2=list(map(lambda x: x**3,list1))
# print(list2)                           # [1, 8, 27, 64, 125]
# tuple=(5,6,7,8,9)
# print(tuple**3)                          # TypeError: unsupported operand type(s) for ** or pow(): 'tuple' and 'int'
# tuple=(5,6,7,8,9)
# print(tuple*3)                          #  (5, 6, 7, 8, 9, 5, 6, 7, 8, 9, 5, 6, 7, 8, 9)
# m=(1,2,3,4)
# print(m*2)                                #  (1, 2, 3, 4, 1, 2, 3, 4)
# m=[1,2,3,4]
# print(m*2)                                 # [1, 2, 3, 4, 1, 2, 3, 4]
# m=[1,2,3,4]
# print(m**2)                                # TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
# ''' *lambda that returns products of elements of list from functools import*'''
# from functools import*
# a=[1,2,3]
# # b=[1,2,3,4,5]
# r=reduce(lambda x,y:x,a)
# p=reduce(lambda x,y:y,a)
# # w=reduce(lambda x,y:x+y,a)
# # c=reduce(lambda x,y:x-y,a)
# # print(r)
# # print(p)
# # print(w)
# # # print(c)
# # a=[10,12,14,16,18]
# # w=reduce(lambda x,y:x,a)
# # w=reduce(lambda x,y:y,a)
# # w=reduce(lambda x,y:x+y,a)
# # w=reduce(lambda x,y:x-y,a)
# print(p)
# print(r)
''' write  a program to create separate functions for each with local variable '''
''' name and each local variable should represent  the respective name from each place '''
# def sc(name='goutham'):
#     print(f"My Name in school is {name}")
#     wk()
# def cn(name='ravi'):
#     print(f"My Name in college is {name}")
#     sc()
# def wk(name='babu'):
#     print(f"My Name at work place is {name}")
#     cn()
# ''' this is infinity loop '''
# def sc(name='goutham'):
#     print(f"My Name in school is {name}")
#     wk()
# def cn(name='ravi'):
#     print(f"My Name in college is {name}")
#     sc()
# def wk(name='babu'):
#     print(f"My Name at work place is {name}")
    
# cn()