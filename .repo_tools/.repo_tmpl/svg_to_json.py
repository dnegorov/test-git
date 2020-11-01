import argparse
import json

parser = argparse.ArgumentParser(add_help=True,
                                 description="SVG to JSON")
parent_parser = argparse.ArgumentParser(add_help=False)

parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
parser.add_argument("-if", "--input",
                    help="path to input file: svg_to_json -in <FILE>")
parser.add_argument("-of", "--output",
                    help="path to output file: svg_to_json -in <IN_FILE> -of <OUT_FILE>")


args = parser.parse_args()
print(args)

in_path = None
if args.input:
    in_path = args.input

output = {}
if in_path is not None:
    print(f"Converting {in_path}")
    with open(in_path, "r") as in_file:
        lines = in_file.readlines()
        print(lines[1])
        output = {"logoSvg": "".join(lines)}

print(output)
of_path = None
if args.output:
    of_path = args.output

if of_path is not None:
    print(f"Saving to {of_path}")
    with open(of_path, "w") as of_file:
        json.dump(output, of_file)
