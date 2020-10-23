import sys

def read_lines(filename):
    file = open(filename,"r")
    lines = file.readlines()
    file.close()
    return lines

def get_identifiers(header):
    identifiers = header
    identifiers = identifiers.rstrip('\n').rstrip('\r')
    identifiers = identifiers.split(',')
    identifiers = identifiers[1::]
    return identifiers


def main(filename):
    lines = read_lines(filename)
    identifiers = get_identifiers(lines[0])
    lines = lines[1::]
    print('File: ' + filename)

    for line in lines:
        line = line.rstrip('\n').rstrip('\r')
        line = line.split(',')
        key = line[0]
        for i in range(0,len(identifiers)):
            print(key+';'+identifiers[i]+';'+line[i+1])

if __name__ == '__main__':
    main(sys.argv[1])
