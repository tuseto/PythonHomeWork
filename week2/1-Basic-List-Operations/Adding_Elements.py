languages = ["Python", "Ruby"]
print(languages)

languages = languages + ["C++", "java", "C#"]
print(languages)

languages = ["Haskell"] + languages
print(languages)

languages = languages + ["Go"]
print(languages)

print(languages[0])
print(languages[1])
print(languages[4])

languages[5] = ["F#"]
print(languages)

print(languages[len(languages)-1])

is_in = "Haskell" in languages
print("Haskell is in: " + str(is_in))

is_in = "Ruby" in languages
print("Ruby is in: " + str(is_in))

is_in = "Go" in languages
print("Go is in: " + str(is_in))

is_in = "Rust" in languages
print("Rust is in: " + str(is_in))
