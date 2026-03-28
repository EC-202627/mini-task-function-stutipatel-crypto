def calculate_fine(book_title, days_overdue, daily_rate=5.0, max_fine=150.0):
    fine = days_overdue * daily_rate
    if fine > max_fine:
        fine = max_fine
    return fine


# Take inputs separately
book_title = input()   # waits for title
days = int(input())    # waits for days

fine = calculate_fine(book_title, days)

print(f"Book: {book_title}")
print(f"Days overdue: {days}")
print(f"Fine: Rs. {fine}")
