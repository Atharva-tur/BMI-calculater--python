print("🔥 Welcome to the Fun BMI Calculator 🔥")
print("Let's find out how fit you are! 💪\n")

try:
    height = float(input("📏 Enter your height in cm: ")) / 100  # cm to meters
    weight = float(input("⚖️ Enter your weight in kilograms: "))
except ValueError:
    print("❌ Please enter valid numbers only. No cheating! 😜")
    exit()

print(f"\n✅ Your height is: {height} m")
print(f"✅ Your weight is: {weight} kg")

a = input("\n🤔 Do you want to see your BMI? Type 'YES': ")

if a.lower() == "yes":
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    print(f"\n📊 Your BMI is: {bmi}")

    # Category logic
    if bmi < 18.5:
        print("🟡 You are Underweight. Time to eat some laddoos! 🍛")
    elif 18.5 <= bmi < 24.9:
        print("🟢 You are Fit and Healthy! Keep it up champ! 💪")
    elif 25 <= bmi < 29.9:
        print("🟠 You are Overweight. Let's go for a walk! 🚶‍♂️")
    else:
        print("🔴 You are Obese. Health is wealth, time to act! ❤️‍🔥")

else:
    print("😅 Alright! Maybe next time. Stay healthy! 🌿")