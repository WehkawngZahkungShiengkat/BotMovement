class BotMovementAction:
    directions = ["North", "East", "South", "West"]
    move_val = {"North": [0,1], "East": [1,0], "South": [0,-1], "West": [-1,0]}
    def __init__(self, dirc="North", x=0, y=0):
        self.current_direction = dirc
        self.current_x_pos = x
        self.current_y_pos = y

    def get_string(self):
        print(f"X: {self.current_x_pos} Y: {self.current_y_pos} Direction: {self.current_direction}")

    def do_actions(self, action_str):
        action_list = [char for char in action_str]
        while len(action_list):
            action_list = self.one_action_aat(action_list)
        pass

    def one_action_aat(self, split_str) -> list:
        take_action = split_str.pop(0)
        print(take_action)
        if take_action in ["R", "L"]:
            print("Turn RL")
            self.turn(take_action)
        elif take_action == "W":
            print("Move by W")
            take_action = split_str.pop(0) if split_str[0] else take_action
            while split_str and split_str[0].isdigit():
                take_action += split_str.pop(0)
            print(take_action)
            self.move(take_action)
        elif take_action.isdigit():
            print("in isdigit")
            while split_str and split_str[0].isdigit():
                take_action += split_str.pop(0)
            self.move(take_action)
        else:
            print("Invalid command -", take_action)
        return split_str

    def turn(self, command):
        turn_action = {"R": 1, "L": -1}
        current_dirc_idx = self.directions.index(self.current_direction)
        new_dirc = self.directions[(current_dirc_idx % (len(self.directions)-1)) + turn_action[command]]
        self.current_direction = new_dirc

    def move(self, command):
        try:
            steps = [val * int(command) for val in self.move_val[self.current_direction]]
            self.current_x_pos += steps[0]
            self.current_y_pos += steps[1]
        except Exception as e:
            print(e)

if __name__=='__main__':
    import sys
    bot = BotMovementAction()
    bot.get_string()
    # bot.do_actions("RRW10W1")
    get_input = sys.argv
    print("get_input -",get_input)
    if len(get_input)>1:
        get_input.pop(0)
        for each in get_input:
            bot.do_actions(each)
            bot.get_string()
    else:
        get_input = input("Enter command to move the bot(LR to turn and W+number to move): ")
        bot.do_actions(get_input)
        bot.get_string()