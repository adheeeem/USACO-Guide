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
        bool flag = true;
        int l = 0, r = l + i;
        if (r > s.size())
            break;
        set<string> st;
        string ans;
        while (r <= s.size())
        {
            string foo = "";
            for (int i = l; i < r; i++)
            {
                foo += s[i];
            }
            ll temp = st.size();
            ans = foo;
            st.insert(foo);
            l++; r++;
            if (temp == st.size())
            {
                flag = false;
                break;
            }
        }
        if (flag)
        {
            cout << ans.size() << '\n';
            break;
        }
    }
}

int main()
{
    freopen("whereami.in", "r", stdin);
    freopen("whereami.out", "w", stdout);
    int t;
    t = 1;
    // cin >> t;
    while (t--)
        solve();
}
