from datetime import datetime, timedelta
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--num_y", help="The number of years", type=int)
parser.add_argument("--num_d", help="The number of days", type=int)

args = parser.parse_args()
current_time = datetime.now()
print("Current date:", current_time)
if args.num_y:
    print("Given years:", args.num_y)
else:
    print("Given years: not given")
if args.num_d:
    print("Given days:", args.num_d)
else:
    print("Given days: not given")
if args.num_y and args.num_d:
    print("Final date:", current_time + timedelta(days=args.num_y*365 + args.num_d))
elif args.num_y and not args.num_d:
    print("Final date:", current_time + timedelta(days=args.num_y*365))
elif not args.num_y and args.num_d:
    print("Final date:", current_time + timedelta(args.num_d))
elif not args.num_y and not args.num_d:
    print("Final date:", current_time)