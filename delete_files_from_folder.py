"""
    Name:             delete_files_from_folder.py
    Purpose:          Delete all the files from the directory and sub-directories
    Usage:            python delete_files_from_folder.py <source>
    Author:           Rohan Nagalkar
    Created:          23/06/2016
    Version:         0.1              Rohan Nagalkar     Created.
"""

import os
import sys


def usage():
    """
        Usage of the process
    :return:
    """
    print """
            Usage : python delete_files_from_folder.py <path/to/directory>
          """
    return True

def main():
    """
        Main

    :return: True on success else False
    """
    if len(sys.argv) != 2:
        usage()
        return False

    directory = sys.argv[1]

    for root_dir, subfolders, files in os.walk(directory):
        if len(files) > 0:
            for dir_file in files:
                print "Deleting : %s" % os.path.join(root_dir, dir_file)
                os.remove(os.path.join(root_dir, dir_file))
        else:
            print "%s is empty." % root_dir

    return True


if __name__ == '__main__':
    main()
