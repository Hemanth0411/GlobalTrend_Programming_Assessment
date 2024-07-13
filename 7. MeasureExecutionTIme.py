import time

def measure_time(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    exec_time = end_time - start_time
    print(f"Function {func.__name__} took {exec_time:.6f} seconds to complete execution")
    return result
  return wrapper

@measure_time
def fibonacci(n):
  if n<0:
    print("Enter a positive integer!!")
  elif n==0:
    return 0
  elif n==1 or n==2:
    return 1
  else:
    a, b = 0, 1
    for i in range(2, n):
      a, b = b, a + b
    return b
  

result = fibonacci(12)

print(f"The {n}th fibonacci sequence is {result}")