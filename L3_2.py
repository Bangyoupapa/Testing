responses_new = [
    [200, 201],
    [400, 401, 404],
    [500, 502, 503]
]

# 印出responses_new的每個元素
for j in range(3):
    for i in range(3):
        if j < len(responses_new[i]):
            print(responses_new[i][j])

# print(responses_new[0][0])
# print(responses_new[1][0])
# print(responses_new[2][0])
# print(responses_new[0][1])
# print(responses_new[1][1])
# print(responses_new[2][1])  
# print(responses_new[0][2])
# print(responses_new[1][2])


