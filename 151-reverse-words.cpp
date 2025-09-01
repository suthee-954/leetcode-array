class Solution {
public:
    string reverseWords(string s) {
       stack<string> st;
       istringstream iss(s);
       string word;
       while(iss >> word)
       {
           st.push(word);
       }
       s.clear();
       s=st.top();
       st.pop();
       while(!st.empty())
       {
        s=s+' '+st.top();
        st.pop();
        
       }
       return s;

    }
};
