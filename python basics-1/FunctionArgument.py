# Four types of functionarguments
#Default, Keyword, Variable length , Required
# def average(a=9,b=5):
#     def average (*numbers)-variable length




# def name(**args):
#     print(args)
#     print("Hello",args['fname'],args['mname'],args['rose'])

# name(fname='k',mname='s',rose='l')


# Generate a List of Prime Numbers up to N

# def prime_numbers(N):
#      primes = []  
#     for num in range(2, n + 1):  
#         is_prime = True
#         for i in range(2, int(num**0.5) + 1): 
#             if num % i == 0:  
#                 is_prime = False
#                 break  
#         if is_prime:  
#             primes.append(num)
#     return primes

#  Find the Second Largest Number in a List
def second_largest_num(lst):
    Unique_num=list(set(lst))
    Unique_num.sort()
    return Unique_num

second_largest_num([15,25,67,89,97])

