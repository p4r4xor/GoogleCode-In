#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
 
using namespace __gnu_pbds;
using namespace std;

typedef long long int ll;
typedef unsigned long long int ull;
typedef long double ld;
typedef pair <ll, ll> pll;
typedef pair <int, int> pii;

typedef tree <ll, null_type, less <ll>, rb_tree_tag, tree_order_statistics_node_update> ordered_set;
// order_of_key(val): returns the number of values less than val
// find_by_order(k): returns an iterator to the kth largest element (0-based)

#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define all(a) a.begin(), a.end()
#define sz(a) (ll)(a.size())
#define endl "\n"

template <class Ch, class Tr, class Container>
basic_ostream <Ch, Tr> & operator << (basic_ostream <Ch, Tr> & os, Container const& x) 
{
    os << "{ ";
    for(auto& y : x) 
    {
        os << y << " ";
    }
    return os << "}";
}
template <class X, class Y>
ostream & operator << (ostream & os, pair <X, Y> const& p) 
{
    return os << "[" << p.ff << ", " << p.ss << "]";
}

ll gcd(ll a, ll b)
{
    if(b==0)
    {
        return a;
    }
    return gcd(b, a%b);
}
ll modexp(ll a, ll b, ll c)
{   
    a%=c;
    ll ans = 1;
    while(b)
    {
        if(b&1)
        {
            ans = (ans*a)%c;
        }
        a = (a*a)%c;
        b >>= 1;
    }
    return ans;
}
//Please adjust your input here. 20 is the chess board size (20x20)
const ll L = 20;
bool present[L][L];
auto seed = chrono::high_resolution_clock::now().time_since_epoch().count();
mt19937_64 mt(seed);
vector <ll> x;
bool isSafe()
{
    for(ll i=0; i<L; i++)
    {
        for(ll j=0; j<L; j++)
        {
            present[i][j] = false;
        }
    }
    for(ll i=0; i<L; i++)
    {
        present[i][x[i]] = true;
    }
    for(ll i=0; i<L; i++)
    {
        ll posx = i;
        ll posy = x[i];
        ll a = posx, b = posy;
        a++, b++;
        while(a < L && b < L)
        {
            if(present[a][b])
            {
                return false;
            }
            a++, b++;
        }   
        a = posx, b = posy;
        a++, b--;
        while(a < L && b >= 0)
        {
            if(present[a][b])
            {
                return false;
            }

            a++, b--;
        }
        a = posx, b = posy;
        a--, b--;
        while(a >= 0 && b >= 0)
        {
            if(present[a][b])
            {
                return false;
            }
            a--, b--;
        }
        a = posx, b = posy;
        a--, b++;
        while(a >= 0 && b < L)
        {
            if(present[a][b])
            {
                return false;
            }
            a--, b++;
        }
    }
    return true;
}
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    for(ll i=0; i<L; i++)
    {
        x.pb(i);
    }
    while(true)
    {
        shuffle(all(x), mt);
        if(isSafe())
        {
            for(ll i=0; i<L; i++)
            {
                for(ll j=0; j<L; j++)
                {
                    if(j == x[i])
                    {
                        cout << "Q ";
                    }
                    else
                    {
                        cout << ". ";
                    }
                }
                cout << endl;
            }
            break;
        }
    }
    return 0;
}