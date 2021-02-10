import sys
from enum import Enum


''' ------- MAIN ------- '''

def main():

    args = sys.argv;
    argc = sys.argc;

    if(args[0] == Arguments.DISPLAY_CHANGES):
        command__display_changes();



if __name__ == '__main__':
    main();





''' ------- COMMANDS ------- '''

# command for logging current changes
def command__display_changes():
    changes = GitCommandLineAPI.get_changes();
    # TODO:
    # log changes onto screen with indexes





''' ------- GIT COMMAND LINE API ------- '''

class GitCommandLineAPI():

    def __init__():
        pass;

    # returns an array if all current changes and their type
    def get_changes():

        changes = [];
        # TODO:
        # write echo git status into a file
        # parse text and store intoo changes
        return changes;





''' ------- ENUMS ------- '''

# args enum
class Arguments(Enum):
    DISPLAY_CHANGES = "displayChanges";
