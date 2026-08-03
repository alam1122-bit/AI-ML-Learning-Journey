friends = ["A","B"]

def find_setting(seated,remaining):
  if (len(remaining)< 1):
    print(seated)
    return
  for i in range (len(remaining)):
    print(len(remaining))
    # 0-2 remaining[0] = "A"
    new_seated = seated + [remaining[i]] # [] + ["A"] = ["A"]
    new_remaining = remaining[:i] + remaining[i+1:] # ["B"]
    find_setting(new_seated,new_remaining) # ["A"], ["B"]

find_setting([],friends)
