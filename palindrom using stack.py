n = input("ENTER  STRING\n")
length = int(len(n))

for i in range(0, int(length/2 + 1)):
   if n[i] == n[-i - 1]:
      i += 1
   else:
      break
if i < (length / 2):
   print("not")
else:
   print("yes")
