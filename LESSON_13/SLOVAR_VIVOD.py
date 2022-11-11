



V = {
    'C:' : {
        'A': ['file_1', 'file_2'],
        'B': ['file_3', 'file_4'],
        'C': ['file_5','file_6']
        },
    'D:' : {
        'J': ['file_7', 'filt_8'],
        'K': ['file_9', 'filt_10'],
        'L': ['file_11', 'filt_12']

        }

    }


def get_files(path, depth=0):
    for f in path:
        print(" " *depth, f)
        if type(path[f]) == dict:
            get_files(path[f], depth+1)
        else:
            print(" "*(depth+1), " ".join(path[f]))

get_files(V)
