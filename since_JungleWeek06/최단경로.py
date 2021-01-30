import sys
import heapq
sys.stdin = open("input.txt", "r")

V, E = map(int, input().split())
K = int(input())
result = []
graph = [[] for _ in range(V+1)]
heaplist = []