# this is the helper function that has function names defined to perform some tasks as described in the 
# requirement

DEBUG_HELPER = False

class sortEngine:

    def __init__(self):
        self.comparison_count = 0
        self.assignment_count = 0

    def EQ(self,a,b):
        self.comparison_count+=1
        return a==b

    def LT(self,a,b):
        self.comparison_count+=1
        return a<b

    def GT(self,a,b):
        self.comparison_count+=1
        return a>b

    def ASSIGN(self,a,b):
        self.assignment_count+=1
        # since list is mutable
        a[0]=b[0]
        return

    def SWAP(self,a_l,b_l):
        c = [0.0]
        self.ASSIGN(c,b_l)
        self.ASSIGN(b_l,a_l)
        self.ASSIGN(a_l,c)

    def findMedian(self,array):
        if not len(array)==3:
            print("Less than 3 elements: Impossible to find median")

        if not self.LT(array[0],array[1]):
            if not self.LT(array[1],array[2]):
                return 1
            elif not self.GT(array[0],array[2]):
                return 0
            else:
                return 2
        else:
            if not self.LT(array[0],array[2]):
                return 0
            elif not self.LT(array[2],array[1]):
                return 1
            else:
                return 2

    def PARTITION_2(self,array,left,right):
        old_comp_count = self.comparison_count
        index = left
        for i in range(left,right):
            if self.LT(array[i],array[right]):
                # make a list and pass, since list is mutable
                a_l = [array[i]]
                b_l = [array[index]]
                self.SWAP(a_l,b_l)
                array[i] = a_l[0]
                array[index] = b_l[0]
                index+=1

        # make a list and pass, since list is mutable
        a_l = [array[right]]
        b_l = [array[index]]
        self.SWAP(a_l,b_l)
        array[right] = a_l[0]
        array[index] = b_l[0]

        if DEBUG_HELPER:
            print("Partition: Num of Elements: {}, Total Comp: {}, Comp Here: {}".format(right-left+1,self.comparison_count,self.comparison_count-old_comp_count))
            if self.comparison_count-old_comp_count>=(right-left+1):
                print("Large no of comparison on: {}",array[left:right+1])

        return index

    def PARTITION(self,array,left,right):
        # here we will take the middle element as the pivot,
        # swap the element with the first element and perform the same operation
        # the benefit as compared to partition_1 and partition_2 is that it provides
        # .. more dynamics
        midIndex = (right+left)//2

        # swap
        a_l = [array[left]]
        b_l = [array[midIndex]]
        self.SWAP(a_l,b_l)
        array[left] = a_l[0]
        array[midIndex] = b_l[0]

        old_comp_count = self.comparison_count
        index = left
        for i in range(left,right):
            if self.LT(array[i],array[right]):
                # make a list and pass, since list is mutable
                a_l = [array[i]]
                b_l = [array[index]]
                self.SWAP(a_l,b_l)
                array[i] = a_l[0]
                array[index] = b_l[0]
                index+=1

        # make a list and pass, since list is mutable
        a_l = [array[right]]
        b_l = [array[index]]
        self.SWAP(a_l,b_l)
        array[right] = a_l[0]
        array[index] = b_l[0]

        if DEBUG_HELPER:
            print("Partition: Num of Elements: {}, Total Comp: {}, Comp Here: {}".format(right-left+1,self.comparison_count,self.comparison_count-old_comp_count))
            if self.comparison_count-old_comp_count>=(right-left+1):
                print("Large no of comparison on: {}",array[left:right+1])

        return index

    # based on method2 of slide, and some modification
    def PARTITION_5(self,array,left,right):
        # here we will take the middle element as the pivot,
        # swap the element with the first element and perform the same operation
        # the benefit as compared to partition_1 and partition_2 is that it provides
        # .. more dynamics
        midIndex = (right+left)//2

        # swap
        a_l = [array[left]]
        b_l = [array[midIndex]]
        self.SWAP(a_l,b_l)
        array[left] = a_l[0]
        array[midIndex] = b_l[0]

        i = left+1
        j = right

        old_comp_count = self.comparison_count

        while(i<=j):
            while self.LT(array[left],array[j]):
                j-=1              
            while (i<=j) and (not self.GT(array[i],array[left])):
                i+=1
            if(i<=j):                        
                # make a list and pass, since list is mutable
                a_l = [array[i]]
                b_l = [array[j]]
                self.SWAP(a_l,b_l)
                array[i] = a_l[0]
                array[j] = b_l[0]
                j-=1
                i+=1
        
        # make a list and pass, since list is mutable
        a_l = [array[left]]
        b_l = [array[j]]
        self.SWAP(a_l,b_l)
        array[left] = a_l[0]
        array[j] = b_l[0]

        if DEBUG_HELPER:
            print("Partition: Num of Elements: {}, Total Comp: {}, Comp Here: {}".format(right-left+1,self.comparison_count,self.comparison_count-old_comp_count))
            if self.comparison_count-old_comp_count>=(right-left+1):
                print("Large no of comparison on: {}",array[left:right+1])
        return j

    # based on method2 of slide, and some modification
    def PARTITION_4(self,array,left,right):
        i = left+1
        j = right

        old_comp_count = self.comparison_count

        while(i<=j):
            while self.LT(array[left],array[j]):
                j-=1              
            while (i<=j) and (not self.GT(array[i],array[left])):
                i+=1
            if(i<=j):                        
                # make a list and pass, since list is mutable
                a_l = [array[i]]
                b_l = [array[j]]
                self.SWAP(a_l,b_l)
                array[i] = a_l[0]
                array[j] = b_l[0]
                j-=1
                i+=1
        
        # make a list and pass, since list is mutable
        a_l = [array[left]]
        b_l = [array[j]]
        self.SWAP(a_l,b_l)
        array[left] = a_l[0]
        array[j] = b_l[0]

        if DEBUG_HELPER:
            print("Partition: Num of Elements: {}, Total Comp: {}, Comp Here: {}".format(right-left+1,self.comparison_count,self.comparison_count-old_comp_count))
            if self.comparison_count-old_comp_count>=(right-left+1):
                print("Large no of comparison on: {}",array[left:right+1])
        return j

    # based on method2 of slide
    def PARTITION_1(self,array,left,right):
        i = left+1
        j = right

        old_comp_count = self.comparison_count

        while(i<=j):
            if not self.GT(array[i],array[left]):
                i+=1              
            elif not self.LT(array[j],array[left]):
                j-=1
            else:                        
                # make a list and pass, since list is mutable
                a_l = [array[i]]
                b_l = [array[j]]
                self.SWAP(a_l,b_l)
                array[i] = a_l[0]
                array[j] = b_l[0]
                j-=1
                i+=1
        
        # make a list and pass, since list is mutable
        a_l = [array[left]]
        b_l = [array[j]]
        self.SWAP(a_l,b_l)
        array[left] = a_l[0]
        array[j] = b_l[0]

        if DEBUG_HELPER:
            print("Partition: Num of Elements: {}, Total Comp: {}, Comp Here: {}".format(right-left+1,self.comparison_count,self.comparison_count-old_comp_count))
            if self.comparison_count-old_comp_count>=(right-left+1):
                print("Large no of comparison on: {}",array[left:right+1])
        return j

    def quick_sort(self,array,left,right):
        if(left<right):
            pivot = self.PARTITION(array,left,right)
            self.quick_sort(array,left,pivot-1)
            self.quick_sort(array,pivot+1,right)
        return

    def give_values(self):
        return self.comparison_count,self.assignment_count