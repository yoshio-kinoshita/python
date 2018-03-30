words = ['cat', 'dog', 'bird']

for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 3:
        words.insert(0, w)

print(words)