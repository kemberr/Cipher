phonetics = ["Alpha","Bravo","Charlie","Delta","Echo","Foxtrot","Golf","Hotel","India",
             "Juliet","Kilo","Lima","Mike","November","Oscar","Papa","Quebec","Romeo",
             "Sierra","Tango","Uniform","Victor","Whiskey","X-Ray","Yankee","Zulu"]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
               "n","o","p","q","r","s","t","u","v","w","x","y","z"]
check_value = dict(zip(alphabet, phonetics)) # {'a': 'Alpha', 'b': 'Bravo', 'c': 'Charlie'......
newlist = []
i = 0
# l == the leter
# i == index number of letter
word = input("Please enter your word:\n")
for alphabet, phonetics in check_value.items():
    if i == len(word):
        break
    for l in alphabet:
        if l == word[i]:
            newlist.append(check_value[word[i]])
        else:
            newlist.append(check_value[word[i]])
        i += 1

print(" ".join(newlist))