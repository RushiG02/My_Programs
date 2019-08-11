#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    int q,y,x;
    set<int>s;
    cin>>q;
    while(q){
        cin>>y>>x;
        switch(y){
            case 1:
            s.insert(x);
            break;
            case 2:
            s.erase(x);
            break;
            case 3:
            set<int>::iterator itr=s.find(x);
            (itr!=s.end())?cout<<"Yes"<<endl:cout<<"No"<<endl;
            break;
        }
        q--;
    } 
    return 0;
}



