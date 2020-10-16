import uncompyle6
import os, fnmatch


def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


if __name__ == '__main__':
    path = '/Users/janghanbin/Downloads/SJVA2-master/SJVA2-master/lib/'
    for filename in find_files(path, '*.pyo'):
        pure_name = filename[:-4]
        # print(pure_name)
        with open('{0}.py'.format(pure_name), 'w') as f:
            try:
                uncompyle6.decompile_file(filename, f)
                print('{0}.py Saved!'.format(pure_name))

            except Exception as e:
                print(e)
                print('failed to save {0}.py'.format(pure_name))


