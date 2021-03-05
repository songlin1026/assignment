#要求一
def calculate(min, max):
    # 請用你的程式補完這個函式的區塊
    result=0
    while min<=max:
        result+=min
        min+=1
    print(result)
calculate(1, 3) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8) # 你的程式要能夠計算 4+5+6+7+8，最後印出 30


#要求二
def avg(data):
# 請用你的程式補完這個函式的區塊
    result=0
    x=0
    while x<data["count"]:
        result=result+data["employees"][x]["salary"]
        x+=1
    print(result/data["count"])

avg({
"count":3,
"employees":[
{
"name":"John",
"salary":30000
},
{
"name":"Bob",
"salary":60000
},
{
"name":"Jenny",
"salary":50000
}
]
}) # 呼叫 avg 函式


#要求三

def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    n=1
    answer=[]
    
    while n<len(nums):
        y=len(nums)-n
        z=len(nums)-n-1
        
        while z>=0:
            answer.append(nums[y]*nums[z])
            z-=1
        n+=1
   
    p=1
    m=answer[0]
    while p<len(answer):
        
        if m>answer[p]:
            p+=1
        else:
            m=answer[p]
            p+=1
    print(m)

maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值


#要求四

def twoSum(nums, target):
# your code here
    a=0
    b=1
    while a<len(nums):
        while b<len(nums):
            if nums[a]+nums[b]==target:
                return ("["+ str(a) +","+ str(b) +"]")
            b+=1
        a+=1
        b=a+1
    nums[0]
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#要求五
def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    a=0 #計算0數量
    b=0  #陣列項目
    c=[]
    d=0
    while b<len(nums):
        if nums[b]<1:
            b+=1
            a+=1

            if b>=len(nums):
                c.append(int(a))
                break
        else:
            c.append(int(a))
            a=0
            b+=1

    f=0 #最大數
    e=0 #項目數
    g=len(c)-1
    if len(c)==1:
        print(c[0])
    else:
        while e<g:
            if c[e]>c[e+1]:
                if f>c[e]:
                    e+=1
                else:
                    f=c[e]
                    e+=1
                    
            else:
                if f>c[e+1]:
                    e+=1
                else:
                    f=c[e+1]
                    e+=1
        print(f)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
