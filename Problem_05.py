
def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate

    if fine > max_fine:
        fine = max_fine

    return fine


# Input (line by line)
book_title = input()
days = int(input())
rate = float(input())
max_fine = float(input())

# Function call
fine = calculate_fine(book_title, days, rate, max_fine)

# Output
print(f"Book: {book_title}")
print(f"Days overdue: {days}")
print(f"Fine: Rs. {fine}")