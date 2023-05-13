#bubbleSort
def bubbleSort(v):
    
    sortat = False
    while not sortat:
        sortat = True
        for i in range(len(v)- 1):
            if v[i] > v[i+1]:
                aux = v[i]
                v[i] = v[i+1]
                v[i+1] = aux
                sortat = False
#sfarsitbubblesort



##quicksort

# functie de quicksort
 
def pivot_calc(v, left, right):
    pivot = v[(left+right) // 2]
    i = left - 1
    j = right + 1
    while( i < j ):
        i+=1
        while( v[i] < pivot ):
            i+= 1
        j -= 1
        while v[j] > pivot:
            j -= 1
        if i < j:
            v[i], v[j] = v[j], v[i]
    return j  

def Quicksort(v, left, right):
    if left < right:
        pivot = pivot_calc(v, left, right)
        Quicksort(v, left, pivot)
        Quicksort(v, pivot+1, right)


##sfarsit quicksort

###RadixSort

def numarare(v, poz):
    size = len(v)
    rez = [0] * size
    
    count = [0] * 10

    for i in range(0, size):
        index = v[i] // poz
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        index = v[i] // poz
        rez[count[index % 10] - 1] = v[i]
        count[index % 10] -= 1
        i -= 1;

    for i in range(0, size):

        v[i] = rez[i]
    return v;

def radixSort(v):
    max_element = max(v)

    place = 1
    while max_element // place > 0:
        numarare(v, place)
        place *= 10


### sfarsit radixSort
###mergeSort

def merge_list(v, left, middle, right):
    i = left;
    j = middle +1;
    new_v = []
    while i <= middle and j <= right:
        if v[i] < v[j]:
            new_v.append(v[i])
            i += 1
        elif v[i] > v[j]:
            new_v.append(v[j])
            j += 1
        else:
            new_v.append(v[i])
            new_v.append(v[j])
            i+=1
            j +=1
    while i <= middle:
        new_v.append(v[i])
        i += 1
    while j <= right:
        new_v.append(v[j])
        j += 1
    
    aux = 0
    for i in range(left, right + 1):
        v[i] = new_v[aux]
        aux += 1
    

def MergeSort ( array , left , right ) :
    if left < right :
        middle = ( left + right ) // 2
        MergeSort ( array , left , middle )
        MergeSort ( array , middle + 1, right )
        merge_list ( array , left , middle , right)

###sfarsit mergeSort

### inceput InsertionSort

def InsertionSort(v):
    dimensiune = len(v)

    for i in range(1, dimensiune):
        elem = v[i]
        j = i -1
        while j >= 0 and v[j] > elem:
            v[j +1 ] = v[j] 
            j -= 1
        v[j + 1] = elem
    return v

###sf insertion sort


def shellSort(v):
    n = len(v)

    spatiu = n // 2

    while spatiu > 0:


        for i in range(spatiu, n):
            tmp = v[i]
            j = i

            while j >= spatiu and v[j - spatiu] > tmp:
                v[j] = v[j - spatiu]
                j -= spatiu
            v[j] = tmp;
        spatiu //= 2

## sf shellsort
### start selectionSort
def SelectionSort(v):
    dimensiune = len ( v )

    for i in range ( dimensiune - 1) :
        poz_minima = i
        for j in range ( i + 1, dimensiune ):
            if v[ poz_minima ] > v [j ]:
                poz_minima = j
        v [i], v [ poz_minima ] = v [ poz_minima ], v [i]


### HeapSort

def constrHeap(v, n, i):
      largest = i
      l = 2 * i + 1
      r = 2 * i + 2
  
      if l < n and v[i] < v[l]:
          largest = l
  
      if r < n and v[largest] < v[r]:
          largest = r
  
      if largest != i:
          v[i], v[largest] = v[largest], v[i]
          constrHeap(v, n, largest)
  
  
def heapSort(v):
      n = len(v)
  
      for i in range(n//2, -1, -1):
          constrHeap(v, n, i)
  
      for i in range(n-1, 0, -1):
          v[i], v[0] = v[0], v[i]
  
          constrHeap(v, i, 0)
### final heapsort

##inceput cocktail shaker sort
def cocktail_shaker_sort(v):

    start = 0
    end = len(v) - 1
 
    swapped = False
    while (not swapped and end - start > 1):
        swapped = True
        for i in range(start, end):
            if v[i] > v[i + 1]:
                v[i], v[i+1] = v[i+1], v[i]
                swapped = False
        end = end - 1

        for i in range(end, start, -1):
            if v[i] < v[i - 1]:
                v[i], v[i-1] = v[i-1], v[i]
                swapped = False
        start = start + 1
### sfarsit cocktail shaker sort