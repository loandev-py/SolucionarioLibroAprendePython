# ************
# ELLA QUÍMICA
# ************


def run(formula: list) -> bool:
    # TU CÓDIGO AQUÍ
    formula = set(formula)
    
    # Regla 1: Componentes 1 y 2 no pueden estar juntos
    if 1 in formula and 2 in formula:
        return False
        
    # Regla 2: Componentes 3 y 4 no pueden estar juntos
    if 3 in formula and 4 in formula:
        return False
        
    # Regla 3: Componentes 5 y 6 deben estar juntos
    if (5 in formula) != (6 in formula):
        return False
        
    # Regla 4: Debe estar el 7 o el 8 o ambos
    if 7 not in formula and 8 not in formula:
        return False
    
    return True
    

if __name__ == '__main__':
    run([1, 3, 7])