#include <bits/stdc++.h>
using namespace std;

int main()
{
	int n;
	int count1 = 0;
	int count2 = 0;
	cin >> n;
	vector <int> a, b;
	for(int i=1; i*i <= n; i++)
	{
		if(n % i == 0)
		{
			a.push_back(i);
			count1 += 1;
			if(n/i != i)
			{
				count2 += 1;
				b.push_back(n/i);
			}
		}
	}
	for(auto i: a)
	{
		cout << i << " ";
	}
	reverse(b.begin(), b.end());
	for(auto i: b)
	{
		cout << i << " ";
	}
	cout << endl;
	cout << count1+count2 << "\n";
	return 0;
}