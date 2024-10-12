process_time_latest = [385, 400, 395, 375, 401]

user_input = input("Enter the process time: ")
n = input("前n名通過: ")
process_time_latest.append(int(user_input))
process_time_latest.sort()
index = process_time_latest.index(int(user_input))
n = int(n)
if index < n:
    print("Pass")
else:
    print("Fail")