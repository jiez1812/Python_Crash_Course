#string.title() = Titlecase. Each wordbegins with a capital letter.
name = "ada lovelace"
print(name.title())

#lower() and upper() convert string to lowercase and uppercase.
name = "Ada Lovelace"
print(name.lower())
print(name.upper())

#combine strings, concatenation
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

#store concatenation to compose message
message = "Hello, " + full_name.title() + "!"
print(message)