//�������� 
//ͨ�������������У�����δ��������ݣ����Ѿ�����������дӺ���ǰɨ�裬�ҵ���Ӧλ�ò����롣 

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
#include<stdio.h>
int main(){
	
	int arr[]={22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70};
	int len=sizeof(arr)/sizeof(*arr);
	insertion_sort(arr,len);
	for(int i=0;i<len;i++){
		printf("%4d\n",arr[i]);
	}
	insertion_sort(arr,len);
	return 0;
} 


