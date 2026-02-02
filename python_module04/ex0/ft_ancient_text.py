print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print("Accessing Storage Vault: ancient_fragment.txt")

try:
    file = open("ancient_fragment.txt", "r")
except:
    print("ERROR: Storage vault not found. Run data generator first.")
else:
    print("Connection established...")
    print("RECOVERED DATA:")
    data = file.read()
    print(data, end="")
    file.close()
    print("\nData recovery complete. Storage unit disconnected.")
