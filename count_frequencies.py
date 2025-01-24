freqdict = {}

with open("alice.txt", encoding="utf-8") as fin:
	for line in fin:
		line = line.strip().split(" ")
		for token in line:
			if not token in freqdict:
				freqdict[token] = 0

			freqdict[token] = freqdict[token] + 1

for token, frequency in freqdict.items():
	if frequency == 1:
		print(f"{token}\t{frequency}")