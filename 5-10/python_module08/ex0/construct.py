import os
import site
import sys


def is_virtual_environment() -> bool:
    return sys.prefix != sys.base_prefix


def get_environment_name() -> str:
    return os.path.basename(sys.prefix)


def get_package_path() -> str:
    package_paths = site.getsitepackages()

    if package_paths:
        return package_paths[0]
    return "Package path not available"


def show_global_environment() -> None:
    python_path = sys.executable
    venv_name = "None detected"

    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {venv_name}\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print(r"matrix_env\Scripts\activate  # On Windows")
    print()
    print("Then run this program again.")


def show_virtual_environment() -> None:
    python_path = sys.executable
    environment_name = get_environment_name()
    environment_path = sys.prefix
    package_path = get_package_path()

    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {environment_name}")
    print(f"Environment Path: {environment_path}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(package_path)


def main() -> None:
    if is_virtual_environment():
        show_virtual_environment()
    else:
        show_global_environment()


if __name__ == "__main__":
    main()
