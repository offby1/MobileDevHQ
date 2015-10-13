def factorial (x)
  if x < 2 then
    return 1
  end
  product = 1
  while (x > 1)
    product *= x
    x -= 1
  end
  return product
end

# Test like this:
# ruby factorial.rb hey you 1 2 3 5 10 20 50 69
ARGV.each do |i|
  printf "%s => %d => %d\n", i, i.to_i, factorial(i.to_i)
end
