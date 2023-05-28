// http://www.usaco.org/index.php?page=viewproblem2&cpid=807

#include <iostream>

#define ll long long

using namespace std;

void teleport()
{
    ll tele, a, b, x, y; cin >> a >> b >> x >> y;
    if (a > b) swap(a, b);
    if (x > y) swap(x, y);
    tele = abs(a-x) + abs(b-y);
    cout << min(tele, abs(a-b));
}

int main()
{
    freopen("teleport.in", "r", stdin);
    freopen("teleport.out", "w", stdout);

    teleport();
    return 0;
}