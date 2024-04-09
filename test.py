def aware():
    print('Do you want to check meteor activity?', '\n', 'press 1 - yes, press 2 - no')
    if str(input()) == '1':
        print('1')
    if str(input()) == '2':
        print('press enter')
    else:
        print('press enter')
        aware()
    # return case_if_stay_go()

aware()