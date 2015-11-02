# -*- coding: UTF-8 -*-

#******************************************************************************
#******************************************************************************
#   2) Plot - Processing Arrays - IO
#******************************************************************************

# Import
import numpy as np
import matplotlib.pyplot as plt

#Set array for one side of grid
points = np.arange(-5,5,0.01)           #(start,stop,step)
dx,dy = np.meshgrid(points,points)      #return dx,dy from vector(point,point)
print( 'Creo una griglia su cui valutare una funzione:\n', dx )     #For exemple

print( '\nEvaluating Function...\n')
z = (np.sin(dx) + np.sin(dy))
print ( z )

print ('\n...Plotto la funzione...')
plt.imshow(z)
print( plt.imshow(z) )                  # plt.imshow() genera una AxesImage() ...
plt.colorbar()                          #Add colourbar on side .. da un warning..
plt.title('Grafico di sin(x)+sin(Y)')   #Give a plot title
#plt.show()                             # TOGLIERE PER MOSTRARE IL GRAFICO...


#******************************************************************************
#******************************************************************************
#   List Comprehension
#******************************************************************************
A = np.array([1,2,3,4])
B = np.array([100,200,300,400])
condition = np.array([True,True,False,False])


print( '''Usa show A_val se cond è vera otherwise show B_val per ogni A_val, B_val, cond in Zip()

zip() prende gli array che ho definito prima e 
ritorna list of touples [(1,100,True),(2,200,True),(A_val, B_val, cond)...] 
(A_val, B_val, cond sono nomni a caso)

[( ) for <indici della lista di touples> in <lista di touples [(),..]> ]
for.. in..
SI USA CON LE TOUPLE = insieme di dati non modificabili
''')


# Ho due modi per arrivare ad uno stesso risultato ma...
# Il primo mi fornisce una lista: [a,b,..]
# Il secondo (MIGLIORE) ritorna un array...

answer = [(A_val if cond else B_val) for A_val,B_val,cond in zip(A,B,condition)]
print( answer )

answer2 = np.where(condition, A, B)
print( answer2 )


from numpy.random import randn
arr = randn(10,10)
arr2 = np.where(arr < 0, 0, arr)
print( '\nProva del metodo where():\n' ,arr2)

print( '\nPosso calcolare la somma degli elementi:\t', arr2.sum())
print( 'La deviazione standard:\t\t\t', arr2.std() )
print( 'La varianza:\t\t\t\t' , arr2.var() )

print( '\nOrdinare la matrice:\n', np.sort(arr2.reshape(arr2.size)) )


print('\n unique() ordina toglie i duplicati...')
countries = np.array(['France', 'Germany', 'USA', 'Russia','USA','Mexico','Germany'])
print( countries )
print( np.unique(countries) )

print( '\nin1d() method test values in one array..')
print( np.in1d( ['France','USA','Italy'], countries ) )

#******************************************************************************
#******************************************************************************
#   INPUT - OUTPUT
#******************************************************************************

from Global import PATH                                                 # Usato per definire Variabili Globali   

# Saving on BINARY .npy or .npz
np.save( PATH() +'my_array', np.arange(10))                             # Save on binary file .npy
print( np.load(PATH() +'my_array.npy') )

# Saving multiple array into a zip file
np.savez(PATH() +'array_archive', x=np.arange(10), y=np.arange(20))     # Saving and indexing..
print( np.load(PATH() +'array_archive.npz')['y'] )                      # Loading the y one..
                                        

# Saving and loadin ,txt files
arr = np.array([[1,2,3],
                [4,5,6]])

np.savetxt(PATH() +'my_text.txt', arr, delimiter=',' )        # Saving
print( np.loadtxt(PATH() +'my_text.txt', delimiter=',') )     # Loading



