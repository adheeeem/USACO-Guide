#include <bits/stdc++.h>

#define ll long long

using namespace std;

void solve()
{
  ll n, m, s = 0;
  cin >> n >> m;
  ll cards[m + 1][n + 1];
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < m; j++)
      cin >> cards[j][i];
  }

  for (int i = 0; i < m; i++)
  {
    sort(cards[i], cards[i] + n);
    for (int j = 0; j < n; j++)
    {
      s += j * cards[i][j] - (n - j - 1) * cards[i][j];
    }
  }
  cout << s << '\n';
}

int main()
{
  ll t;
  cin >> t;
  while (t--)
    solve();
}