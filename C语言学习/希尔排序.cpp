//ϣ������
//��������ĸĽ�
//ϣ�������ǻ��ڲ�������������������ʶ�����Ľ������ġ�
//����������ڼ����Ѿ��ź�������ݲ���ʱ��Ч�ʸߣ��ȿ��Դﵽ���������Ч��
//��������һ���ǵ�Ч�ģ���Ϊÿ��ֻ�ܽ������ƶ�һλ��
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
