
print("Hi user, below are formulas for 5 physics topics.")
print("Select: a, b, c, d, e")

formselect = input("Choose a formula (a/b/c/d/e): ").lower()

# ------------------- FORMULA A ------------------- #
if formselect == "a":
    print("\nFormula A is for calculating WEIGHT of a body.")
    print("Formula: W = M × G")
    print("Parameters involved: W, M, G")
    paraselect = input("Which parameter do you want to calculate? (W/M/G): ").upper()

    if paraselect == "W":
        M = float(input("Mass (M): "))
        G = float(input("Gravity (G): "))
        print("Weight (W) =", M * G)

    elif paraselect == "M":
        W = float(input("Weight (W): "))
        G = float(input("Gravity (G): "))
        print("Mass (M) =", W / G)

    elif paraselect == "G":
        W = float(input("Weight (W): "))
        M = float(input("Mass (M): "))
        print("Gravity (G) =", W / M)

    else:
        print("Invalid parameter.")

# ------------------- FORMULA B ------------------- #
elif formselect == "b":
    print("\nFormula B is for calculating ACCELERATION.")
    print("Formula: A = (V - U) / T")
    print("Parameters: A, V, U, T")

    paraselect = input("Which parameter do you want to calculate? (A/V/U/T): ").upper()

    if paraselect == "A":
        V = float(input("Final Velocity (V): "))
        U = float(input("Initial Velocity (U): "))
        T = float(input("Time (T): "))
        print("Acceleration (A) =", (V - U) / T)

    elif paraselect == "V":
        A = float(input("Acceleration (A): "))
        U = float(input("Initial Velocity (U): "))
        T = float(input("Time (T): "))
        print("Final Velocity (V) =", A * T + U)

    elif paraselect == "U":
        A = float(input("Acceleration (A): "))
        V = float(input("Final Velocity (V): "))
        T = float(input("Time (T): "))
        print("Initial Velocity (U) =", V - A * T)

    elif paraselect == "T":
        V = float(input("Final Velocity (V): "))
        U = float(input("Initial Velocity (U): "))
        A = float(input("Acceleration (A): "))
        print("Time (T) =", (V - U) / A)

    else:
        print("Invalid parameter.")

# ------------------- FORMULA C ------------------- #
elif formselect == "c":
    print("\nFormula C is Ohm's Law.")
    print("Formula: V = I × R")
    print("Parameters: V (Voltage), I (Current), R (Resistance)")

    paraselect = input("Calculate which parameter? (V/I/R): ").upper()

    if paraselect == "V":
        I = float(input("Current (I): "))
        R = float(input("Resistance (R): "))
        print("Voltage (V) =", I * R)

    elif paraselect == "I":
        V = float(input("Voltage (V): "))
        R = float(input("Resistance (R): "))
        print("Current (I) =", V / R)

    elif paraselect == "R":
        V = float(input("Voltage (V): "))
        I = float(input("Current (I): "))
        print("Resistance (R) =", V / I)

    else:
        print("Invalid parameter.")

# ------------------- FORMULA D ------------------- #
elif formselect == "d":
    print("\nFormula D is SPEED calculation.")
    print("Formula: Speed = Distance / Time")
    print("Parameters: S (Speed), D (Distance), T (Time)")

    paraselect = input("Calculate which parameter? (S/D/T): ").upper()

    if paraselect == "S":
        D = float(input("Distance (D): "))
        T = float(input("Time (T): "))
        print("Speed (S) =", D / T)

    elif paraselect == "D":
        S = float(input("Speed (S): "))
        T = float(input("Time (T): "))
        print("Distance (D) =", S * T)

    elif paraselect == "T":
        S = float(input("Speed (S): "))
        D = float(input("Distance (D): "))
        print("Time (T) =", D / S)

    else:
        print("Invalid parameter.")

# ------------------- FORMULA E ------------------- #
elif formselect == "e":
    print("\nFormula E is DENSITY calculation.")
    print("Formula: Density = Mass / Volume")
    print("Parameters: ρ (Density), M (Mass), V (Volume)")

    paraselect = input("Calculate which parameter? (P/M/V): ").upper()

    if paraselect == "P":
        M = float(input("Mass (M): "))
        V = float(input("Volume (V): "))
        print("Density (ρ) =", M / V)

    elif paraselect == "M":
        P = float(input("Density (ρ): "))
        V = float(input("Volume (V): "))
        print("Mass (M) =", P * V)

    elif paraselect == "V":
        P = float(input("Density (ρ): "))
        M = float(input("Mass (M): "))
        print("Volume (V) =", M / P)

    else:
        print("Invalid parameter.")

else:
    print("Invalid formula selection.")