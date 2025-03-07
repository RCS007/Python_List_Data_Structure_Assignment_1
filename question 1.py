# Question 1

# Create a list of five sports. Ask the user what their favourite sport is other than the five sport already in the
# list and add this to the end of the list. Sort the list and display it. Ask the user which sport they don’t like.
# Delete the sport they have chosen from the list before you display the list again.

# Create a list of five sports
sports_list = ["Football", "Basketball", "Cricket", "Tennis", "Baseball"]

# Ask the user for their favorite sport
favorite_sport = input("What is your favorite sport that is not in the list? ")

# Add the favorite sport to the list
sports_list.append(favorite_sport)

# Sort the list
sports_list.sort()

# Display the sorted list
print("Sorted list of sports:", sports_list)

# Ask the user which sport they don't like
disliked_sport = input("Which sport don't you like? ")

# Remove the disliked sport from the list
if disliked_sport in sports_list:
    sports_list.remove(disliked_sport)
else:
    print(f"{disliked_sport} is not in the list.")

# Display the list after removal
print("Updated list of sports:", sports_list)
