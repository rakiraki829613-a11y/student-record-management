#include<iostream>
using namespace std;

int main(){
    int aee[5]={10,19,18,17,16};
    cout<<"unique elements"<<endl;
    for(int i=0;i<5;i++){
        int cout=0;
    for(int j=0;j<5;j++){
        if(aee[i]==aee[j]){
            cout++;
        }
    }
    if(cout==1){
        cout<<aee[i]<<endl;  
    }
}
return 0;
}