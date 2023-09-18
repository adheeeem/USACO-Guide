#include <bits/stdc++.h>
 
using namespace std;
 
#define hakuna_matata ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
 
typedef long long ll;
 
int t;
 
void solve() {
	ll n, x, arr[200002], flag = 1; cin >> n >> x;
	map<ll, ll> m, c;
	for (int i = 1; i <= n; i++) {
		cin >> arr[i];
		m[arr[i]] = i;
		c[arr[i]]++;
	}
	if (x%2==0 && c[x/2]>1) {
		int t = 2;
		for (int i = 1; i <= n; i++) {
			if (arr[i]==x/2 && t) {
				cout << i << ' ';
				t--;
			}
		}
	} else {
		for (int i = 1; i <= n; i++) {
			if (m[arr[i]] && m[x-arr[i]] && m[arr[i]]!=m[x-arr[i]]) {
				cout << m[arr[i]] << ' ' << m[x-arr[i]] << '\n';
				flag = 0;
				break;
			}
		}
	}
	if (flag) cout << "IMPOSSIBLE\n";
 
}
 
 
int main() 
{
	hakuna_matata
	//cin >> t;	
	t = 1;
	while (t--) {
		solve();
	}
	return 0;
}