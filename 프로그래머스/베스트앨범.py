genres = ["classic","classic","classic","classic","pop"]
plays = [500,150,800,800,2500]
# [5, 1, 4, 7, 3, 0, 6]

    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)



# genre_set = list(set(genres))
# playing_nums = [0 for _ in range(len(genre_set))]
# keys = [[] for _ in range(len(genre_set))]
# temp = []
# answer = []
#
# for idx in range(len(genres)):
#     playing_idx = genre_set.index(genres[idx])
#     playing_nums[playing_idx] += plays[idx]
#     keys[playing_idx].append((plays[idx], idx))
#
#
# for list in keys:
#     list.sort(reverse=True, key = lambda x : (x[0], -x[1]))
#
# while playing_nums:
#     max_idx = playing_nums.index(max(playing_nums))
#     temp.append(keys[max_idx][:2])
#     playing_nums.pop(max_idx)
#     keys.pop(max_idx)
# print(temp)
#
# for i in range(len(temp)):
#     for val in temp[i]:
#         answer.append(val[1])
# print(answer)