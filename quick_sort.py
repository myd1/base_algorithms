#-*- coding:utf-8 -*-
def quick_sort(L,low,high):
    i = low
    j= high
    if i > j:
        return L
    key = L[i]
    while L:
        # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
        while i < j and L[j] >= key:
            j = j - 1 #前移一位，只到找到比基数小的元素
            L[i] = L[j] #进行复制
        # 同样的方式比较前半区
        while i < j and L[i] <= key:
            i = i + 1
            L[j] = L[i]
    L[i] = key
    quick_sort(L,low,i-1)  #采用递归的对左边的进行排序
    quick_sort(L,i+1,high) #采用递归对右边的进行排序
    return L
if __name__ == '__main__':
    array = [49, 38, 65, 97, 76, 13, 27]
    quick_sort(array,1,6)
    print(array)

