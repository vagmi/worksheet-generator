from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import random

def generate_sheet(filename, title, problems, operation):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    c.setFont("Helvetica-Bold", 20)
    c.drawString(200, height - 50, title)
    c.setFont("Helvetica", 16)
    
    x_offset = 50
    y_offset = height - 100
    line_height = 25
    
    for i, (num1, num2) in enumerate(problems):
        if i % 3 == 0 and i != 0:
            y_offset -= line_height * 4
        
        # Draw the first number right-aligned
        num1_str = f"{num1:>4}"  # Right align with width of 4
        c.drawRightString(x_offset + (i % 3) * 200 + 60, y_offset, num1_str)
        
        # Draw the operator
        op_symbol = '+' if operation == '+' else ('-' if operation == '-' else '×')
        c.drawString(x_offset + (i % 3) * 200 + 80, y_offset - line_height/2, op_symbol)
        
        # Draw the second number right-aligned
        num2_str = f"{num2:>4}"  # Right align with width of 4
        c.drawRightString(x_offset + (i % 3) * 200 + 60, y_offset - line_height, num2_str)
        
        # Draw the line
        c.line(x_offset + (i % 3) * 200, y_offset - line_height - 10, 
               x_offset + (i % 3) * 200 + 60, y_offset - line_height - 10)
    
    c.save()

def generate_problems(operation, count=20, num_range=(1, 20)):
    problems = []
    for _ in range(count):
        num1 = random.randint(*num_range)
        num2 = random.randint(*num_range)
        
        if operation == '-':
            if num1 < num2:
                num1, num2 = num2, num1  # Ensure non-negative results for subtraction
        problems.append((num1, num2))
    return problems

# Generate worksheets
addition_problems = generate_problems('+', count=10, num_range=(10, 500))
subtraction_problems = generate_problems('-', count=10, num_range=(10, 500))
multiplication_problems = generate_problems('*', count=10, num_range=(2, 12))

generate_sheet("Grade3_Addition.pdf", "Addition Worksheet", addition_problems, '+')
generate_sheet("Grade3_Subtraction.pdf", "Subtraction Worksheet", subtraction_problems, '-')
generate_sheet("Grade3_Multiplication.pdf", "Multiplication Worksheet", multiplication_problems, '*')

print("Worksheets generated successfully!")
