def main():
    travel_log = {
        "France": ["Paris", "Lille", "Dijon"],
        "Germany": ["Stuttgart", "Berlin"],
    }
    print(travel_log["France"][1])

    nested_list = ["A", "B", ["C", "D"]]
    print(nested_list[2][1])


if __name__ == "__main__":
    main()
