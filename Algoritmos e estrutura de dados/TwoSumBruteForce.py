def TwoSum(lista, target):
  for i in range(len(lista)):
    for j in range(i+1, len(lista)):
      if (lista[i] + lista[j]) == target:
        return [i, j]
  return None
