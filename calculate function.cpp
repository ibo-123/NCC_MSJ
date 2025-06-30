#include <iostream>
 
using namespace std;
 
int main()
{
   long long int n,m,s;
  
    cin>>n;
    s=n%2;
    if (s==0){
        m=n/2;
        cout<<m;
    }
    else {
        m=n/2+1;
        cout<<-1*m;
    }
    }
