og_message = input("Type a sentence to reverse: ")
words = og_message.split()
reversed_message = words[::-1]
final_result = " ".join(reversed_message)
print("\nHere is your reversed sentence:")
print(final_result)