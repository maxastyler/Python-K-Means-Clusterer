from extractor import *
from tempfile import mkstemp
from shutil import move
from os import remove, close, path.expanduser

def replace_colours(file_path, colour_dict):
    #Create temp file
    fh, abs_path = mkstemp()
    with open(abs_path,'w') as new_file:
        with open(file_path) as old_file:
            file_lines=[]
            for line in old_file:
                stripped=line.split(':')[0]
                key_in_line=False
                for key in colour_dict:
                    if key in stripped:
                        new_line="*{0}: {1}\n".format(key, colour_dict[key])
                        key_in_line=True
                        pass
                if key_in_line: file_lines.append(new_line)
                else: file_lines.append(line)
            for line in file_lines:
                new_file.write(line)
    close(fh)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)

replace_colours(path.expanduser(str(sys.argv[1])), prepare_for_terminal(path.expanduser(str(sys.argv[2])), True))
