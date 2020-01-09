//选择排序
//首先在未排序序列中找到最小（大），存放在排序序列的起始位置。
//然后，再从剩余未排序元素中寻找最小（大）元素，，放在已排序序列的末尾，以此类推，直到所有元素排序完毕
#include<stdio.h>
void swap(int *a,int *b){
	int temp=*a;
	*a=*b;
	*b=temp;
}
void selection_sort(int arr[],int len){
	for(int i=0;i<len-1;i++){
		int min=i;
		for(int j=i+1;j<len;j++){
			if(arr[j]<arr[min]){
				min=j;
			}
		}
		swap(&arr[min],&arr[i]);
	}
	
}

int main(){
	int arr[]={22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70};
	int len=sizeof(arr)/sizeof(*arr);
	selection_sort(arr,len);
	for(int i=0;i<len;i++){
		printf("%4d\n",arr[i]);
	}
//	int a=1;
//	int b=2;
//	swap(&a,&b);
//	printf("%d\t %d\t",a,b);
	return 0;
} 
