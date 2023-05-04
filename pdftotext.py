import argparse
import re
import unicodedata
from pdfminer.high_level import extract_text

# Create an ArgumentParser object
parser = argparse.ArgumentParser(description='Extract text from a PDF file and save it to a text file.')

# Add arguments for input and output file names
parser.add_argument('input_file', help='Path to input PDF file')
parser.add_argument('output_file', help='Path to output text file')

# Parse the command-line arguments
args = parser.parse_args()

# Extract text from input PDF file
text_output = extract_text(args.input_file)

# Remove unicode characters from text
text_output = unicodedata.normalize('NFKD', text_output).encode('ascii', 'ignore').decode('utf-8')

# Replace lines with no words with an empty line
lines = text_output.split('\n')
lines = [line.strip() if any(word.isalpha() for word in line.split()) else '\n' for line in lines]
text_output = '\n'.join(lines)

# Remove trailing spaces from text
# text_output = text.rstrip()

# Remove lines with less than 3 characters from text
lines = text_output.split('\n')
lines = [line.strip() for line in lines if len(line.strip()) > 3]
text_output = '\n'.join(lines)

# Merge double empty lines in text
# lines = text_output.split('\n')
# merged_lines = []
# for i in range(len(lines)):
#     if not lines[i].strip() and i > 0 and not lines[i-1].strip():
#         continue
#     merged_lines.append(lines[i])
# merged_lines = [re.sub(r'\s{2,}', ' ', line) for line in merged_lines]
# text_output = '\n'.join(merged_lines)

# Remove empty brackets from text
pattern = r'\(\s*\)'
text_output = re.sub(pattern, '', text_output)

# Add empty line before and after lines with "HADIS" followed by a number
hadis_lines = []
for line in text_output.split('\n'):
    if re.match(r'HADIS\s+\d+', line):
        hadis_lines.append('')
        hadis_lines.append('<|endoftext|>')
        hadis_lines.append(line)
        hadis_lines.append('')
    else:
        hadis_lines.append(re.sub(r'\s{2,}', ' ', line))
text_output = '\n'.join(hadis_lines)

# Save extracted text to output file
with open(args.output_file, 'w', encoding='utf-8') as f:
    f.write(text_output)

# Print confirmation message
print(f'Text extracted from "{args.input_file}" and saved to "{args.output_file}"')
