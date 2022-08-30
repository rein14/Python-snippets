def compound_interest(principal, rate, time, n_times):
    digits = 1 + rate / n_times
    ci = principal * (pow(digits, time))
    return ci

ci = compound_interest(2000, 0.02, 20,100)
print(ci)
