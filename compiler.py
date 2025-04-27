import emoji
import readchar

enabled_emoji = ["right_arrow", "upwards_button", "downwards_button", "left_arrow", "outbox_tray", "repeat_button", ":END_arrow:", "inbox_tray"]
math_operations = ["plus", "minus", "multiply", "divide", "heavy_equals_sign"]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
memory = [0]
pos = 0
flag = True

num = ""
while True:
    command = input()
    words = list(command)
    for word in words:
        cmd = emoji.demojize(word)
        if enabled_emoji[0] in cmd:
            if pos == len(memory) - 1:
                memory.append(0)
            pos += 1
        if enabled_emoji[1] in cmd:
            memory[pos] += 1
        if enabled_emoji[2] in cmd:
            memory[pos] -= 1
        if enabled_emoji[3] in cmd:
            if pos > 0:
                pos -= 1
            else:
                memory.insert(0,0)
        if enabled_emoji[4] in cmd:
            print(chr(memory[pos]))
        if enabled_emoji[7] in cmd:
            ch = readchar.readchar()
            memory[pos] = ord(ch)
        if cmd in numbers:
            num += cmd
        if math_operations[0] in cmd:
            try:
                num = int(num)
            except ValueError:
                num = 0
            memory[pos] = int(num)
            num = ""
            if (words.index(word)  != len(words) - 1):
                words = words[words.index(word):]
                for i in range(len(words)):
                    if words[i] in numbers:
                        num += words[i]
                memory[pos] += int(num)        
        if math_operations[1] in cmd:
            try:
                num = int(num)
            except ValueError:
                num = 0
            memory[pos] = int(num)
            num = ""
            if (words.index(word)  != len(words) - 1):
                words = words[words.index(word):]
                for i in range(len(words)):
                    if words[i] in numbers:
                        num += words[i]
                memory[pos] -= int(num)
        if math_operations[2] in cmd:
            try:
                num = int(num)
            except ValueError:
                num = 0
            memory[pos] = int(num)
            num = ""
            if (words.index(word)  != len(words) - 1):
                words = words[words.index(word):]
                for i in range(len(words)):
                    if words[i] in numbers:
                        num += words[i]
                memory[pos] *= int(num)
        if math_operations[3] in cmd:
            try:
                num = int(num)
            except ValueError:
                num = 0
            memory[pos] = int(num)
            num = ""
            if (words.index(word)  != len(words) - 1):
                words = words[words.index(word):]
                for i in range(len(words)):
                    if words[i] in numbers:
                        num += words[i] 
                if int(num) == 0:
                    pass   
                else:
                    memory[pos] //= int(num)
        if math_operations[4] in cmd:
            print(memory[pos])
        if enabled_emoji[5] in cmd:
            words = words[words.index(word) + 1:]
            while memory[pos] != 0:
                if emoji.emojize(enabled_emoji[6]) in words:
                    flag = False
                if flag and len(words) == 0:
                    command = input()
                    w = list(command)
                    words += [e for e in w]
                else:
                    for word in words:
                        cmd = emoji.demojize(word)
                        if enabled_emoji[0] in cmd:
                            if pos == len(memory) - 1:
                                memory.append(0)
                            pos += 1
                        if enabled_emoji[1] in cmd:
                            memory[pos] += 1
                        if enabled_emoji[2] in cmd:
                            memory[pos] -= 1
                        if enabled_emoji[3] in cmd:
                            if pos > 0:
                                pos -= 1
                            else:
                                memory.insert(0,0)
                        if enabled_emoji[4] in cmd:
                            print(chr(memory[pos]))
                        if enabled_emoji[7] in cmd:
                            ch = readchar.readchar()
                            memory[pos] = ord(ch)
                        if cmd in numbers:
                            num += cmd
                        if math_operations[0] in cmd:
                            try:
                                num = int(num)
                            except ValueError:
                                num = 0
                            memory[pos] = int(num)
                            num = ""
                            if (words.index(word)  != len(words) - 1):
                                words = words[words.index(word):]
                                for i in range(len(words)):
                                    if words[i] in numbers:
                                        num += words[i]
                                memory[pos] += int(num)        
                        if math_operations[1] in cmd:
                            try:
                                num = int(num)
                            except ValueError:
                                num = 0
                            memory[pos] = int(num)
                            num = ""
                            if (words.index(word)  != len(words) - 1):
                                words = words[words.index(word):]
                                for i in range(len(words)):
                                    if words[i] in numbers:
                                        num += words[i]
                                memory[pos] -= int(num)
                        if math_operations[2] in cmd:
                            try:
                                num = int(num)
                            except ValueError:
                                num = 0
                            memory[pos] = int(num)
                            num = ""
                            if (words.index(word)  != len(words) - 1):
                                words = words[words.index(word):]
                                for i in range(len(words)):
                                    if words[i] in numbers:
                                        num += words[i]
                                memory[pos] *= int(num)
                        if math_operations[3] in cmd:
                            try:
                                num = int(num)
                            except ValueError:
                                num = 0
                            memory[pos] = int(num)
                            num = ""
                            if (words.index(word)  != len(words) - 1):
                                words = words[words.index(word):]
                                for i in range(len(words)):
                                    if words[i] in numbers:
                                        num += words[i]    
                                if int(num) == 0:
                                    pass   
                                else:
                                    memory[pos] //= int(num)
                        if math_operations[4] in cmd:
                            print(memory[pos])
        if "no_entry" in cmd:
            print(memory)
            exit(0)