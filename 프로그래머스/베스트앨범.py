genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

genre_set = list(set(genres))
playing_nums = [0 for _ in range(len(genre_set))]

for idx in range(len(genres)):
    playing_idx = genre_set.index(genres[idx])
    playing_nums[playing_idx] += plays[idx]


print(genre_set)
print(playing_idx)
print(playing_nums)