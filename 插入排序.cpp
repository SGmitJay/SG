/*≤Â»Î≈≈–Ú*/

#include<stdio.h>

void insertion_sort(int arr[],int len);
int main(){
	
	int a[]={ 22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70 };
	int len=sizeof(a)/sizeof(*a);
	insertion_sort(a,len);
	int i;
	for(i=0;i<len;i++){
		printf("%4d",a[i]);
	}
	
	return 0;
} 

void insertion_sort(int arr[],int len){
	int i,j,temp;
	for(i=1;i<len;i++){
		temp=arr[i];
		for(j=i;j>0&&arr[j-1]>temp;j--){
			arr[j]=arr[j-1];
		}
		arr[j]=temp;
	}
}
