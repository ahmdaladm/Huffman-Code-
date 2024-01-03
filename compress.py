# Function to count the frequency of each character in the text
def count_frequencies(text):
    frequencies = {}

    for item in text:
        if item in frequencies:
            frequencies[item] += 1
        else:
            frequencies[item] = 1

    return frequencies

# Function to create a list of nodes sorted by their frequency
def create_sorted_node_list(frequencies):
    sorted_node = list(frequencies.items())
    node_list = sorted(sorted_node, key=lambda x: x[1])
    n = len(node_list)

    for i in range(n):
        result_list = [{'symbol': symbol, 'frequency': frequency} for symbol, frequency in node_list]
    node_list = result_list

    return node_list

# Function to build the Huffman tree
def build_huffman_tree(node_list):
    while len(node_list) > 1:
        node1 = node_list[0]
        node2 = node_list[1]

        node_list.remove(node1)
        node_list.remove(node2)

        parent_freq = node1['frequency'] + node2['frequency']
        parent_node = {'frequency' : parent_freq, 'left': node1, 'right': node2}
        node_list.append(parent_node)

    return node_list[0]

# Function to generate Huffman codes for each symbol
def generate_huffman_codes(node, code="", codes={}):
    if 'left' not in node:  
        if 'symbol' in node:  
            codes[node['symbol']] = code  
        return codes  

    if 'right' not in node:  
        generate_huffman_codes(node['left'], code + '0', codes)  
        return codes

    generate_huffman_codes(node['left'], code + '0', codes)  
    generate_huffman_codes(node['right'], code + '1', codes)

    return codes  

# Function to encode the text using Huffman codes
def encode_text(text, codes):
    encoded_text =""
    for string in text:
        if string in codes:
            encoded_text += codes[string]
    return encoded_text

# Function to save the encoded text and Huffman tree to files
def compress_and_save(input_file_path, output_file_path, frequencies_file_path):
    input_file = open(input_file_path, 'r')
    text = input_file.read()
    input_file.close()

    frequencies = count_frequencies(text)
    frequencies_file = open(frequencies_file_path, 'w')
    for string, freq in frequencies.items():
        frequencies_file.write(f"{ord(string)} {freq}\n")
    frequencies_file.close()

    node_list = create_sorted_node_list(frequencies)
    huffman_tree = build_huffman_tree(node_list)

    codes = generate_huffman_codes(huffman_tree)
    encoded_text = encode_text(text, codes)
    encoded_file = open(output_file_path, 'w')
    encoded_file.write(encoded_text)
    encoded_file.close()


# لا تغيير بعد هذا السطر
input_file_path = 'input.txt'
output_file_path = 'compressed_text.txt'
frequencies_file_path = 'frequencies.txt'
compress_and_save(input_file_path, output_file_path, frequencies_file_path)

