#include <bits/stdc++.h>
using namespace std;

int main()
{
int a;cin>>a;
for (int b = 0;b<a;b++)
{
    string n;cin>>n;
    vector<int> best;
    int count = 0;
    bool boo = false;
    for (int i = n.size()-1;i>-1;i--)
    {
        if (n[i] == '0')
        {
            count += n.size()-1-i;
            for (int j = i-1;j>-1;j--)
            {
                if (n[j] == '0'||n[j] == '5')
                {
                    count += i-(j+1);
                    boo = true;
                    break;
                }
            }
            break;
        }
    }
    if (boo){best.push_back(count);}
    count = 0;
    boo = false;
    for (int i = n.size()-1;i>-1;i--)
    {
        if (n[i] == '5')
        {
            count += n.size()-1-i;
            for (int j = i-1;j>-1;j--)
            {
                if (n[j] == '2'||n[j] == '7')
                {
                    count += i-(j+1);
                    boo = true;
                    break;
                }
            }
            break;
        }
    }
    if (boo){best.push_back(count);}
    cout << *min_element(best.begin(),best.end())<<endl;
}

    return 0;
}