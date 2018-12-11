# Description:  
This repository contains the software implementations of all the algorithms that I, as a student, studied while my time at UAH for undergraduate course "Intro to Design and Analysis of Algorithms". I have presented here more practical side of the course. By this I mean, I have presented implementations of the studied algorithms rather than the acutal theoritical explanations of the concepts. Although, I have to admit that I might as well present some theoritical explanations as well.

I might add some extra coding practises that are helpful at the end, after the section **Project2** ends. Lets see how far I can go with that.

A discretion advise to all is that this is not supposed to be a single stop for solution to assignments for others, but is intended to serve as a referral place for myself. The materials presented here, although, are hand-typed by me, do (may) not belong to me.

***

## The Start:  
  
Any algorithm course starts with the theoritical definitions of Growth of Functions. There are basically six-ways of expressing the growth of functions (as I have been taught as of now). Bit-O, Bit-\theta, and Bit-\omega and the lowercase versions of each of them. There are a lot of materials online that explains these concepts in detail. Please refer to one of them if you are some one who is not me. For myself, I would refer to [this line for quick refresher](https://cathyatseneca.gitbooks.io/data-structures-and-algorithms/content/analysis/notations.html) and [this link for another refresher](https://stackoverflow.com/questions/1364444/difference-between-big-o-and-little-o-notation).

One important thing to keep in mind as a student is the following sequencee. While analyzing algorithms, this would provide a shorter path to arrange the given growth rates from slowest to faster (although at time it will fail, so you need to use *Limit Rule* to verify).

*Constant << Logarithmic << Polynomial<Exponential << Factorial << n power n*  
  
The above order of functions show the relative order of function in increasing order of complexity. It is, however, by no means a definitive indicator that any functions should follow the given order.

## First Things:  

**Searching**  

### I:  

The first algorithm that I learnt was searching. First searching would always be in a random collection of data. Since random collection have no ordering (thus the name random), a simple search should be done where you start at the first element of the array or collection, check to see if that is what you want. If it is what you want, return with the information on how to find the element item again. If not, move on to the next one.  

I have implemented this in a fully runnable python program with a random collection (I have taken a list of integers). Some extra stuffs have been added for obvious correctness verificaiton.

```python
# This is the simple search code for GIT repo.

# This is random library
import random	
def simple_search(myList,key):
	'''
	This function takes a list and an element.
	If the element is in the list, it returns the Index of the item in list
		else it returns -1
	'''
	n=len(myList)
	for i in range(n):
		if myList[i]==key:
			return i
	return -1

def verify(myList,index,key):
	'''
	This function verifies the operation of searching is correct
	'''
	if index<0:
		return "Not Found in Array"
	if myList[index]==key:
		return True
	else:
		return False

if __name__=="__main__":
	num_elements = random.randint(1,101)
	myList = random.sample(range(num_elements),num_elements);

	key_to_search = random.randint(0,num_elements-1)
	index_returned =simple_search(myList,key_to_search)	#our answer is already in index_returned

	print("Found {} at index {} in array {}".format(key_to_search,index_returned,myList))

	# folllwing does the checking
	if verify(myList,index_returned,key_to_search)==True:
		print("The algorithm works correctly")
	else:
		print("Algo Not working")
```
 
## Project 1:  
**Project 1** mainly consists of two classes, namely  
 *sortEngine* (inside file helper.py) and  
 *myClass* (inside file main.py).  

-> Class *sortEngine* has a method *quick_sort(array,leftIdx,rightIdx)* which sorts the array in-place.  
-> Class *myClass* has to be initialized with a filename that is to be read.  
   The file consists of numbers that constitutes of a matrix. The first line, however, of the file should mention the number of rows and number of cols in the matrix.  
   *myClass* read the matrix, and using *method1()* of myClass, it sorts all the elements of the matrix, rearranges into the dimensions of the original matrix and prints the final matrix in the output file. The last line of the output file mentions the number of comparisons made and number of assignments done during sorting.  
   Using *method2()*, the matrix is sorted but in a different way. First, each row is sorted. Then each column is sorted. Final matrix is printed in another file in way similar to *method1()*. Both *method1()* and *method2()* make use of *quick_sort(...)*  from *sortEngine*.
->*main()* function prompts user for filename, and calls function *operate()* inside *myClass* which calls *method1()* and *method2()* 
  
## Project 2:  
**Project2** read a file for data and creates optimal binary search tree.  
The input file is named 'input.txt', which is already defined in the code. The nature of file should be such that the first line contains the number of keys desired, and each subsequent lines should be the value of keys (probability)  
It uses the concept of dynamic programming to build the matrix which is used to create the optimal BST  
The matrix generated as well as the final BST is printed to an output file