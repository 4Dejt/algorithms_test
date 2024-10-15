# czy możliwe jest odważanie wagi amount za pomocą odważników z listy weights (odważniki tylko na jednej szalce)

def is_measurable(amount, weights, i):
    if i == len(weights):
        return amount == 0
    else:
        return is_measurable(amount, weights, i + 1) or is_measurable(amount - weights[i], weights, i + 1)

# czy możliwe jest odważanie wagi amount za pomocą odważników z listy weights (odważniki możliwe na dwóch szalkach)
def is_measurable2(amount, weights, i):
    if i == len(weights):
        return amount == 0
    else:
        return is_measurable2(amount, weights, i + 1) or is_measurable2(amount - weights[i], weights, i + 1) or is_measurable2(amount + weights[i], weights, i + 1)

print(is_measurable(6, [1,3,7], 0))

