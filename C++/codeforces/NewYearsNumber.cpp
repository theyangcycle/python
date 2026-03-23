#include <bits/stdc++.h>
using namespace std;

int main()
{
    long a;cin>>a;
    for (long b = 0;b<a;b++)
    {
        long n;cin>>n;
        if (n<2020){cout<<"NO"<<endl;}
        else if (n == 2020||n == 2021||n%2020 == 0||n%2021 == 0){cout<<"YES"<<endl;}
        else
        {
            while (true)
            {
                n -= 2021;
                if (n == 2021 || n%2020 == 0){cout<<"YES"<<endl;break;}
                else if (n<2020){cout<<"NO"<<endl;break;}
            }
        }
    }

    return 0;
}