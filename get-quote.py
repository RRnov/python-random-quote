import random

def captain():
  #print("Keep it logically awesome.")
  f = open("quotes.txt", "a")
  f.write("Woah there boyo, you added me??\n")
  f.close()

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)
  print(quotes[rnd], end='')
  print(quotes[rnd2], end='')

if __name__== "__main__":
  captain()
