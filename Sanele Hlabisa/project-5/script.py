
commands =  """
88
1 2 E
MMLMRMMRRMML
"""


position = [0, 0]
direction = [1, 0]
X = 0
Y = 0

nesw = ['N', 'E', 'S', 'W']
nesw_direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def exec_command(cmd, line):
    global X, Y, position, direction
    if line == 0:
        X = int(cmd[1])
        Y = int(cmd[2])
    elif line == 1:
        print(f"-{cmd}-")
        if int(cmd[0]) <= X or int(cmd[2]) <= Y:
            position = [int(cmd[0]), int(cmd[2])]
            
            direction = nesw_direction[nesw.index(cmd[4])]
        else:
            print("Danger")
    elif line == 2:
        for char in cmd:
            print(position, direction)
            if char == 'M':
                position[0] += 1 * direction[0]
                position[1] += 1 * direction[1]
                #position += (1, 1) * direction 
            elif char in ['L', 'R']:
                if char == 'R':
                    direction = nesw_direction[(nesw_direction.index(direction) + 1) % len(nesw_direction)]
                else:
                    direction = nesw_direction[(nesw_direction.index(direction) + 3) % len(nesw_direction)]
            
                #direction = nesw_direction[nesw.index(char)]
        
                   
    
        
    

line_count = 0

command_line = ""

for char in commands:
    if char =='\n':
        if command_line != "":
            print("exec ", command_line, len(command_line), line_count)
            exec_command(command_line, line_count)
            line_count += 1
            command_line = ""
            continue
    command_line += char
        
        