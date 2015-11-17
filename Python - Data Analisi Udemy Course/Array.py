# -*- coding: UTF-8 -*-

#******************************************************************************
#******************************************************************************
#    1) CREATING ARRAYS
#******************************************************************************

# Import
# You can take care of floats... Otherwise 5/2=2...
from __future__ import division 
import numpy as np
from numpy import arange

# Linea di codice per settare le opzioni di printing delle matrici. Discorso da approfondire....
# In particolare:
# 1) non stampa -0 oppure 0. ma solo 0
# 2) i punti del decimale sono allineati
# 3) aleno 2 spazzi tra il primo carattere della colonna i quella i+1
np.set_printoptions(precision=2, suppress=True, linewidth=120)


print( '\n *** Creating Numpy arrays ***\n') 

print( 'np.array() prende UNA SOLA lista (oppure una lista composta da liste [ [],[],... ] separate da virgola) come argomento.\n')
my_list1 = [1,2,3,4]
print( 'Questa è una lista:\n', my_list1)

my_array1 = np.array(my_list1) 
print( 'Questo è un array:\n', my_array1 )

my_list2 = [11,22,33,44]
my_lists = [my_list1, my_list2]
print( '\nListe di liste:\n', my_lists )

my_array2 = np.array(my_lists)
<<<<<<< HEAD
print( 'Array 2D:\n', my_array2)
print( 'Array 3D:\n', np.array([[1,2,3],[11,22,33],[41,42,43]]) )

print ('\nSize of array: ', my_array2.size)
print ('Shape of array: ', my_array2.shape)
print ('This is the data tipe of the array: ', my_array1.dtype)

print ('\n *** You can make special arrays ***\n')
print ('Array di 0: ', np.zeros(5))
print ('Array 2d di 1:\n', np.ones((5, 5)))

print ('Oppure Arrayy tipo:')
print ('\n', np.ones((5, 5)))
print ('\n', np.zeros(5))
print ('\n', np.eye(5))
print ('\n', np.arange(5))

#******************************************************************************
#******************************************************************************
#    USING ARRAYS AND SCALARS
#******************************************************************************

print ('\n *** You can take care of floats... Otherwise 5/2=2... *** \n')
print ('5/2 = ', 5/2)

print('\nPuoi moltiplicare, sottrarre, sommare o dividere arrays...')

arr1 = np.array( (arange(10)+1,
                  arange(10),
                  arange(10)-1) )

print( 'Per esempio:\n', arr1 )
print( 'Moltimplico:\n', arr1*arr1 )
print( 'Sottraggo:\n', arr1-arr1 )
print( 'Divido:\n', 1/(arr1+5) )

#******************************************************************************
#******************************************************************************
#    INDEXING
#******************************************************************************
print( '\n *** Copiare e ottenere valori da un Array... ***\n')
print( "Per esempio l'array:\n", arr1 )

print( 'la prima riga è:\n', arr1[0])
print( 'il 6° elemento della 3° riga è:\n', arr1[2,5])
print( 'oppure: ', arr1[2][5])

print( '\nPosso selezionare slice di array...')
arr2 = np.arange(10,100,2).reshape(9,5) 
#IMPORTANTE: ho realmete creato un aoogetto,,,

print( 'In un Array di %s elementi...' %arr2.size)
print( '...come, per esempio:\n', arr2 )   
#IMPORTANTE: avevo chiamato arr2.reshape(9,5) dentro a print() e questo non modificava arr2 ma solo un'istanza.... 
print( '..che è una matrice: ', arr2.shape )

print( '\nposso selezionare dalla 4° alla 8° riga:\n', arr2[3:8]) 
print( '\noppure:\n', arr2[5:8,1:3] ) #arr2[righe,colonne] 
print( '\n Oppure posso usare una lista per selezionare le righe o le colonne:\n' )
print( arr2[:, [1,2,3] ] )

print( '\nPer copiare un array devo usare il metodo .copy()\n')

print( 'Set up an array...')
print( "Il metodo .shape[] può ricevere l'asse come argomento opzionale\n in questo caso l'ho usato per ottenere il numero delle righe..\n")
for i in range(arr2.shape[0]): 
    arr2[i] = i
    
print( 'Per esempio:\n',arr2 )

#******************************************************************************
#******************************************************************************
#    TRANSPOSIZIONE E FUNZIONI COMUNI
#******************************************************************************
print( '\nPosso anche applicare dei metodi builtIn...\n')
arr3 = np.arange(50).reshape((10,5))
print('Questa è la matrice:\n %s \ne questa è la sua trasposta:\n %s' %(np.array2string(arr3), np.array2string(arr3.T)) )
# il metodo np.array2string() serve per convertire in stringa...

print( 'Posso fare il prodotto scalare:\n ', np.dot(arr3,arr3.T))
print( '...calcolarne esponenziale:\n', np.exp(arr3) )
print( '...o la radice quadrata:\n', np.array2string(np.sqrt(arr3)) )

print( '\nCreare matrici random, sommarle, trovare il max tra 2..')
A, B = np.random.randn(100).reshape(10,10), np.random.randn(50).reshape(10,5)
print( 'A=', A, '\nB=', B)
print( '\nMax di A o B = ', np.maximum(A[:,:5],B))

# Uncomment if you want to open a webbrowser and see link...
#import webbrowser as wb 
#website = "http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs"
#wb.open(website)
#








=======
print 'Array 2d: ', my_array2
>>>>>>> refs/heads/Work_time
