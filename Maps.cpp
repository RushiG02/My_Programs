#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int q,t,mk;
    string nm;
    map<string,int>m;
    cin>>q;
    while(q){
        cin>>t;
        if(t==1){
            cin>>nm>>mk;
        }
        else {
        cin>>nm;
        }
        switch(t){
            case 1:
            if ( m.find(nm) == m.end() ) {
  m.insert(make_pair(nm,mk));
}           else {
  m[nm]+=mk;
}
          
            break;
            case 2:
            m.erase(nm);
            break;
            case 3:
            cout<<m[nm]<<endl;
            break;
        }
        q--;
    }
    return 0;
}



