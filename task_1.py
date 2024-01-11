# No 1
def check_string_case(sentence):
    count = 0
    count2 = 0
    for i in sentence:
        if i == " ":
            continue
        if i == i.upper():
            count += 1
        else:
            count2 += 1
    output = f"Number of upper case characters: {count} \nNumber of lower case characters: {count2}"
    return output


sample_string = "My name is Ukpono Obott"
print(check_string_case(sample_string))


# No 2
def find_max(*args):
    return max(args)


print(find_max(8, 9, 5))


# No 3
def check_prime(n=int(input("Enter a number "))):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(n, "is not a prime number")
                break
            else:
                print(n, "is a prime number")
                break
    else:
        print(n, " is not a prime number")


check_prime()
