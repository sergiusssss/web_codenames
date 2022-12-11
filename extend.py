import numpy as np

def main():
    result_arrays = []

    with open("data.txt") as f:
        for line in f:
            new_line = line.replace("\n", "")
            data = new_line[1:-1]
            reqdy_data = [int(i) for i in data.split(',')]

            array = np.array(reqdy_data)
            matrix = array.reshape(5, 5)

            m90 = np.rot90(matrix, k=1, axes=(1,0))
            m180 = np.rot90(matrix, k=2, axes=(1,0))
            m270 = np.rot90(matrix, k=3, axes=(1,0))

            result_arrays.append(matrix.reshape(-1).tolist())
            result_arrays.append(m90.reshape(-1).tolist())
            result_arrays.append(m180.reshape(-1).tolist())
            result_arrays.append(m270.reshape(-1).tolist())

    with open("extended_data.txt", 'w') as f:
        print(result_arrays)
        for array in result_arrays:
            line = ",".join(str(item) for item in array)
            line = "[" + line + "]\n"
            print(line)
            f.write(line)

if __name__ == "__main__":
    main()