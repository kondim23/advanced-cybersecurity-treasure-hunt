
a = 7
counter = 1
counter2 = 2
while ( counter != 48 ) :
    if ( "7" in str(a * counter2) ):
        counter += 1
    counter2 += 1
print(str(a*(counter2-1)))
