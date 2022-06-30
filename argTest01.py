import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--area",required=True,type=int)

if __name__=="__main__":
    args = parser.parse_args()