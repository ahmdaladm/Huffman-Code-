import compress

def read_frequencies_from_file(file_path):
    file_path = frequencies_file_path
    frequencies = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    symbol, frequency = line.strip().split()
                    frequencies[chr(int(symbol))] = int(frequency)
                except ValueError:
                    print(f"Ignoring invalid line: {line}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    return frequencies

# Function to decode the encoded text using Huffman tree
def decode_text(compressed_file_path,frequencies_file_path):
    frequencies = read_frequencies_from_file(frequencies_file_path)
    node_list = compress.create_sorted_node_list(frequencies)
    huffman_tree = compress.build_huffman_tree(node_list)
    encoded_text = ""
    file = open(compressed_file_path, 'r')
    encoded_text = file.read()
    decoded_text = ""
    current_node = huffman_tree

    for string in encoded_text:
        if string == '0':
            current_node = current_node['left']
        elif string == '1':
            current_node = current_node['right']
        if 'left' not in current_node and 'right' not in current_node:
            decoded_text += str(current_node['symbol'])
            current_node = huffman_tree

    return decoded_text

# لا تغيير بعد هذا السطر
compressed_file_path = 'compressed_text.txt'
frequencies_file_path = 'frequencies.txt'
decoded_text = decode_text(compressed_file_path, frequencies_file_path)
print('Decompressed text:', decoded_text)

