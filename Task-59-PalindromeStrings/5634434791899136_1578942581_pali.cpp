#include "bits/stdc++.h"
#include "ext/pb_ds/assoc_container.hpp"
#include "ext/pb_ds/tree_policy.hpp"

using namespace std;
using namespace __gnu_pbds;

#define ll long long int
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(a) a.begin(),a.end()
vector<ll> v[26];
ll b[26], freq[26];
void dfs(ll x) {
	// cout<<x<<" ";
	b[x] = 1;
	for(auto u: v[x]) {
		if(!b[u]) dfs(u);
	}
}
int main(void)
{
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    cin>>s;
    ll l = 0, r = s.length() - 1, c = 0, d = 0, i;
    while(l < r) {
    	if(s[l] != s[r]) {
    		v[s[l] - 'a'].pb(s[r] - 'a');
    		v[s[r] - 'a'].pb(s[l] - 'a'); 		
    		freq[s[l] - 'a'] = freq[s[r] - 'a'] = 1;
    	}
    	l++;
    	r--;
    }
    for(i=0; i<26; i++) {
    	if(freq[i]) {
    		d++;
    	}
    	if(v[i].size() != 0 && !b[i]) {
    		dfs(i);
    		c++;
    	}
    }
    cout<<d - c<<"\n";
}