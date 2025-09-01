#include <bits/stdc++.h>
class Solution {
public:
    int lengthOfLastWord(string s) {
      
      int len= s.size();
      int i = len-1;
      int count = 0;
      while(s[i]==' ')
      {
        i--;
      }
      while(i>=0)
      {
        if(s[i]!=' ')
        {
            count++;
        }
        else
        {
            break;
        }
        i--;
      }

      return count;
    
    }
};
