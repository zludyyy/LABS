from collections import deque
from typing import Set, Tuple, List

def miu_system(start: str, target: str, max_depth: int = 20, max_length: int = 50) -> Tuple[bool, List[str]]:
    """
    Проверяет, можно ли получить целевую строку из начальной по правилам системы MIU.
    
    Правила MIU:
    1. Если строка заканчивается на 'I', можно добавить 'U' в конец
    2. Если строка начинается с 'M', можно удвоить часть после 'M'
    3. В любой строке можно заменить любую подстроку 'III' на 'U'
    4. В любой строке можно удалить подстроку 'UU'
    """
    
    def apply_rule1(s: str) -> List[str]:
        """Правило 1: если строка заканчивается на 'I', добавить 'U'"""
        if s.endswith('I'):
            return [s + 'U']
        return []
    
    def apply_rule2(s: str) -> List[str]:
        """Правило 2: если строка начинается с 'M', удвоить часть после 'M'"""
        if s.startswith('M'):
            return [s + s[1:]]
        return []
    
    def apply_rule3(s: str) -> List[str]:
        """Правило 3: заменить любую подстроку 'III' на 'U'"""
        results = []
        for i in range(len(s) - 2):
            if s[i:i+3] == 'III':
                new_s = s[:i] + 'U' + s[i+3:]
                results.append(new_s)
        return results
    
    def apply_rule4(s: str) -> List[str]:
        """Правило 4: удалить подстроку 'UU'"""
        results = []
        for i in range(len(s) - 1):
            if s[i:i+2] == 'UU':
                new_s = s[:i] + s[i+2:]
                results.append(new_s)
        return results
    
    # Для восстановления пути
    parent = {start: None}
    
    # BFS
    queue = deque([start])
    visited = {start}
    
    while queue:
        current = queue.popleft()
        
        # Проверяем, достигли ли цели
        if current == target:
            # Восстанавливаем путь
            path = []
            node = current
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return True, path
        
        # Прекращаем поиск, если достигли максимальной глубины или длины
        if len(current) > max_length or len(parent) > 10000:
            continue
        
        # Применяем все правила и получаем новые состояния
        new_states = []
        new_states.extend(apply_rule1(current))
        new_states.extend(apply_rule2(current))
        new_states.extend(apply_rule3(current))
        new_states.extend(apply_rule4(current))
        
        for new_state in new_states:
            if new_state not in visited and len(new_state) <= max_length:
                visited.add(new_state)
                parent[new_state] = current
                queue.append(new_state)
    
    return False, []

# Проверка возможности получить MU из MI
reachable, path = miu_system("MI", "MU", max_depth=15, max_length=30)

print("Начальная строка: MI")
print("Целевая строка: MU")
print(f"Достижима: {'ДА' if reachable else 'НЕТ'}")
print()

if reachable:
    print("Путь преобразования:")
    for i, step in enumerate(path):
        print(f"{i}: {step}")
else:
    print("Невозможно получить MU из MI по правилам системы MIU.")
    print()
    print("Математическое доказательство:")
    print("1. В MI одна буква I (количество I = 1)")
    print("2. Правила изменяют количество I только следующим образом:")
    print("   - Правило 1: не меняет количество I")
    print("   - Правило 2: удваивает количество I (так как удваивает всю хвостовую часть)")
    print("   - Правило 3: уменьшает количество I на 3 (заменяет III на U)")
    print("   - Правило 4: не меняет количество I (удаляет UU)")
    print("3. Следовательно, количество I всегда имеет вид: 2^k - 3m (где k, m ≥ 0)")
    print("4. Для MU нужно количество I = 0")
    print("5. Уравнение 2^k - 3m = 0 не имеет решений в целых числах,")
    print("   так как 2^k никогда не делится на 3")
    print("6. Следовательно, получить MU из MI невозможно")