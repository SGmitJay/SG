//¹é²¢ÅÅÐò
//µü´ú·¨
#include<stdio.h>
#include<stdlib.h>
int min(int x,int y){
	return (x>y)?y:x;
} 
void merge_sort(int arr[],int len);

int main(){
	
	int arr[]={22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70};
	int len=sizeof(arr)/sizeof(*arr);
	merge_sort(arr,len);
	for(int i=0;i<len;i++){
		printf("%4d\n",arr[i]);
	}
	return 0;
} 


void merge_sort(int arr[],int len){
	int* a=arr;
	int* b=(int*)malloc(len*sizeof(int));
	int seg,start;
	for(seg=1;seg<len;seg+=seg){
		for(start=0;start<len;start+=seg+seg){
			int low =start;
			int mid=min(start+seg,len);
			int high=min(start+seg+seg,len);
			int k=low;
			int start1=low, end1=mid;
			int start2=mid, end2=high;
			while(start1<end1&&start2<end2){
				b[k++]=a[start1]<a[start2]?a[start1++]:a[start2++];
			
			}
			while(start1<end1){
				b[k++]=a[start1++];
			}
			while(start2<end2){
				b[k++]=a[start2++];
			}
			
			
		}
		int* temp=a;
		a=b;
		b=temp;
	}
	if(a!=arr){
		for(int i=0;i<len;i++){
			b[i]=a[i];
		}
		b=a;
	}
	free(b);
}
