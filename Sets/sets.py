Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

average = Sum of total disctinct heights /total number of distinct heights

Solution:

def average(array):
    # your code goes here
    sum1=0
    set_arr=set(arr)
    #print(set_arr)
    for i in set_arr:
        
        sum1+=i
    return(sum1/len(set_arr))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

    arr=set([12,2,2,3,5,6,7,8,9])

 **********************    Learning **********************
I tried using for loop with i index , it didn't worked bcos we cant iterate set
for item in arr:
    print(item)

my_set = set([1, 2, 3, 2])
print(my_set)
