def run(humanYears=int, catYears=int, dogYears=int)->int:
  if humanYears == 1:
    catYears += 15
    dogYears += 15
  elif humanYears ==2:
    catYears += 24
    dogYears += 24
  elif humanYears >=3:
    catYears=24+humanYears*4
    dogYears=24+humanYears*5
  else:
    print("ingrese un año adecuado")
  return catYears, dogYears

if __name__ == '__main__':
  print(run(5,5,5))