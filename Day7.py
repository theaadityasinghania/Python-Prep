# Functions and python modules.

# print("Hello World")

# def myprint(txt):
#     print(txt)

# myprint("Hello Aaditya Singhania")

# msg_template = """
# Hello {}, Thanks for subscribing to my channel {}.
# """

# def format_msg(a,b):
#     print(msg_template.format(a,b))

# format_msg("Aaditya Singhania","AOPF")

msg_template = """
Hello {}, Thanks for subscribing to my channel {}.
"""

def format_msg(a,b):
    return msg_template.format(a,b)