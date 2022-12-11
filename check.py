
def main():
    with open("data.txt") as f:
        for line in f:
            new_line = line.replace("\n", "")
            data = new_line[1:-1]
            array = [int(i) for i in data.split(',')]

            red_count = 0
            blue_count = 0
            white_count = 0
            black_count = 0
            for number in array:
                if number == 0:
                    black_count += 1
                if number == 1:
                    white_count += 1
                if number == 2:
                    blue_count += 1
                if number == 3:
                    red_count += 1

            if white_count != 7 or black_count != 1:
                print(array)

            red = red_count == 9 and blue_count == 8
            blue = red_count == 8 and blue_count == 9
            if not (red or blue):
                print(array)

if __name__ == "__main__":
    main()