'''
3. A spam comment is defined as a text containing following keywords: “Make a lot of
money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.
'''

text = input("Enter text: ").casefold()

if("make a lot of money" in text or "buy now" in text or "subscribe this" in text or "click this" in text):
    print("SPAM DETECTED!")
else:
    print("SPAM NOT DETECTED!")