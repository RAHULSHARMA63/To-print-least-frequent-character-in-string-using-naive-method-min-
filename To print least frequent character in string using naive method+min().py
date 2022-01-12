test_str = "mississippi"

print ("The original string is : " + test_str)

all_freq = {}
for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1
res = min(all_freq, key = all_freq.get)

print ("The minimum of all characters in mississippi is : " + str(res))