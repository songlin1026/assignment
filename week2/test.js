// function calculate(min, max){
//     // 請用你的程式補完這個函式的區塊
//     result=0
//     while (min<=max){
//         result+=min
//         min++
//         }
//     console.log(result)
    
//     }
//     calculate(1, 3); // 你的程式要能夠計算 1+2+3，最後印出 6
//     calculate(4, 8); // 你的程式要能夠計算 4+5+6+7+8，最後印出 30




    // function avg(data){
    //     result=0
    //     x=0
    //     while (x<data["count"]){
    //     result=result+data["employees"][x]["salary"]
    //     x+=1
    //      }
    //     console.log(result/data["count"])
    //     }
    //     avg({
    //     "count":3,
    //     "employees":[
    //     {
    //     "name":"John",
    //     "salary":30000
    //     },
    //     {
    //     "name":"Bob",
    //     "salary":60000
    //     },
    //     {
    //     "name":"Jenny",
    //     "salary":50000
    //     }
    //     ]
    //     });

        // function maxProduct(nums){
        //     // 請用你的程式補完這個函式的區塊
        //     n=1
        //     answer=[]
            
        //     while (n<nums.length){
        //         y=nums.length-n
        //         z=nums.length-n-1
                
        //         while (z>=0){
        //             answer.push(nums[y]*nums[z])
        //             z-=1
        //         }
        //         n+=1
        //     }
        //     p=1
        //     m=answer[0]
        //     while (p<nums.length){
                
        //         if (m>answer[p]){
        //             p+=1
        //         }else{
        //             m=answer[p]
        //             p+=1
        //         }
        //     } 
        //     console.log(m)
            
        //     }
        
        //     maxProduct([5, 20, 2, 6]); // 得到 120 因為 20 和 6 相乘得到最大值
        //     maxProduct([10, -20, 0, 3]); // 得到 30 因為 10 和 3 相乘得到最大值

function twoSum(nums, target){

    // your code here
    a=0
    b=1
    while (a<nums.length){
        while (b<nums.length){
            if (nums[a]+nums[b]==target){
                return ("["+ a.toString() +","+ b.toString() +"]")
            }
            b+=1
        }
        a+=1
        b=a+1
    }
    nums[0]
    }
    result=twoSum([2, 11, 7, 15], 9)
    console.log(result) // show [0, 2] because nums[0]+nums[2] is 9