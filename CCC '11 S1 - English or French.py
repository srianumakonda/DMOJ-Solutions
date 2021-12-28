text = ""
s_count = 0
t_count = 0
for i in range(int(input())):
  text += input().lower()

for letter in text:
  if "t" in letter:
    t_count+=1
  elif "s" in letter:
    s_count += 1

if t_count>s_count:
  print("English")
else:
  print("French")