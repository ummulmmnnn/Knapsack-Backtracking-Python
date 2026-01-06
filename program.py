items = [
    {"nama": "Semen", "berat": 3, "nilai": 25},
    {"nama": "Baja Ringan", "berat": 4, "nilai": 40},
    {"nama": "Beras", "berat": 2, "nilai": 20},
    {"nama": "Pupuk", "berat": 5, "nilai": 50},
    {"nama": "Gula", "berat": 3, "nilai": 30},
    {"nama": "Minyak Goreng", "berat": 2, "nilai": 24},
    {"nama": "Elektronik", "berat": 6, "nilai": 65},
    {"nama": "Tekstil", "berat": 4, "nilai": 38},
    {"nama": "Kayu Olahan", "berat": 5, "nilai": 45},
    {"nama": "Suku Cadang", "berat": 3, "nilai": 35}
]

kapasitas_maks = 15 
n = len(items)

max_profit = 0
best_combination = []
total_weight_optimal = 0

def knapsack_backtracking(index, current_weight, current_profit, selected_items):
    global max_profit, best_combination, total_weight_optimal

    if index == n:
        if current_profit > max_profit:
            max_profit = current_profit
            total_weight_optimal = current_weight
            best_combination = list(selected_items)
        return

    if current_weight + items[index]["berat"] <= kapasitas_maks:
        selected_items.append(items[index]["nama"])
        knapsack_backtracking(
            index + 1, 
            current_weight + items[index]["berat"], 
            current_profit + items[index]["nilai"], 
            selected_items
        )
        selected_items.pop()

    knapsack_backtracking(index + 1, current_weight, current_profit, selected_items)

knapsack_backtracking(0, 0, 0, [])

print(f"Nilai maksimum : {max_profit} juta Rp")
print(f"Daftar item terpilih : {', '.join(best_combination)}")
print(f"Total berat : {total_weight_optimal} ton")
