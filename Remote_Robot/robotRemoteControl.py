"""Simple example showing how to get gamepad events."""
#coding utf-8

from __future__ import print_function


from inputs import get_gamepad


def main():
    """Just print out some event infomation when the gamepad is used."""
    while 1:
        events = get_gamepad()
        for event in events:
        #     print(event.ev_type)
        #     print(event.code)
        #     print(event.state)

            if event.code == 'BTN_SOUTH' and event.state == 1:
                print('A')
            if event.code == 'BTN_WEST' and event.state == 1:
                print('X')
            if event.code == 'BTN_EAST' and event.state == 1:
                print('B')
            if event.code == 'BTN_NORTH' and event.state == 1:
                print('Y')

            if event.code == 'ABS_HAT0Y' and event.state == -1:
                print('up')
            if event.code == 'ABS_HAT0Y' and event.state == 1:
                print('down')
            if event.code == 'ABS_HAT0X' and event.state == -1:
                print('left')
            if event.code == 'ABS_HAT0X' and event.state == 1:
                print('rigth')
            if event.code == 'ABS_HAT0Y' and event.state == 0:
                # print('Y_0')
                pass
            if event.code == 'ABS_HAT0X' and event.state == 0:
                # print('X_0')
                pass

            if event.code == 'BTN_TL' and event.state == 1:
                print('TL')
            if event.code == 'BTN_TR' and event.state == 1:
                print('TR')

            if event.code == 'BTN_START' and event.state == 1:
                print('start')
            if event.code == 'BTN_SELECT' and event.state == 1:
                print('select')

            if event.code == 'BTN_THUMBL' and event.state == 1:
                print('Button_Joystick_L')
            if event.code == 'BTN_THUMBR' and event.state == 1:
                print('Button_Joystick_R')

            if event.code == 'ABS_X':
                print('ABS_X : ', )



if __name__ == "__main__":
    main()
