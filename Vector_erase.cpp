#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void Verase(vector<int> v,int n,int a,int b){
    v.erase(v.begin()+n-1);
    v.erase(v.begin()+a-1,v.begin()+b-1);
    cout<<v.size()<<endl;
    for(int i=0;i<v.size();i++)
      {cout<<v[i]<<" ";}

}
int main() {
    vector<int> v;
    int s,n,a,b,x;
    cin>>s;
    for(int i=0;i<s;i++)
     { cin>>x;
        v.push_back(x);
     }
    cin>>n>>a>>b;
Verase(v,n,a,b);
    return 0;
}
