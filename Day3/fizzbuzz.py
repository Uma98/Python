for fizzbuzz in range(25):
    if fizzbuzz != 0:
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
          print("FizzBuzz")                                        
        elif fizzbuzz % 3 == 0:    
          print("Fizz")                                        
        elif fizzbuzz % 5 == 0:        
          print("Buzz")
        else:
          print(fizzbuzz)                                    
