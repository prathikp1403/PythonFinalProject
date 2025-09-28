#!/usr/bin/env python3
import argparse
from ddgs import DDGS   # pip install ddgs

def google_search(query, num_results=10):
    with DDGS() as ddgs:
        return list(ddgs.text(query, max_results=num_results))

def main():
    parser = argparse.ArgumentParser(description="Search from the command line")
    parser.add_argument("query", help="Search query")
    parser.add_argument("-n", "--num", type=int, default=10,
                        help="Number of results (default: 10)")
    
    args = parser.parse_args()

    results = google_search(args.query, args.num)
    print(f"\nTop {len(results)} results for: {args.query}\n")
    for i, r in enumerate(results, 1):
        print(f"{i}. {r['title']} → {r['href']}")

if __name__ == "__main__":
    main()
