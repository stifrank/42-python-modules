import importlib
import sys


REQUIRED_PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_dependencies() -> bool:
    print("Checking dependencies:")

    all_available = True

    for package, description in REQUIRED_PACKAGES.items():
        try:
            module = importlib.import_module(package)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {package} ({version}) - {description}")
        except ImportError:
            all_available = False
            print(f"[MISSING] {package} - Not installed")

    return all_available


def show_installation_help() -> None:
    print("Missing programs detected.")
    print("Install dependencies with pip:")
    print("pip install -r requirements.txt")
    print("Or install dependencies with Poetry:")
    print("poetry install")


def analyze_matrix_data() -> None:
    numpy = importlib.import_module("numpy")
    pandas = importlib.import_module("pandas")
    pyplot = importlib.import_module("matplotlib.pyplot")

    print("Analyzing Matrix data...")

    matrix_signal = numpy.random.randint(0, 100, size=1000)
    anomaly_score = numpy.random.normal(50, 15, size=1000)

    data_frame = pandas.DataFrame({
        "matrix_signal": matrix_signal,
        "anomaly_score": anomaly_score,
    })

    print(f"Processing {len(data_frame)} data points...")
    print("Generating visualization...\n")

    data_frame["anomaly_score"].plot(
        kind="hist",
        title="Matrix anomaly score distribution",
    )

    pyplot.xlabel("Anomaly score")
    pyplot.ylabel("Frequency")
    pyplot.savefig("matrix_analysis.png")
    pyplot.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if not check_dependencies():
        show_installation_help()
        sys.exit(1)

    print()
    analyze_matrix_data()


if __name__ == "__main__":
    main()
