P = float(input("Principal: "))
R = float(input("Rate of Interest: "))
T = float(input("Time (years): "))

SI = (P * R * T) / 100
print(f"Simple Interest: ₹{SI}")

CI = P * (1 + R/100)**T - P
print(f"Compound Interest: ₹{CI:.2f}")
