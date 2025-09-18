class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> result;
       int n = nums.size();
       unordered_map<int,int> two;
       for(int i=0;i<n;i++)
       {
           int req=target-nums[i];
           if(two.find(req)!=two.end())
           {
            int i1 = two[req];
            result.push_back(i1);
            result.push_back(i);
            return result;
           }
           else
           {
            two[nums[i]]=i;
           }
       }
     return result;   
    }
};
