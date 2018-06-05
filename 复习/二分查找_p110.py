#!/usr/bin/python3
#-*-coding:UTF-8-*-


print("有序数组中的二分查找")  
value=int(input("请输入您要查找的整数："))  
data_list=[10,11,12,17,19,21,22,24,32,38,49,51,66,78,90]

def BinarySearch(value,data_list):
    
    low=0   #最小数下标
    high=len(data_list)-1   #最大数下标
    
    while low<=high:
        
        mid = int((low+high)/2)  #中间数下标
        
        if value<data_list[mid]:  
            high = mid-1
            
        elif value>data_list[mid]:  
            low = mid+1
            
        else:  
            return print("%s在数组中的索引为%s"%(value,mid))  
    return print("%s不在该数组中"%value)  
BinarySearch(value,data_list)  
