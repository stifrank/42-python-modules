def ft_ancient_text() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    print("Accessing Storage Vault: ancient_fragment.txt")

    try:
        file = open("ancient_fragment.txt", "r")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print("Connection established...")
    print()
    print("RECOVERED DATA:")

    try:
        data = file.read()
        print(data)
    finally:
        file.close()

    print()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    ft_ancient_text()
