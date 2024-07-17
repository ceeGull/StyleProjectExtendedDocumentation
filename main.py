#################################################################################
#                                 main.py                                       #
#-------------------------------------------------------------------------------#
# By             | cGull                                                        #
# Date           | August 30, 2023 (8/30/2023)                                  #
# Version        | 1                                                            #
# Source Code    | Probably will be just because there is missing documentation #
#################################################################################
# ;imports
try:
    from GF import *
except ImportError as IE:
    print(f"IMPORT ERROR: {IE}")

import pprint as pp
import re

# LIST
data = [[line for line in text] for text in [open(f"/usr/share/cOS/DES/txt/{file}", 'r').read().splitlines() for file in os.listdir("/usr/share/cOS/DES/txt")]]
data_c = [[0, 0], 0, 0, 0]
data_copy = data.copy() # ;Use this as we're going to overwrite the original
# DICT
parameters = {}
# CODE


def newline_removal(v):
    # CODE
    if v == [None, None, None]:
        return False
    elif v in ['', None]:
        return False
    return True

def create_markdown_file():
    """
    Syntax
    -------
    # Style Project Configuration (Complete)
    This is a project that attempts to replicate current and previous macOS versions' window decorations and application style, in the projects documentation though not everything is there, this project is a way to include all information

    ## General Options
    ### Opacity = 26
    _Integer_  
    in hac habitasse platea dictumst vestibulum rhoncus est pellentesque elit ullamcorper dignissim cras tincidunt lobortis feugiat vivamus at augue eget
    """
    # STR
    title = "Style Project Configuration (Complete)"
    intro_str = "This is a project that attempts to replicate current and previous macOS versions' window decorations and application style, in the projects documentation though not everything is there, this project is a way to include all information\n\nIf you want to try this window decoration go [here](https://sourceforge.net/projects/styleproject/)\n_Note: Some code in this project does some of the source code from that project here_\n_[settings.h](https://sourceforge.net/p/styleproject/code/ci/master/tree/config/settings.h)_\n_[settings.cpp](https://sourceforge.net/p/styleproject/code/ci/master/tree/config/settings.cpp)_\n"
    gradient_type_link = "https://sourceforge.net/p/styleproject/wiki/gradient/"
    # ZIP
    information = zip(data[0][:data[0].index("-")], data[1], data[2])
    # LIST
    found_parents = []
    general_exceptions = ["uno"]
    # ENUM
    shadow_options = enumerate(data[0][data[0].index("-")+1:])
    # CODE
    if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/.cache/readme.md"):
        os.remove(f"{os.path.dirname(os.path.abspath(__file__))}/.cache/readme.md")
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/.cache/readme.md", "w+") as markdown_file:
        markdown_file.write(f"# {title}\n{intro_str}\n")
        for description, defaults, key in information:
            # ;d = Description
            d_p_name = description[0]
            d_p_n_parent = d_p_name[0] if len(d_p_name) > 1 else "General"
            d_desc = description[1][0]
            d_comment = description[2]
            # ;i = default
            i_def_value = defaults[0]
            i_d_v_type = defaults[1]
            # ;Code
            if d_p_name[0] in general_exceptions:
                d_p_n_parent = d_p_name[0]
            
            if d_p_n_parent not in found_parents:
                found_parents.append(d_p_n_parent)
                markdown_file.write(f"## {d_p_n_parent} Options\n\n")
            
            if i_d_v_type == "Gradient":
                if d_comment is None:
                    markdown_file.write(f"### {key}={i_def_value}\n_{i_d_v_type}_  \n{d_desc}  \nCheck [here]({gradient_type_link}) to see how gradients work in StyleProject\n\n")
                else:
                    markdown_file.write(f"### {key}={i_def_value}\n_{i_d_v_type}_  \n{d_desc}  \n{d_comment}  \nCheck [here]({gradient_type_link}) to see how gradients work in StyleProject\n\n")
            elif i_d_v_type == "Shadow Enumerator":
                if d_comment is None:
                    markdown_file.write(f"### {key}={i_def_value}\n_{i_d_v_type}_  \n{d_desc}  \nPlease refer to Shadow Options for your choices that you can make\n\n")
                else:
                    markdown_file.write(f"### {key}={i_def_value}\n_{i_d_v_type}_  \n{d_desc}  \n{d_comment}  \nPlease refer to Shadow Options for your choices that you can make\n\n")
            elif d_comment is None:
                markdown_file.write(f"### {key}={i_def_value}\n_{i_d_v_type}_  \n{d_desc}  \n\n")
            else:
                markdown_file.write(f"### {key}={i_def_value}\n_{i_d_v_type}_  \n{d_desc}  \n{d_comment}  \n\n")
        
        markdown_file.write("## Shadow Options\n\n")
        for shadow_option in shadow_options:
            s_o_enum = shadow_option[0]
            s_o_name = shadow_option[1][0]
            s_o_desc = shadow_option[1][1][0]
            s_o_comment = shadow_option[1][2]
            
            # ;p(s_o_enum)
            # ;p(s_o_name)
            # ;p(s_o_desc)
            # ;p(s_o_comment)
            # ;p("\n")
            
            if s_o_comment is None:
                markdown_file.write(f"### {s_o_enum}={s_o_name}\n_Enum_  \n{s_o_desc}  \n\n")
            else:
                markdown_file.write(f"### {s_o_enum}={s_o_name}\n_Enum_  \n{s_o_desc}  \n{s_o_comment}  \n\n")


