import sys
from data_analysis import load_data, daily_cases

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 testing.py <function>")
        sys.exit(1)

    function = sys.argv[1]

    try:
        if function == "load_data":
            filename = input("Input filename: ")
            print(load_data(filename))
        elif function == "daily_cases":
            filename = input("Input filename: ")
            data = load_data(filename)  # Load the data first
            print(daily_cases(data))
        else:
            print(f"Unknown function: {function}")
    except Exception as e:
        print(f"Error: {e}")
    # except Exception:
    #     traceback.print_exc()