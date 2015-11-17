# Returns a random integer between the numbers 0 and 10, inclusive.
num = random.randint(0, 10)

# Sometimes, when we generate a random sequence, we want it to be the same sequence whenever the program is run.
# An example is when you use random numbers to select a subset of the data, and you want other people
# looking at the same data to get the same subset.
# We can ensure this by setting a random seed.
# A random seed is an integer that is used to "seed" a random number generator.
# After a random seed is set, the numbers generated after will follow the same sequence.
random.seed(10)
print([random.randint(0,10) for _ in range(5)])
# => [9, 0, 6, 7, 9]
random.seed(10)
# Same sequence as above.
print([random.randint(0,10) for _ in range(5)])
# => [9, 0, 6, 7, 9]
random.seed(11)
# Different seed means different sequence.
print([random.randint(0,10) for _ in range(5)])
# => [7, 8, 7, 7, 8]
random.seed(20)
print([random.randint(0,10) for _ in range(10)])
# => [10, 2, 4, 10, 10, 1, 5, 9, 2, 0]
random.seed(20)
print([random.randint(0,10) for _ in range(5)])
# => [10, 2, 4, 10, 10]

# % Selecting Items for a list %
shopping = [300, 200, 100, 600, 20]
# We want to sample the data, and only select 4 elements.
random.seed(1)
shopping_sample = random.sample(shopping, 4)


## probability
# Number of combinations formula
# N!/(k!(N-k)!
# In this formula, N is the total number of events we have,
# and k is the target number of times we want our desired outcome to occur.
# So if we wanted to find the number of combinations in which 4 out of 5 days can be sunny,
# we'd set N to 5, and k to 4.

# prob of it being sunny = 0.7
# prob of not being sunny = 0.3
# find probability that 3 days are sunny out of 5 days
def number_of_combinations(N, k):
    return math.factorial(N) / ( math.factorial(k) * math.factorial(N - k) )

prob_combination_3 = number_of_combinations(5, 3) * ( 0.7 * 0.7 * 0.7 * 0.3 * 0.3 )
