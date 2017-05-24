import matplotlib.pyplot as plt
import elizabeth


with open("Revizor.txt") as book:
	text = book.read()
count_letters = dict()
for letter in text:
	letter = letter.upper()
	if ord(letter) > 90 and letter.isalpha():
		if letter not in count_letters.keys():
			count_letters[letter] = 1
		else:
			count_letters[letter] += 1
fig = plt.figure()
pair = list(count_letters.items())
pair.sort(key=lambda x: x[0])
letters = [pair[i][0] for i in range(len(pair))]
count = [pair[i][1] for i in range(len(pair))]
colors = [elizabeth.Text('en').color().lower() for i in range(1, 33)]
left = [i for i in range(1, 33)]
plt.bar(left, height=count, color=colors, tick_label=letters, align='center')
plt.show()