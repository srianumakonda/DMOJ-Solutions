inputs = list(map(int, input().split()))
start = inputs[0]
count = inputs[1]
value = 2
out = [0 for i in range(35)]
out[start-1] = 1

while value<=count:
  out[start] = value
  value += 1
  start+=1

out = ["  "+str(i) if i<10 else " "+str(i) for i in out ]
# for i in range(6, len(out), 7):
#   out[i] = out[i]+"."


reshaped_output = [out[i:i+7] for i in range(0, len(out), 7)] #return list at every 7th intervals
del_idx = 0
for i in range(len(reshaped_output[4])):
  if " 0" in reshaped_output[4][i]:
    del_idx+=1
for i in range(del_idx):
  reshaped_output[4].pop(-1)

print("Sun Mon Tue Wed Thr Fri Sat")
for week in range(len(reshaped_output)-1):
  for day in range(len(reshaped_output[0])):
    if " 0" in reshaped_output[week][day]:
      reshaped_output[week][day] = "   "

  print(*reshaped_output[week])
print(*reshaped_output[-1])

# print(reshaped_output)