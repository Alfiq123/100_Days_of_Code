# Tip Calculator Project

# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))

# Solver 1
print("Selamat datang di tip kalkulator")
harga = float(input("Berapa total tagihan? Rp. "))
tip = int(input("Berapa persen tip yang akan Anda berikan? "))
orang = int(input("Berapa banyak orang yang akan membayar tagihan? "))

hitung_tip = (tip / 100) * harga
total_tagihan = harga + hitung_tip
patungan = (total_tagihan + hitung_tip) / orang

print("========================================")
print("Menghitung Tip Dari Suatu Tagihan")
print("========================================")
print(f"Total Awal: Rp. {harga:,.0f}")
print(f"Persen Tip: {tip}%")
print(f"Total Tip: Rp. {hitung_tip:,.0f}")
print("========================================")
print(f"Total Tagihan: Rp. {total_tagihan:,.0f}")
print(f"Total Tagihan Per Orang: Rp. {patungan:,.0f}")

# Solver 2
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
