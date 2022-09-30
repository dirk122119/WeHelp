# 第一題slide方式印出總和
# input (min,max,step)
# output sum
#O(n)
def calculate(min,max,step):
    temp=0
    for i in range(min,max+1,step):
        temp+=i
    print(temp)
calculate(1,3,1)
calculate(4,8,2)
calculate(-1,2,2)

# 第二題list and dic 得到非manager薪水平均值
# input json file
# output 平均薪資
#O(n)
def avg(data):
    sum=0
    nonmanagerNumber=0
    for item in data["employees"]:  
        if not item["manager"]:
            nonmanagerNumber+=1
            sum+=item["salary"]
    print(sum/nonmanagerNumber)
    
avg({
"employees":[
    {
        "name":"John",
        "salary":30000,
        "manager":False
    },
    {
        "name":"Bob",
        "salary":60000,
        "manager":True
    },
    {
        "name":"Jenny",
        "salary":50000,
        "manager":False
    },
    {
        "name":"Tony",
        "salary":40000,
        "manager":False
    }
    ]
})

# 第三題def in def
# f(a, b) calls f with two parameters a and b
# f(a)(b) calls f with one parameter a, which then returns another function, which is then called with one parameter b
# input (a)(int2,int3)
# output int2*int3+int1
#O(1)
def func(a):
    def operator(int1,int2):   
        return print(int1*int2+a)
    return operator

func(2)(3,4)
func(5)(1,-5)
func(-3)(2,9)

# 第四題 練一下刻bubble sort由大到小排序，比前兩個數字相乘或最後兩個負數相乘
# bubble sort -> O(n^2)
# 兩個迴圈 ->O(n^2)
def maxProduct(nums):
    # bubble sort 遞迴
    length=len(nums)
    def sort(length,nums):
        if length==1:
            return nums
        else:
            for indx in range(0,length-1,1):
                if(nums[indx]<nums[indx+1]):
                    temp=nums[indx]
                    nums[indx]=nums[indx+1]
                    nums[indx+1]=temp
            length=length-1
            return sort(length,nums)

    nums=sort(length,nums)

    # 排序完找是否最後兩個負數相乘大於前兩個正整數
    lastTwoItem=nums[-1]*nums[-2]
    firstTwoItem=nums[0]*nums[1]
    if (firstTwoItem>lastTwoItem):
        print(firstTwoItem)
    else:
        print(lastTwoItem)
    
  
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])
maxProduct([10, -20, 0, -3])
maxProduct([-1, 2])
maxProduct([-1, 0, 2])
maxProduct([5,-1, -2, 0])
maxProduct([-5, -2])

#第五題two sum
# O(n^2)
def twoSum(nums, target):
    for idx,item in enumerate(nums):
        try:
            if nums.index(target-item):
                return[idx,nums.index(target-item)]
        except ValueError:
            return "no item in list"
result=twoSum([2, 11, 7, 15], 9)
print(result)

#第六題 找0最長的長度
# O(n)
def maxZeros(nums):
    # 先轉成字串
    listToString=''
    for item in nums:
        listToString+=str(item)
    # 切字串
    ar=listToString.split('1')
    # 找出連續0最長的
    maxLength=0
    for item in ar:
        if len(item)>maxLength:
            maxLength=len(item)
    print(maxLength)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1]) 
maxZeros([0, 0, 0, 1, 1])