for line in data_copy[0][:data_copy[0].index('--=-=-=')]:
    # ;Apparently in the StyleProject's source code has some missing documented parameters
    parameter = line.rsplit("*/", maxsplit=1)
    # ;Grab the parameter name only if regular expression is not empty otherwise return None
    p_name = re.findall('[a-z.]+', parameter[0])[0] if re.findall('[a-z.]+', parameter[0]) != [] else None
    # ;Split using var above and the marker is the char "." only if p_name isn't NOP
    p_name_splitted = p_name.split(".") if p_name is not None else None
    # ;Grab the parameter document only if the length of the list has 2 indexes otherwise return None also include comments
    p_desc = parameter[1].strip()[1:].split("//") if len(parameter) == 2 else None
    if p_desc is not None:
        # ;Remove leftover C/C++ syntax
        p_desc[0] = p_desc[0].rstrip()[:-2] if p_desc[0].rstrip()[-2:] == '",' else p_desc[0].rstrip()[:-1]
    p_d_comment = p_desc[1] if p_desc is not None and len(p_desc) == 2 else None
    # ;Overwrite original data
    data[0][data[0].index(line)] = [p_name_splitted, p_desc, p_d_comment]
    data_c[0][0] += 1

for line in data_copy[0][data_copy[0].index('--=-=-='):]:
    # ;Apparently in the StyleProject's source code has more options than what's documented
    parameter = line.split(":", maxsplit=1)
    # ;Grab the name
    p_name = parameter[0][1:]
    # ;Grab the description
    p_desc = parameter[1].strip().rsplit("//", maxsplit=1) if len(parameter) == 2 else None
    # ;Remove leftover C/C++ syntax
    if p_desc is not None:
        p_desc[0] = p_desc[0][:-2] if p_desc[0][:-2] == '",' else p_desc[0][:-1]
    # ;Grab the comment if it exists
    p_d_comment = p_desc[1] if p_desc is not None and len(p_desc) == 2 else None
    # ;Case correct the first character in the string
    if p_d_comment is not None and p_d_comment[0].isupper is False:
        p_d_comment[0] = p_d_comment[0].upper()
    # ;Overwrite original data
    data[0][data[0].index(line)] = [p_name, p_desc, p_d_comment]
    data_c[0][1] += 1

# ;Overwrite seperator with a straight up string representing a seperator
data[0][data[0].index(["-=-=-=", None, None])] = "-"
# ;Remove "empty" lists
data[0] = list(filter(newline_removal, data[0]))

for line in data_copy[1]:
    # ;Remove any trailing spaces only if the line is not empty
    value = line.strip() if line != "" else None
    # ;Strip C/C++ Syntax
    value = value[:-1] if value is not None and value[-1:] == "," else value
    # ;Determine type based on given contents
    if value is not None:
        if value in ["true", "false"]:
            value_type = "Boolean"
        elif value.isnumeric():
            value_type = "Integer"
        elif value == "QString()":
            value_type = "String (Qt Based)"
        elif value == "QStringList()":
            value_type = "String List"
        elif ":" in value:
            value_type = "Gradient"
        elif value[0] and value[-1] == '"':
            value_type = "String"
            if value[1] == "#":
                value_type = "Color"
        elif value[:2] == "0x":
            value_type = "Hex"
        elif value in [p_name[0] for p_name in data[0][data[0].index("-")+1:]]:
            value_type = "Shadow Enumerator"
        else:
            value_type = "Unknown Type"
        # ;Overwrite original data
        data[1][data_c[1]] = [value, value_type]
    data_c[1] += 1

# ;Remove "empty" data
data[1] = list(filter(newline_removal, data[1]))

for line in data_copy[2]:
    # ;Remove trailing lines
    p_name = line.strip() if line != "" else None
    # ;Strip C/C++ Syntax
    if p_name is not None:
        p_name = p_name[1:-2] if p_name[-2:] == '",' else p_name[1:-1]
    # ;Overwrite data
    data[2][data_copy[2].index(line)] = p_name
    data_c[2] += 1

# ;Remove "empty" data
data[2] = list(filter(newline_removal, data[2]))

create_markdown_file()
