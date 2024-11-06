import argparse

parser = argparse.ArgumentParser(description="Mitt krypteringverktyg")

parser.add_argument("name", help ="Ange ditt namn")
parser.add_argument("age", type=int, help="Ange din ålder")

parser.add_argument("--v", action="store_true", help="Visa mer information") ## --v = behövs ej den info

args = parser.parse_args()

print(f"Hej {args.name}")
