#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string r;
    r = " reverse it";
    
    int f=0,l=r.size()-1;
    while(f<l)
    {
        swap(r[f],r[l]);
        f++;
        l--;
    }
    
    cout << r;
    return 0;
}
