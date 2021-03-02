# def calculate(min, max):
#     result=0
#     while min<=max:
#         result+=min
#         min+=1
#     print(result)
# calculate(1,3)
# calculate(4,8)
# #請用你的程式補完這個


# def avg(data):
#     result=0
#     x=0
#     while x<data["count"]:
#         result=result+data["employees"][x]["salary"]
#         x+=1
#     print(result)

# # 請用你的程式補完這個函式的區塊
# avg({
#     "count":3,
#     "employees":[
#         {
#             "name":"John",
#             "salary":30000
#         },
#         {
#             "name":"Bob",
#             "salary":60000
#         },
#         {
#             "name":"Jenny",
#             "salary":50000
#         }
#     ]
# }) # 呼叫 avg 函式


# def maxProduct(nums):
#     n=1
#     answer=[]
    
#     while n<len(nums):
#         y=len(nums)-n
#         z=len(nums)-n-1
        
#         while z>=0:
#             answer.append(nums[y]*nums[z])
#             z-=1
#         n+=1
   
#     p=1
#     m=answer[0]
#     while p<len(answer):
        
#         if m>answer[p]:
#             p+=1
#         else:
#             m=answer[p]
#             p+=1
#     print(m)

    

# # 請用你的程式補完這個函式的區塊
# maxProduct([5, 20, 2, 6]) # 得到 120 因為 20 和 6 相乘得到最大值
# maxProduct([10, -20, 0, 3]) # 得到 30 因為 10 和 3 相乘得到最大值


#要求四


# def twoSum(nums, target):
#     # your code here
#     a=0
#     b=1
#     while a<len(nums):
#         while b<len(nums):
#             if nums[a]+nums[b]==target:
#                 return ("["+ str(a) +","+ str(b) +"]")
#             b+=1
#         a+=1
#         b=a+1
#     nums[0]

# result=twoSum([2, 11, 7, 15], 9)
# print(result) # show [0, 2] because nums[0]+nums[2] is 9

