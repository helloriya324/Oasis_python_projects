def calculate_bmi(weight, height):
  """Calculates the Body Mass Index (BMI) for a given weight and height.

  Args:
      weight: Weight in kilograms (float).
      height: Height in meters (float).

  Returns:
      The calculated BMI (float).
  """
  bmi = weight / (height * height)
  return bmi

def classify_bmi(bmi):
  """Classifies the BMI into a weight category.

  Args:
      bmi: The calculated Body Mass Index (float).

  Returns:
      A string representing the weight category (e.g., "Underweight", "Normal").
  """
  if bmi < 18.5:
    return "Underweight"
  elif bmi < 25:
    return "Normal"
  elif bmi < 30:
    return "Overweight"
  else:
    return "Obese"

def main():
  """Prompts the user for weight and height, calculates BMI, and displays results."""
  try:
    weight = float(input("Enter your weight in kilograms (kg): "))
    height = float(input("Enter your height in meters (m): "))

    if weight <= 0 or height <= 0:
      raise ValueError("Weight and height must be positive values.")

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {category}")
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()