import argparse
import re
import sys

import num2words
import transliterate


def translit(text):
    text_with_replaced_nums = re.sub(r'(\d+)', lambda match: num2words.num2words(match.group(0)),
                                     text)
    return transliterate.translit(text_with_replaced_nums, 'ru')


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="name of file for translation")
    parser.add_argument("-o", "--output", help="output file name")
    return parser.parse_args()


if __name__ == '__main__':
    args = get_arguments()
    source = open(args.file, 'r') if args.file else sys.stdin
    destination = open(args.output, 'w') if args.output else sys.stdout
    for line in source:
        print(translit(line), file=destination)
