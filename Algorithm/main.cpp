#include <iostream>
#include <vector>
#include <algorithm>
#include "tangram.h"
using namespace std;
int main() {
    string s;
    int n,m;
    do{
        cin>>n>>m;
        choose_mode(n,m);
        cout<<"Do you want to continue? y or n"<<'\n';
        cin>>s;
    }while(s=="y"); 
    return 0;

}
