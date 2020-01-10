//快速排序
//在区间中随机挑选一个元素作为基准，将小于基准的元素放在基准之前，将大于基准的元素放在基准之后，
//在分别对大数区与小数区排序
//迭代法

#include<stdio.h>
typedef struct _Range{
	int start,end;
	
}Range;

Range new_Range(int s,int e){
	Range r;
	r.start=s;
	r.end=e;
	return r;
}

void swap(int* x,int* y){
	int temp;
	temp=*x;
	*x=*y;
	*y=temp;
}

void quick_sort(int arr[],int len){
	if(len<=0){
		return ;
	}
	Range r[len];
	int p=0;
	r[p++]=new_Range(0,len-1);
	while(p){
		Range range=r[--p];
		if(range.start>=range.end){
			continue;
		}
		int mid=arr[(range.start+range.end)/2];    //选取中间点为基准点。
		int left=range.start,right=range.end ;
		do{
			while(arr[left]<mid){
				++left;    //检查基准点左侧是否符合要求 
			}
			while(arr[right]>mid){
				--right;
			} 
			if(left<=right){
				swap(&arr[left],&arr[right]);
				left++;
				right--;
			}
		}while(left<=right);
		if(range.start<right){
			r[p++]=new_Range(range.start,right);
		}
		if(range.end>left){
			r[p++]=new_Range(left,range.end);
		}
	}
}
int main(){
	int arr[]={22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70};
	int len=sizeof(arr)/sizeof(*arr);
	quick_sort(arr,len);
	for(int i=0;i<len;i++){
		printf("%4d\n",arr[i]);
	}
	
	return 0;
}
