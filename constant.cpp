#include<bits/stdc++.h>
using namespace std;

int main(){
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif
    ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);

    string s, cons = "";
    bool flag = false;
    while(getline(cin,s)){
        for(int i=0; i<s.size(); ++i){
            if(s[i]>='0' && s[i]<='9'){
                if(s[i-1]==' ' || s[i-1]=='='|| s[i-1]=='*' || s[i-1]=='/' || s[i-1]=='+' || s[i-1]=='-'|| s[i-1]=='<' || s[i-1]=='>'){
                    while((s[i]>='0' && s[i]<='9') || s[i]=='.'){
                        cons += s[i];
                        ++i;
                    }
                    flag = true;
                }
                if(flag) {
                    cout<<cons<<endl;
                    flag = false;
                }
                cons="";
            }
        }
    }
return 0;
}
