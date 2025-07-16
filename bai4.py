n = int(input("Nhập n: "))

is_prime = True

if n < 2:
  is_prime = False
else:
  for i in range(2,  int(n ** 0.5) + 1):
    if(n % i == 0):
      is_prime = False

if is_prime:
  print(n,"là số nguyên tố")
else:
  print(n,"không phải số nguyên tố")