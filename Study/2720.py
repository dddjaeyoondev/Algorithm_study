quarter = 25
dime = 10
nickel = 5
penny = 1

T = int(input())

for i in range(T):
    dollar = int(input())

    quarters_count = dollar // quarter
    dollar %= quarter

    dimes_count = dollar // dime
    dollar %= dime

    nickels_count = dollar // nickel
    dollar %= nickel

    pennis_count = dollar // penny

    print(quarters_count, dimes_count, nickels_count, pennis_count)
