import os

def local_param(location, offset, space, pins, io_order='default'):
    local_msg  = "\n\t({}\n\t\t(locals\n".format(location)
    local_msg += "\t\t\tio_order={}\n\t\t\toffset={}\n\t\t\tspace={}\n\t\t)\n".\
                  format(io_order, offset, space)
    
    for key in pins:
        if pins[key] == 1:
            local_msg += "\t\t(pin name=\"{}\" layer=2 width=2.6 depth=2.6)\n".\
                          format(key)
        elif pins[key] > 1:
            for i in range(pins[key]):
                local_msg += "\t\t(pin name=\"{}[{}]\" layer=2 width=2.6 depth=2.6)\n".\
                              format(key, i)
    local_msg += "\t)"

    return local_msg

def read_piname(location):
    piname = (input(location + " pin names : ")).split()
    pin_info = {}
    for i in range(len(piname)):
        name = piname[i]
        local_msg = "number of " + name + " : "
        pin_info[name] = int(input(local_msg))
    
    return pin_info

msg =  "===== FPGA module.ioc generator =====\n"
msg += "===== Following the instructions ====\n"
msg += "===== to compelet the .ioc file. ====\n"

print(msg)

module_name = input("module name : ")

top_pins = read_piname('top')
top_offset, top_space = input("Set top offset & space : ").split()

right_pins = read_piname('right')
right_offset, right_space = input("Set right offset & space : ").split()

left_pins = read_piname('left')
left_offset, left_space = input("Set left offset & space : ").split()

bottom_pins = read_piname('bottom')
bottom_offset, bottom_space = input("Set bottom offset & space : ").split()

iocfile = open((module_name + ".ioc"), 'w')
iocfile.write("(globals\n\tversion=3\n\tio_order=default\n\toffset=10\n\tsapce=40\n)\n\n(iopin")
iocfile.write(local_param('top', top_offset, top_space, top_pins))
iocfile.write(local_param('right', right_offset, right_space, right_pins))
iocfile.write(local_param('left', left_offset, left_space, left_pins))
iocfile.write(local_param('bottom', bottom_offset, bottom_space, bottom_pins))
iocfile.write("\n)")
iocfile.close()

print("\nmodule_name : {}\n".format(module_name))
input("Press Enter to continue...")
