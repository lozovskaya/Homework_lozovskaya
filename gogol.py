import matplotlib.pyplot as plt


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
xdata = [0, 1, 2, 4, 5, 8]
ydata = [0.1, 0.2, 0.4, 0.8, 0.6, 0.1]
fig = plt.figure()
print(list(count_letters.keys()))
plt.bar(list(count_letters.values()), labels=list(count_letters.keys()))
plt.grid(True)   # линии вспомогательной сетки
plt.show()
'''pylab.bar(list(count_letters.keys()), list(count_letters.values()))
pylab.show()'''