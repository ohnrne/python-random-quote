import random
def main():


  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  print(quotes[rnd])
  random.choice(quotes)
  print random.choice(quotes)


if __name__== "__main__":
  main()
