# -*- coding: UTF-8 -*-

#Creating Numpy arrays
import numpy as np

my_list1 = [1,2,3,4]
print 'Questa è una lista: ', my_list1

my_array1 = np.array(my_list1) # Per argomento riceve 1 sola lista o una touple!!
print 'Questo è un array: ', my_array1

my_list2 = [11,22,33,44]
my_lists = [my_list1, my_list2]
print 'Liste di liste: ', my_lists

my_array2 = np.array(my_lists)
print 'Array 2d: ', my_array2

