#include <bits/stdc++.h>

#define ll long long

using namespace std;

void solve()
{
    ll n;
    cin >> n;
    string s;
    cin >> s;
    for (int i = 1; i <= 100; i++)
    {
        int l = 0, r = l + i;
        bool flag = true;
        while (r < s.size())
        {
            if (s[l] != s[r])
            {
                flag = false;
                break;
            }
            l++; r++;
        }
        if (flag)
        {
            cout << i << '\n';
            break;
        }
    }
}

int main()
{
    //freopen( "whereami.in", "r", stdin );
    //freopen( "whereami.out", "w", stdout );
    int t;
    t = 1;
    // cin >> t;
    while (t--)
        solve();
}
