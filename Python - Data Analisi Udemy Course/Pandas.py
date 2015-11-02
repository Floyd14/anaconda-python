# -*- coding: UTF-8 -*-

#******************************************************************************
#******************************************************************************
#    3) SERIES - DATA FRAMES
#******************************************************************************

# Imports
import numpy as np
import pandas as pd
from pandas import Series, DataFrame     # Si evita di scrivere pd.Series ecc... 
from unittest.mock import inplace

#Lets create a Series (array of data and data labels, its index)

obj = Series([3,6,9,12])    #
print( 'Questa è una serie:\n',obj)
print( '\nPuoi ottenere i valori:\t', obj.values)
print( '...e gli indici:\t', obj.index)


ww2_cas = Series([8700000,4300000,3000000,2100000,400000],index=['USSR','Germany','China','Japan','USA'])
print( '\nPosso personalizzare gli indici:\n',ww2_cas)

# Call a value
print( '\nCall a value..', ww2_cas['Germany'] )
# Can also check with array operations
print( 'o richiamare tramite un espressione..,', ww2_cas[ww2_cas>4000000] )
# Check if the's a value..
print( 'oppure fare il check di presenza di un valore..','USSR' in ww2_cas )

# Convert Series in Python dictionary
print( '\nConvertire in dictionary:\n', ww2_cas.to_dict())
print( 'o fare il contrario:\n', Series(ww2_cas.to_dict()) )

#We can use isnull and notnull to find missing data
print( pd.isnull(ww2_cas) )
print( ww2_cas )

# We can mixing two Series and sorting...
obj2 = Series([1,2],index=['Italy','France'])
#print( pd.concat([ww2_cas,obj2]).sort_index(inplace=True) ) 
# inplace = True  --> modifica realmente la serie !!
# il problema è che non posso richiamarla perchè non l'ho instanziata: ho usato metodi all'interno del metodo print()

s3 = pd.concat([ww2_cas,obj2]).sort_index(inplace=True)
print( s3 )

#add a name to a Serie or index
s3.name = 'World War 2 Casualties'
s3.index.name = 'Countries'
print( '\n', s3 )

#******************************************************************************
#******************************************************************************
#    DATAFRAMES
#******************************************************************************

#Add some data for Exemple
#import webbrowser as wb
#website = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'
#wb.open(website)

#Copy and read to get data..then showing
nfl_frame = pd.read_clipboard() #devo copiare dalla ClipBoard !! retunr Series
nfl_frame.to_csv(PATH()'nfl_frame.csv')

