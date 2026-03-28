
def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate

    if fine > max_fine:
        return max_fine, True   # exceeded
    else:
        return fine, False      # not exceeded


# Input (line by line)
book_title = input()
days = int(input())

# Function call
fine, exceeded = calculate_fine(book_title, days)

# Output
print(f"Book: {book_title}")
print(f"Days overdue: {days}")
print(f"Fine: Rs. {fine}")

# Extra message
if exceeded:
    print("You have accumulated the maximum fine of INR: 150.0")