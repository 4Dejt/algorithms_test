def check_parentheses(expr, index=0, balance=0):
    if balance < 0:
        return False  # za dużo zamykających nawiasów
    if index == len(expr):
        return balance == 0  # sprawdzenie, czy wszystkie nawiasy się zgadzają
    if expr[index] == '(':
        return check_parentheses(expr, index + 1, balance + 1)
    elif expr[index] == ')':
        return check_parentheses(expr, index + 1, balance - 1)
    else:
        return check_parentheses(expr, index + 1, balance)

# Przykład użycia
print(check_parentheses("(())"))  # True
print(check_parentheses("(()))"))  # False