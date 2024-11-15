# Artificial_Intelligence
Bu repostroy'de yapay zeka öğrenme sürecinde yazdığım küçük projeleri paylaşıyor olacağım.

BFS_find_path

[TR]
🗺️ Grid Üzerinde Breadth-First Search (BFS) Algoritması ile Yol Bulma
📋 Proje Açıklaması
Bu proje, 2 boyutlu bir grid üzerinde Breadth-First Search (BFS) algoritmasını kullanarak en kısa yolu bulmayı amaçlamaktadır. Grid, şu şekilde temsil edilir:

0 değeri, geçilebilir boş bir hücreyi ifade eder.
1 değeri, geçilemeyen bir engeli ifade eder.
Verilen bir başlangıç noktası ve hedef nokta arasında, BFS algoritması grid'i tarayarak başlangıçtan hedefe en kısa yolu bulur.

🚀 Özellikler
BFS algoritmasını kullanarak en kısa yolu bulur.
Grid üzerindeki tüm yönleri (yukarı, aşağı, sol, sağ) tarar.
Engelleri etkili bir şekilde kontrol ederek 1 ile işaretlenmiş hücreleri geçmez.
Bulunan yolu adım adım başlangıçtan hedefe kadar listeler.
🧩 Örnek

Girdi Grid:
[0, 1, 0, 0, 1, 0, 0]
[0, 1, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0]
Başlangıç: (0, 0)
Hedef: (0, 6)

Çıktı:
Çözüm bulundu!
Tam yol:
Adım 0: (0, 0)
Adım 1: (1, 0)
Adım 2: (2, 0)
Adım 3: (2, 1)
Adım 4: (2, 2)
Adım 5: (2, 3)
Adım 6: (3, 3)
Adım 7: (4, 3)
Adım 8: (4, 4)
Adım 9: (4, 5)
Adım 10: (3, 5)
Adım 11: (2, 5)
Adım 12: (1, 5)
Adım 13: (0, 5)
Adım 14: (0, 6)
Toplam adım sayısı: 15 (başlangıç noktası dahil)

[ENG]
🗺️ Breadth-First Search (BFS) Pathfinding Algorithm in a Grid
📋 Project Description
This project implements a Breadth-First Search (BFS) algorithm to find the shortest path in a 2D grid. The grid is represented by a matrix where:

0 denotes a free cell that can be traversed.
1 denotes an obstacle that cannot be crossed.
Given a starting point and a goal point, the BFS algorithm explores the grid to find the shortest path from the start to the goal, if one exists.

🚀 Features
Uses the BFS algorithm to ensure the shortest path is found.
Explores all possible directions (up, down, left, right) in the grid.
Returns the path as a sequence of steps from the starting point to the goal.
Handles obstacles effectively by avoiding cells marked with 1.
🧩 Example

Input Grid:
[0, 1, 0, 0, 1, 0, 0]
[0, 1, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0]

Start: (0, 0)
Goal: (0, 6)

Output:
Solution found!
Complete path:
Step 0: (0, 0)
Step 1: (1, 0)
Step 2: (2, 0)
Step 3: (2, 1)
Step 4: (2, 2)
Step 5: (2, 3)
Step 6: (3, 3)
Step 7: (4, 3)
Step 8: (4, 4)
Step 9: (4, 5)
Step 10: (3, 5)
Step 11: (2, 5)
Step 12: (1, 5)
Step 13: (0, 5)
Step 14: (0, 6)
Total steps: 15 (including the starting point)
