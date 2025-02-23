def run(x=int,y=int)->int:
  aspect1 = x*(16/9)
  aspect2 = y*(16/9)
  aspect1 = round(aspect1)
  aspect2 = round(aspect2)

  return aspect1, aspect2
  

if __name__ == '__main__':
  print(run(500,280))