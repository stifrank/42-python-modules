print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols")

print("SECURE EXTRACTION:")

with open("classified_vault.txt", "r") as file:
    data = file.read()
    print(data, end="")

print("SECURE PRESERVATION:")

with open("classified_vault.txt", "a") as file:
    file.write("[CLASSIFIED] New security protocols archived\n")
    print("[CLASSIFIED] New security protocols archived")

print("Vault automatically sealed upon completion")
print("All vault operations completed with maximum security.")
