import emoji

enabled_emoji = ["right_arrow", "upwards_button"]
memory = [0]

while True:
    command = input()
    words = list(command)
    for word in words:
        cmd = emoji.demojize(word)
        if enabled_emoji[0] in cmd:
            memory.append(0)
        if enabled_emoji[1] in cmd:
            memory[len(memory) - 1] += 1
        if "no_entry" in cmd:
            print(memory)
            exit(0)