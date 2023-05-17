import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Differentiation')
    parser.add_argument('input', type=str, help='Input expression')
    args = parser.parse_args()

    print(args.input)
