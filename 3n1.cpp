#include <iostream>
#include <algorithm>
using namespace std;
int main(int argc, char const *argv[]) {
  int i,n1,n2,temp,a[1000],j;
  while(cin>>n1>>n2&&n1!=0){

  cout<<n1<<"\t"<<n2<<"\t";
    int n=n2-n1;
    j=0;
  while(n1<=n2){
  temp=n1;
  i=1;

  while (temp!=1) {
    if (temp%2==0) {
      temp=temp/2;
    }
    else{
    temp=3*temp+1;
    }
    i++;
  }
  n1++;
  a[j++]=i;
}

cout<<*max_element(a, a + n)<<endl;
}
  return 0;
}
