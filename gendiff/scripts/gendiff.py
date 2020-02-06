#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=int)
    parser.add_argument('second_file', type=int)
    parser.add_argument('-f', '--format', type=int)
    args = parser.parse_args()


if __name__ == '__main__':
    main()
