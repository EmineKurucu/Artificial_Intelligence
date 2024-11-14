# Node class'ını oluşturuyoruz
from collections import deque

class Node:
    
    def __init__(self, state, parent = None):
        self.state = state # düğümün ismi / state'i
        self.parent = parent # düğümün hangi düğümden geldiğini tutar
        
    # çözüm yolunu geri izlemek için:
    def path(self): # hedefe ulaşıldığında başlangoçtan hedefe kadar olan yolu tutar
        node , path_back = self, [] # yol bir liste A -> C -> F gibi
        while node:
            path_back.append(node.state) # Geçilen node'ü yola ekliyoruz şu ankinden başlangıca doğru gider
            node = node.parent
        return list(reversed(path_back)) # yolu ters çevirdik
        
        
# Problem sınıfı       

class Problem:
    def __init__(self, initial, goal, graph):
        self.initial = initial
        self.goal = goal
        self.graph = graph  # graph yapısı komşuluk listesi
        
        
    def is_goal(self, state):
        return state == self.goal
    
    def expand(self, node): # düğüm komşularını genişletir ve her komşuya node üretir
        return [Node(state, node) for state in self.graph[node.state]]
    
    
def breadth_first_search(problem):
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node
    
    frontier = deque([node]) #BFS algoritması keşdefilecek düğümleri queue(FIFO) yapısında tutar
    reached = {problem.initial} #ziyaret edilmiş durumlardan set oluşturur
    
    while frontier: # queue boşalana kadar
        node = frontier.popleft() # queue yapısının başından alır (FIFO)
        
        # genişletme ve hedef kontrolü
        for child in problem.expand(node): # mevcut node'ün komşu düğümlerini çağırır
            s = child.state 
            
            if problem.is_goal(s):
                return child
            
            if s not in reached:
                reached.add(s)
                frontier.append(child)
            
    return None

def main():
    graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
    }
    
    problem = Problem("A", "F", graph) # başlandıç node A aranan node F + ağaç yapısı
    
    solution = breadth_first_search(problem)
    
    if solution:
        print("Solution found ", "-> ".join(solution.path()))
    else:
        print("Solution has not found.")
        
if __name__ == "__main__":
    main()
    
# çıktı : Solution found  A-> C-> F
    
                
        
    
    
    
        