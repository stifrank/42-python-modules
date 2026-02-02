print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")


def handle_crisis(filename, routine):
    if routine:
        print(f"ROUTINE ACCESS: Attempting access to '{filename}'...")
    else:
        print(f"CRISIS ALERT: Attempting access to '{filename}'...")

    try:
        with open(filename, "r") as file:
            data = file.read()
            # El ejemplo enseña que en éxito se imprime una parte del contenido
            print(f"SUCCESS: Archive recovered - ``{data.strip()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print("RESPONSE: Unexpected anomaly detected")
        print("STATUS: Crisis contained, system stable")


handle_crisis("lost_archive.txt", routine=False)
handle_crisis("classified_vault.txt", routine=False)
handle_crisis("standard_archive.txt", routine=True)

print("All crisis scenarios handled successfully. Archives secure.")
