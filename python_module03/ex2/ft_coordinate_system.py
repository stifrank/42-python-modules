import math

print("=== Game Coordinate System ===")

# 1) Posición fija (demo simple)
position = (10, 20, 5)
print(f"Position created: {position}")

# 2) Distancia 3D
origin = (0, 0, 0)
dx = position[0] - origin[0]
dy = position[1] - origin[1]
dz = position[2] - origin[2]
dist = math.sqrt(dx * dx + dy * dy + dz * dz)
print(f"Distance between {origin} and {position}: {dist:.2f}")

# 3) Parsear coordenadas válidas
coord_str = "3,4,0"
print(f'Parsing coordinates: "{coord_str}"')

parts = coord_str.split(",")
parsed = (int(parts[0]), int(parts[1]), int(parts[2]))
print(f"Parsed position: {parsed}")

dx = parsed[0] - origin[0]
dy = parsed[1] - origin[1]
dz = parsed[2] - origin[2]
dist = math.sqrt(dx * dx + dy * dy + dz * dz)
print(f"Distance between {origin} and {parsed}: {dist}")

# 4) Parsear coordenadas inválidas con try/except
bad_str = "abc,def,ghi"
print(f'Parsing invalid coordinates: "{bad_str}"')

try:
    parts = bad_str.split(",")
    bad_pos = (int(parts[0]), int(parts[1]), int(parts[2]))
    print(f"Parsed position: {bad_pos}")
except ValueError as e:
    print(f"Error parsing coordinates: {e}")
    print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

# 5) Unpacking demonstration
print("Unpacking demonstration:")
x, y, z = parsed
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
