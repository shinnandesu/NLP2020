s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s_s = s.split(" ")
target_l = [1,5,6,7,8,9,15,16,19]
answer = {}
for i, word in enumerate(s_s,1):
    if i in target_l:
        answer[i] = word[0]
    else:
        answer[i] = word[:2]

print(answer)