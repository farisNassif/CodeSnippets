def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print (complaint)
ask_ok('Prompt 1: Do you really want to quit?')
ask_ok('Prompt 2: OK to overwrite the file?', 1)
ask_ok('Prompt 3: OK to overwrite the file?', 2, 'Come on, only yes or no!(TEST)')