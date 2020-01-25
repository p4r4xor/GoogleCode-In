#include <iostream>
#include <armadillo>
#include <bits/stdc++.h>
#include <chrono>
using namespace std::chrono;
using namespace std;
using namespace arma;

int main()
{
	//arma::mat(3,3, arma::fill::randi).print();
	mat a1 = randi<mat>(15000, 15000, distr_param(0, 1));
	auto start = high_resolution_clock::now();
	mat B = trans(a1);
	auto stop = high_resolution_clock::now();
	double time_taken = chrono::duration_cast<chrono::nanoseconds>(stop - start).count(); 
    time_taken *= 1e-9;
    cout << fixed << time_taken << setprecision(9) << "\n"; 
	//cout << a1 << endl;
	//cout << B << endl;
	return 0;
}