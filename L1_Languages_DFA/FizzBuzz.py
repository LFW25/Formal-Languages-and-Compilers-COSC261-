divisors = [3, 5, 7]
words = ["Fizz", "Buzz", "Piss"]
max_range = 100

for i in range(max_range):
    output_word = ""
    for j in range(len(divisors)):
        if i % divisors[j] == 0:
            output_word += words[j]

    if output_word == "":
        output_word += str(i)

    print(output_word)
