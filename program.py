# Data muatan 
items = [
    {"nama": "Semen", "berat": 15, "nilai": 75},
    {"nama": "Baja Ringan", "berat": 4, "nilai": 40},
    {"nama": "Beras", "berat": 11, "nilai": 90},
    {"nama": "Pupuk", "berat": 5, "nilai": 50},
    {"nama": "Gula", "berat": 3, "nilai": 30},
    {"nama": "Minyak Goreng", "berat": 2, "nilai": 24},
    {"nama": "Elektronik", "berat": 6, "nilai": 65},
    {"nama": "Tekstil", "berat": 4, "nilai": 38},
    {"nama": "Kayu Olahan", "berat": 13, "nilai": 85},
    {"nama": "Suku Cadang", "berat": 3, "nilai": 35}
]

kapasitas_maks = 10
n = len(items)

max_profit = 0
best_combination = []

def knapsack_backtracking(index, current_weight, current_profit, selected_items):
    global max_profit, best_combination

    if index == n:
        if current_profit > max_profit:
            max_profit = current_profit
            best_combination = list(selected_items)
        return

    # Opsi 1: Ambil barang ke-index (x_i = 1)
    if current_weight + items[index]["berat"] <= kapasitas_maks:
        selected_items.append(items[index]["nama"])
        knapsack_backtracking(
            index + 1, 
            current_weight + items[index]["berat"], 
            current_profit + items[index]["nilai"], 
            selected_items
        )
        selected_items.pop() 

    # Opsi 2: Tidak ambil barang ke-index (x_i = 0)
    knapsack_backtracking(index + 1, current_weight, current_profit, selected_items)

knapsack_backtracking(0, 0, 0, [])

print(f"--- Solusi Optimal Knapsack (Kapasitas {kapasitas_maks} Ton) ---")
print(f"Total Keuntungan Maksimal: {max_profit} Juta Rp")
print(f"Barang yang dibawa: {', '.join(best_combination)}")