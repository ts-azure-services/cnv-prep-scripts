# Analyze results script

# Input the test key
key = str(input("Enter the test key (only 'h' or 'n'):"))
if len(key) == 10:
    if key == key.lower():
        print(f"Key is: {key}")
    else:
        print("Key is not in lowercase.")
else:
    print("Length is not 10 letters.")

# Input the counters to analyze ratings
counter = 0
human_but_neural = 0
neural_but_human = 0
participant = str(input("Enter participant name: "))
a = str(input("Enter participant ratings (only 'h' or 'n'): "))
if len(a) == 10:
    if a == a.lower():
        for i in range(len(a)):
            if a[i] == key[i]:
                counter += 1
            if a[i] == 'h' and key[i] == 'n':
                human_but_neural += 1
            if a[i] == 'n' and key[i] == 'h':
                neural_but_human += 1
    else:
        print("Key is not in lowercase.")
else:
    print("Length is not 10 letters.")

accuracy = counter / len(a)
human_but_neural_score = human_but_neural / len(a)
neural_but_human_score = neural_but_human / len(a)
print(f"Accuracy: {accuracy * 100}")
print(f"Human, but actually neural: {human_but_neural_score * 100}")
print(f"Neural, but actually human: {neural_but_human_score * 100}")
