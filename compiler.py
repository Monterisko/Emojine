import emoji

enabled_emoji = ["right_arrow", "upwards_button", "downwards_button", "left_arrow", "inbox_tray", "repeat_button", "END_arrow"]
memory = [0]
pos = 0
flag = True

while True:
    command = input()
    words = list(command)
    for word in words:
        cmd = emoji.demojize(word)
        if enabled_emoji[0] in cmd:
            memory.append(0)
            pos += 1
        if enabled_emoji[1] in cmd:
            memory[pos] += 1
        if enabled_emoji[2] in cmd:
            memory[pos] -= 1
        if enabled_emoji[3] in cmd:
            if pos > 0:
                pos -= 1
        if enabled_emoji[4] in cmd:
            print(chr(memory[pos]))
        if enabled_emoji[5] in cmd:
            words = []
            while memory[pos] > 0:
                if emoji.emojize(enabled_emoji[6]) in words:
                    flag = False
                if flag:
                    command = input()
                    w = list(command)
                    words += [e for e in w]
                
                else:
                    for word in words:
                        cmd = emoji.demojize(word)
                        if enabled_emoji[0] in cmd:
                            memory.append(0)
                            pos += 1
                        if enabled_emoji[1] in cmd:
                            memory[pos] += 1
                        if enabled_emoji[2] in cmd:
                            memory[pos] -= 1
                        if enabled_emoji[3] in cmd:
                            if pos > 0:
                                pos -= 1
                        if enabled_emoji[4] in cmd:
                            print(chr(memory[pos]))

        if "no_entry" in cmd:
            print(memory)
            exit(0)