using Pkg
using BenchmarkTools
n = 15000
A = rand([0, 1], n, n)
b = Array{Float64}(A)
@time begin
transpose(b)
end