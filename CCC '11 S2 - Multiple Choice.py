length = int(input())
responses = []
answers = []
for i in range(length):
  responses.append(str(input()))
for i in range(length):
  answers.append(str(input()))

correct = sum([i==j for i, j in zip(responses, answers)])
print(correct)