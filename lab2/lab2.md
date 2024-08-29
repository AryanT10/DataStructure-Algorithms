# Lab 2


### function 1:

1. The basic operation in this function is the addition and multiplication inside the loop.
2. The loop runs from `0` to `number - 1`, so it executes `number` times.
3. Inside the loop, the operations `x = (i + 1)` and `total += (x * x)` are constant time operations, `𝑂(1)`, and are executed `number` times.
4. The time complexity of function1 is `O(n)`, where `n` is the value of `number`.

```python
def function1(number):
    total = 0  # O(1)

    for i in range(0, number):  # O(n)
        x = (i + 1)  # O(1)
        total += (x * x)  # O(1)

    return total  # O(1)
    # T(n) = O(1) + O(n).O(1) + O(1) = O(n)
```
![Screenshot 2024-05-26 at 7 52 28 PM](https://github.com/seneca-dsa456-s24/labs-atuwar/assets/59858427/8d714f32-7b88-406f-b191-e630d739b5a7)



### function 2:

1. The basic operation is the arithmetic calculation.
2. The calculation is done in constant time.
3. The basic operation is executed once, regardless of number.
4. The time complexity of function2 is `O(1)`.

```python
def function2(number):
    # Calculate the sum of the squares of
    # the first 'number' natural numbers
	return  ((number)*(number+1)*(2*number + 1))/6 # O(1)
    # T(n) = O(1)
```

### function 3:

1. The outer loop runs `len(list) - 1` times, contributing 
`𝑂(𝑛)`
2. The outer loop runs `n - 1` times, and the inner loop runs `n - 1 - i` times.
3. The inner loop runs `len(list) - 1 - i` times for each `i`, resulting in \( \sum_{i=0}^{n-2} (n-1-i) \), which simplifies to \( \frac{(n-1)n}{2} \), or \( O(n^2) \).
4. operations inside the inner loop are 
𝑂(1) and are executed `n^2` times in total.
5. The time complexity of function3 is `O(n^2)`, where n is the length of the list.

```python

def function3(list):
	# length of the list
	n = len(list)                               # O(1)
	# Outer loop from 0 to n-2
	for i in range(n - 1):                      # O(n)
        # Inner loop from 0 to n-2-i
		for j in range(n - 1 - i):          # O(n)
			if list[j] > list[j+1]:     # O(1)
                # Swap the elements
				tmp=list[j]         # O(1)
				list[j]=list[j+1]   # O(1)
				list[j+1]=tmp       # O(1)

# T(n) = O(n^2)

```
![Screenshot 2024-05-26 at 7 52 54 PM](https://github.com/seneca-dsa456-s24/labs-atuwar/assets/59858427/56da1732-098a-4b10-a14a-3551bedcef7b)

### function 4:

1. The initialization of `total` is `𝑂(1)`.
2. The loop runs from `1` to `number - 1`, so it executes `number - 1` times.
3. Inside the loop, operation `total=total * (i + 1)` is executed `number - 1` times
4. The time complexity of function4 is `O(n)`

```python
def function4(number):
	total=1                     # O(1)
    # Loop from 1 to number-1
	for i in range(1, number):# O(n)
    # Multiply total by (i + 1)
		total=total*(i+1)   # O(1)
	return total                # O(1)

# T(n) = O(1) + O(n).O(1) + O(1) = O(n)
```
![Screenshot 2024-05-26 at 7 53 14 PM](https://github.com/seneca-dsa456-s24/labs-atuwar/assets/59858427/0c8ca8e9-4564-4389-bf2b-8a21ca8d6314)



## In class portion

### Function: partb_one



```python

def partb_one(mylist, key):
    total = 0
    for i in range(len(mylist)):  # O(n)
        for j in range(i + 1, len(mylist)):  # O(n)
            if i != j:  # O(1)
                if mylist[i] + mylist[j] == key:  # O(1)
                    total += 1  # O(1)
    return total  # O(1)

# T(n) = [(n-1)n]/2 = O(n^2)

```
![Screenshot 2024-05-26 at 7 53 27 PM](https://github.com/seneca-dsa456-s24/labs-atuwar/assets/59858427/7ace6d07-0552-4f36-a221-37f54b10a294)



1. The outer loop runs `len(mylist)` times, contiributing `O(n)`
2. The inner loop runs `len(mylist) - i - 1` times for each `i`, contributing `O(n)`
3. The nested loops gives us `O(n^2)`
4. operation inside the loop will give constant time,`O(1)`
5. Time complexity `T(n) = O(n^2)`

### Function: partb_two

```python
def partb_two(mylist, key):
    total = 0
    mylist.sort()  # O(n log n)
    i = 0
    j = len(mylist) - 1
    while i < j:  # O(n)
        if mylist[i] + mylist[j] < key:  # O(1)
            i += 1  # O(1)
        elif mylist[i] + mylist[j] > key:  # O(1)
            j -= 1  # O(1)
        else:
            total += 1  # O(1)
            i += 1  # O(1)
            j -= 1  # O(1)
    return total  # O(1)

# T(n) = O(nlogn) + O(n) = O(nlogn)

```

1. Sorting the list takes `O(nlogn)`
2. The while loop runs `len(mylist)` times, contributing `O(n)`
3. Inside the while loop, `O(1)`.

5. Time complexity `T(n) = O(nlogn)`

![Screenshot 2024-05-26 at 8 25 10 PM](https://github.com/seneca-dsa456-s24/labs-atuwar/assets/59858427/86a78357-c393-4e93-a4b3-87cbe0da2a8c)
   
### Function: partb_three

```python
def partb_three(mylist, key):
    items = {}  # O(1)
    total = 0
    for number in mylist:  # O(n)
        items[number] = 1  # O(1)
    for number in mylist:  # O(n)
        other = key - number  # O(1)
        if other in items:  # O(1)
            total += 1  # O(1)
    return total // 2  # O(1)
# T(n) = O(n) + O(n) = O(n)
```

1. Creating the dictionary `items` takes `O(n)`
2. The second loop will run `len(mylist)` times, which will give `O(n)`
3. the operation inside the second loop are constant time, `O(1)`
4. Time complexity `T(n) = O(n)`

![WhatsApp Image 2024-05-26 at 8 36 33 PM](https://github.com/seneca-dsa456-s24/labs-atuwar/assets/59858427/bbe0c6f4-65c2-4730-aaac-c9a969b90797)



### Group members
List the members of your group member below:

	• ARYAN TUWAR (112137229)
	• MEHTAB JAGDE (119003226)
	• SHUBH RAMCHANDANI (118554229)

### Timing Data

1. `partb_one`![PART_B_FUNCTION_1](https://github.com/seneca-dsa456-s24/labs-atuwar/assets/59858427/98c2a53c-a41c-444f-adaf-9a1c395ae941)

   

2. `partb_two`
![PART_B_FUNCTION_2](https://github.com/seneca-dsa456-s24/labs-atuwar/assets/59858427/b31047e0-62c9-49fc-9abc-66b963dd71e8)


3. `partb_three`
![PART_B_FUNCTION_3](https://github.com/seneca-dsa456-s24/labs-atuwar/assets/59858427/93a3787b-3103-415c-a77a-830056a005e8)


### Summary

### Timing Data

The following table shows the timing data collected for the three functions:

|Function   | runtime based on analysis | Most SImilar curve|
|-----------|---------------------------|-------------------|
|partb_one  |        $O(n^2)$           | Quadratic         |
|partb_two  |        $O(nlogn)$         | LogLinear         |
|partb_three|        $O(n)$             | Linear            |

### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach?  Write down your observations.

=> Efficent algorithms from lab 2 is outperforming simple methods such as nested loops and all from lab 1

=> Functions in lab2 is showing better scalability and performance, particularly for larger input sizes.

=> Lab2's use of more advanced techniques leads to considerable performance improvements, which higlighyts the importance of appropriate DSA


## Reflection:

## 1. Growth Rate Analysis

### partb_one
- **Expected Growth Rate:** `O(n^2)`
- **Observation:** The time increases approximately quadratically with the size, confirming `O(n^2)`.

### partb_two
- **Expected Growth Rate:** `O(nlogn)`
- **Observation:** The time increases slower than quadratic but faster than linear, consistent with `O(nlogn)`.

### partb_three
- **Expected Growth Rate:** `O(n)`
- The time increases linearly with the size, confirming `O(n)`.

## 2. Consistency of Analysis

- Yes, the analysis matches the observed results. The results confirm the theoretical time complexity analysis for all three functions, so there are no discrepancies between the analyses.

## 3. Conclusions

- Efficient algorithms (e.g., hash mapping) enhance performance and scalability compared to other methods such as nested loops.
- Linear `O(n)` and log-linear `O(nlogn)` algorithms scale well with large datasets, unlike the quadratic `O(n^2)` algorithm.
- The choice of data structures and algorithms (DSA) significantly impacts performance, highlighting the importance of selecting optimal approaches for large input sizes.

