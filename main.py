import random
import time
from algoSortare import *


def nearly_sorted_numbers(n):
    if n >= 100:
        x = n//10
    elif n >= 10:
        x = 9
    else:
        x = 4 
    numbers = []    
    for i in range(1,n):
        if i%x==0: 
            numbers.append(random.randint(0,n))
        else:
            numbers.append(i)
    return numbers

def nearly_sorted(lst):
  new_lst = lst[:]
  n = len(new_lst)
  for i in range(n):
    j = random.randint(max(0, i-1), min(n-1, i+1))
    new_lst[i], new_lst[j] = new_lst[j], new_lst[i]
  return new_lst


#listaDeSortat = random.sample(range(0, 1000000), dimensiune)

###SORTARE ELEMENTE APROAPE SORTATE
###

dimensiune = 10000
#bubbleSort(copis) #pentru calcul bubbleSort lista aproape sortata
while dimensiune < 200000:
    listaDeSortat = nearly_sorted(nearly_sorted_numbers(dimensiune)) 

    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    cocktail_shaker_sort(copis)
    timp_sfarsit = time.perf_counter();
    print("Cocktail Shaker Sort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)

    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    Quicksort(copis, 0, len(copis) - 1 )
    timp_sfarsit = time.perf_counter();
    print("QuickSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)



    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter()
    heapSort(copis)
    timp_sfarsit = time.perf_counter()

    print("HeapSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)

    #print(copis)

    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    radixSort(copis)
    timp_sfarsit = time.perf_counter();
    print("radixSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)


    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    MergeSort(copis, 0, len(copis)-1)
    timp_sfarsit = time.perf_counter();
    print("MergeSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)

    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    shellSort(copis)
    timp_sfarsit = time.perf_counter();
    print("ShellSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)



    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    SelectionSort(copis)
    timp_sfarsit = time.perf_counter();
    print("SelectionSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)



    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    InsertionSort(copis)
    timp_sfarsit = time.perf_counter();
    print("InsertionSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)

    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter()
    bubbleSort(copis)
    timp_sfarsit = time.perf_counter()

    print("bubbleSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)
    if(dimensiune == 10000):
        dimensiune *= 10
    elif dimensiune == 100000:
        dimensiune *= 2
    else: 
        break

###SFARSIT SORTARE LISTA APROAPE SORTATA
### SORTARE ELEMENTE ALEATORII
dimensiune = 10000
while dimensiune < 200000:
    listaDeSortat = random.sample(range(0, 1000000), dimensiune)

    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    cocktail_shaker_sort(copis)
    timp_sfarsit = time.perf_counter();
    print("Cocktail Shaker Sort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)

    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    Quicksort(copis, 0, len(copis) - 1 )
    timp_sfarsit = time.perf_counter();
    print("QuickSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)



    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter()
    heapSort(copis)
    timp_sfarsit = time.perf_counter()

    print("HeapSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)

    #print(copis)

    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    radixSort(copis)
    timp_sfarsit = time.perf_counter();
    print("radixSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)


    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    MergeSort(copis, 0, len(copis)-1)
    timp_sfarsit = time.perf_counter();
    print("MergeSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)

    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    shellSort(copis)
    timp_sfarsit = time.perf_counter();
    print("ShellSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)



    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    SelectionSort(copis)
    timp_sfarsit = time.perf_counter();
    print("SelectionSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)



    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter();
    InsertionSort(copis)
    timp_sfarsit = time.perf_counter();
    print("InsertionSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)

    copis = listaDeSortat.copy();
    timp_inceput = time.perf_counter()
    bubbleSort(copis)
    timp_sfarsit = time.perf_counter()

    print("bubbleSort s-a executat in ", (timp_sfarsit-timp_inceput), " secunde si a sortat ", dimensiune)
    if(dimensiune == 10000):
        dimensiune *= 10
    elif dimensiune == 100000:
        dimensiune *= 2
    else: 
        break