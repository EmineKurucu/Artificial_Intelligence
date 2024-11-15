from collections import deque

class gridProblem:
    def __init__(self, initial_state, goal_state, grid):
        self.initial_state = initial_state # başlangıç koordinatı (0,0)
        self.goal_state = goal_state # bitiş koordinatı (0, 6)
        self.grid = grid # iki boyutlu matris yapısı 0'lar boş 1'ler engel
        
    def is_goal(self, state):
        return state == self.goal_state # bulunulan konum hedef konum ise
        #bulunulan konumu hedefe eşitler
        
    def is_valid_cell(self, row, col):
        return 0<= row < len(self.grid) and 0 <= col < len(self.grid[0]) and self.grid[row][col] == 0
    # bulunulan row,col verilen grid yapısının içinde mi ve engel var mı (0 da engel yok)
    
    def expand(self, node):
        # mevcut düğümün 4 komşu hücresini kontrol edecek ve geçerli komşu düğümleri oluşturacak
        row , col = node.state 
        children = []
        
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_row , new_col = row + dr , col + dc
            
            if self.is_valid_cell(new_row, new_col): # child geçerli mi kontrol ettik 
                child_state = (new_row, new_col) # yeni bilgileri ekledik
                child_node = Node(child_state, parent=node) # child node olarak eklendi 
                children.append(child_node)
                
        return children
            
        
class Node:
    
    def __init__(self, state, parent=None, action=None):
        self.state = state # node'un bulunduğu koordinat
        self.parent = parent # bulunulan node'ün geldiği önceki node
        self.action = action # bulunulan node'a ne hareketl gelindi
        
    
def breadth_first_search(problem):
    node = Node(problem.initial_state)
    
    if problem.is_goal(node.state):
        return node
    
    frontier = deque([node]) # aranacak node'ları tutan bir queue (FIFO) yapısı oluşturduk
    reached = {problem.initial_state} # ziyaret edilen Node'ları saklayan küme(set)
    
    while frontier: # Node var oldukça
        node = frontier.popleft()
        
        for child in problem.expand(node): # nodun çevresine bakıyoruz
            state = child.state 
            
            if problem.is_goal(state): # aranan düğüm bakılan komşuysa
                return child
            
            if state not in reached:
                reached.add(state) # ziyaret edilenlere eklendi
                frontier.append(child) # queue(FIFO) yapısına eklendi
                
    return None  # queue boşalırsa None döner

def reconstruct_path(node): # hedef düğümden başlangıç düğüme giderek path'i oluşturur
    path = []
    
    while node:
        path.append(node.state) # nodun konumunu path'e ekledi
        node = node.parent  
    
    return list(reversed(path))

def print_complete_path(path):
    if path:
        for step, point in enumerate(path):
            print("Step {} : {}".format(step, point))
            
    else:
        print("No solution found.")
    
    
def main():
    grid = [
    [0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0]
    
    ] # 0'lar boş 1'lerde engel var
    
    initial_state = (0,0)
    goal_state = (0,6)
    
    # problemi tanımlıyoruz
    problem = gridProblem(initial_state, goal_state, grid)
    
    solution_node = breadth_first_search(problem)

    if solution_node:
        print("Solution found!")
        solution_path = reconstruct_path(solution_node)
        print("Complete path : ")
        print_complete_path(solution_path)
        
    else:
        print("Solution has not found!")
        
if __name__ == "__main__":
    main()
