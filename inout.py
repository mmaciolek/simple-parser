class InOut:
    def __init__(self):
        self.input_file_path = None
        self.output_file_path = None
        self.input_file_text = None

    def take_file_path(self, path, file_type):
        # receive file path for input or output file
        if file_type == 0:
            self.input_file_path = path
        elif file_type == 1:
            self.output_file_path = path
        else:
            print("File path error.")

    def read_input_file(self):
        # read lines from input file
        f = open(self.input_file_path, "r", encoding="utf-8")
        text = f.readlines()
        lines = list()
        # clean lines of line breaks and add to list of lines
        for line in text:
            lines.append(line.replace('\n', ''))
        # join the cleaned lines into input_file_text
        self.input_file_text = str.join(' ', lines)
        f.close()

    def write_lines_to_output_file(self, to_write):
        # open or create output file based on file path
        f = open(self.output_file_path, "a", encoding='utf-8')
        # write lines to output file, putting each line on a new line
        for line in to_write:
            f.write(f"{line}\n")
        f.close()
