#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n,q,x;
    cin>>n;
    vector<int> a;
    for(int i=0;i<n;i++){
        cin>>x;
        a.push_back(x);
    }
    cin>>q;
    while(q--){
        cin>>x;
       //vector<int>::iterator f=find (a.begin(), a.end(), x);
        //vector<int>::iterator l=lower_bound (a.begin(), a.end(), x);
        if(find (a.begin(), a.end(), x)!=a.end())
        cout<<"Yes "<<lower_bound (a.begin(), a.end(), x)-a.begin()+1<<endl; 
        else
        cout<<"No "<<lower_bound (a.begin(), a.end(), x)-a.begin()+1<<endl;

    }    

    return 0;
}
