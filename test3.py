

# print ([1,2]*2)
#
# import array
#
# a = array.array('f', (1.0, 1.5, 2.0, 211222))
# print(a)
#
# import sys
# print (sys.version)
#
# import datetime
# print(datetime.datetime.now())


# x=range(10)
# print (type(x))
#
#
# x=zip([12,2,3],[2,3,34])
# for i in x:
#     print (i)

# print([lambda n: index * n for index in range (4)])(2)
# def multiplexers ():

# def fast (items= []):
# 	items.append (1)
# 	return items
#
# print(fast ())
# print(fast ())


# print('aeioubcdfg'[:3])

#
# 	return [lambda n: index * n for index in range (4)]
#
# print ([m (2) for m in multiplexers ()])





# def testProc(n=[]):
#     n=n.append(100)
#     print(n)
# # Do something with n
# testProc([1, 2, 3])  # Explicitly passing in a list
# testProc()  # Using a default empty list


# list = ['a', 'b', 'c', 'd', 'e']
#
# # print(list[:10])
# import collections
# str="My is Pintu singh kacchawa. The only way to live in this world is to stay safe for COVID-19. There are two ways to live"
#
# kv = collections.Counter(str.split())
# print(kv)
# keyMax=max(kv, key=kv.get)
# print (keyMax)
# xr=range(20)
# print(type(xr))
# it=iter([1,2,3])
# print(next(it))
# print(next(it))
# print(next(it))

# tp=(1,2,3,4,[1,2,3,4])
# print(id(tp))
# tp[4].append(200)
# print (id(tp))
# print (ord('9'))
# Tv = {'BreakingBad': 100, 'GameOfThrones': 1292, 'TMKUC': 88}
#
# Keymax = max(Tv, key=Tv.get)
# print(Keymax)

# import threading
# import multiprocessing
#
#
# def task1():
#     print("hello task 1")
#
# def task2():
#     print("hello task 2")


# if __name__=='__main__':
#     t1=threading.Thread(target=task1, name='t1')
#     t2=threading.Thread(target=task2, name='t1')
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#
# if __name__=='__main__':
#     t1=multiprocessing.Process(target=task1, name='t1')
#     t2=multiprocessing.Process(target=task2, name='t2')
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()


# def hello():
#     print("hello")
#     return
#
# s=hello()
#
# print(s)

x = 50


# def func():
#     global x
#
#     print('x is', x)
#     x = 2
#     print('Changed global x to', x)
#
#
# func()
# print('Value of x is', x)

# def test(a, b, c, d)
# def func():
#     text = 'Welcome'
#     name = (lambda x: text + ' ' + x)
#     return name
#
#
# msg = func()
# print(msg('All'))

# def addFunc(item):
#     item += [1]
#     print(item)
#
# mylist = [1, 2, 3, 4]
# addFunc(mylist)
# print (len(mylist))
#
# def heading(str):
#     print ("+++%s+++" % str)
# heading.id = 1
# print(heading.id)
# heading.text = "Python functions"
# heading("%d %s" % (heading.id, heading.text))

# for i in range(10):
#     print (i)


# try:
#    f = open("testfile", "r")
#    f.write("This is the test file for exception handling!!")
# except IOError:
#    print ("Error: could not find a file or read data")
# else:
#    print ("content is written in the file successfully")


# a=[1,2,3,4,5,6,7,8,9]
# # print(a[::3])

# a=[1,2,3,4,5]
# print(a[3:0:-1])

# def f(value, values):
#     v = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])


# init_tuple = [(0, 1), (1, 2), (2, 3)]
#
# result = sum(n for _, n in init_tuple)
#
# print(result)
#
# init_tuple = ('Python')
#
# print(type(init_tuple))

# import pdb
# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# print "before pdb trace"
# print pdb.set_trace()
# print "after pdb trace"
# crates['jars'] = jars
# print (crates['box'])
# print (len(crates[box]))
#
# dict = {'c': 97, 'a': 96, 'b': 98}

# for _ in sorted(dict):
#     print (dict[_])
# age=8
# name='pintu' if age>28 else 'Anil'
# print(name)
# y=1
# class classA:
#     def __init__(self,x):
#         print ("Iam A",x)
#
# class classB:
#     def __init__(self,x):
#         print("Iam B",x)
#
# x = (classA if y == 1 else classB)(10, 20)

# z=[x**2 if x%2==0 else x*2 for x in [1,2,3,4,5,6,7,8,9,10]]
# for i in z:
#     print (i)

# import threading
# print(threading)
#
# import pdb

# def test(x, y, z):
# 	print(x, y, z)
#
# testDict = {'x': 1, 'y': 2, 'z': 3}
# testList = [10, 20, 30]
#
# print " *testdict===",type([(1,2,3)])
# test('x','y','z')
# test(**testDict)
# test(*testList)

# result = (lambda k: reduce(int.__mul__, range(1,k+1)))(5)
# print(result)

result2=sum([x*x-1 for x in range(5)[::-1]])
print "result22===", result2
lt2=sum([x*x-1 for x in range(5)[::-1]])
print "result22===", result2

