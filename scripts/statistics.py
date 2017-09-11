import shelve

data = shelve.open("user_data.shelve", writeback=True)
data["counter"] = len(data["unique"].keys())
print(data)
data.close()