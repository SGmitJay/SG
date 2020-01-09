//冒泡排序
//它重复的走访过要排序的数列，一次比较两个元素，如果他们的顺序错误 
// 就把它们交换过来。 
#include<stdio.h>
void bubble_sort(int arr[],int len){
	int i,j,temp;
	for(i=0;i<len-1;i++){
		for(j=0;j<len-1;j++){
			if(arr[j]>arr[j+1]){
				temp=arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=temp;
			}
		}
	}
} 
int main(){
	int arr[]={22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70};
	int len=sizeof(arr)/sizeof(*arr);
	bubble_sort(arr,len);
	for(int i=0;i<len;i++){
		printf("%4d\n",arr[i]);
	}
	return 0;
} 
