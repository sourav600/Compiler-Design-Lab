#include <bits/stdc++.h>
using namespace std;

int main(){
    cout<<"Enter the string: ";
    string s; cin>>s;
    int n = s.size();
    if(s[0]!='a' || s[n-1]!='d' || n%2){
        cout<<"String is Rejected\n";
        return 0;
    }

    for(int i=1; i<n-1; ++i){
        if(s[i]!='b'){
            cout<<"String is Rejected\n";
            return 0;
        }
        else{
            if(s[i+1]=='b' || s[i+1]=='c'){
                ++i;
            }else{
                cout<<"String is Rejected\n";
                return 0;
            }
        }
    }
    cout<<"String is Accepted\n";


    return 0;
}
