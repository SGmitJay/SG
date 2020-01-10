//希尔排序
//插入排序的改进
//希尔排序是基于插入排序的以下两点性质而提出改进方法的。
//插入排序对于几户已经排好序的数据操作时，效率高，既可以达到线性排序的效率
//插入排序一般是低效的，因为每次只能将数据移动一位。
#include<stdio.h>
void shell_sort(int arr[],int len){
	int temp,gap;
	for(gap=len/2;gap>0;gap=gap/2){
		for(int i=0+gap;i<len;i+=gap){
			temp=arr[i];
			int j=i-gap;
			while(j>=0&&arr[j]>temp){
				arr[j+gap]=arr[j];
				j=j-gap;
			}
			arr[j+gap]=temp;
		}
	}
}
int main(){
	
	int arr[]={22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70};
	int len=sizeof(arr)/sizeof(*arr);
	shell_sort(arr,len);
	for(int i=0;i<len;i++){
		printf("%4d\n",arr[i]);
	}
	return 0;
} 
