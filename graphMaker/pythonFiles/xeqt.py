import graphFileParser
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file', required=True,
        help='Update file name, for help with format look at multiGraphFileExample')

args = parser.parse_args()

a = graphFileParser.MultiGraph(args.file)

a.construct()

a.createBook()
