using Pkg
using BenchmarkTools
n = 15000
A = rand([0, 1], n, n)
b = Array{Float32}(A)
@time begin
inv(b)
end