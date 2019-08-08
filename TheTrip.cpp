#include<bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[]) {
  while(1){
  int n;
  cin>>n;
  if(n==0)
  return 0;
  vector<float> a;
  for(int i=0;i<n;i++){
    float x;
  cin>>x;
  a.push_back(x);
}
double avg= accumulate(a.begin(),a.end(),0.00)/n;

for(int i=0;i<n;i++){
  a[i]-=avg;
}
float sum=0.0;
for(int i=0;i<n;i++){
  if(a[i]>0.0){
    sum+=a[i];
  }
}
printf("$%0.2f",sum);

}
}
