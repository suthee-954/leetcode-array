

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string r;
    r = " reverse it";
    stack<char> st;
    
     for( char c : r)
     {
         st.push(c);
     }
     r.clear();
     
     while(!st.empty())
     {
         r.push_back(st.top());
         st.pop();
     }
     
     cout << r;
    return 0;
}
