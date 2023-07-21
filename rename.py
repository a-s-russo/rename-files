from pathlib import Path


def rename_files(dir, pad=2, sep='-', sub=False):
    """ Renames files to have consistent numbering (for example: 'photo-1.jpg' becomes 'photo-01.jpg') and prints the
    results of the files renamed and not renamed

    Parameters
    ----------
    dir : str
        The root directory containing files to be renamed (specify subdirectories using 'sub' parameter)
        Use a raw string when specifying
    pad : num, optional
        The amount of padding or number of leading zeros to use when renaming (default is 2)
    sep : str, optional
        The separator string to identify the filename counter suffix to be padded (default is '-')
    sub : boolean, optional
        Include all files in all subdirectories of the root directory provided (see 'dir' parameter)
    """

    # Set up directory or directories to loop through
    if sub:
        directories = Path(dir).rglob('*')
    else:
        directories = Path(dir).glob('*')

    for file in directories:

        # Only rename files
        if file.is_file():

            # Print directory
            print('DIR:', file.parent)

            # Split filename by given separator string to isolate counter
            *name, counter = file.stem.split(sep)

            # Ignore if filename is not in expected pattern
            if sep not in file.stem or counter is None or not counter.isnumeric() or len(counter) >= pad:
                print('NOT RENAMED:', file.name, '\n')
                continue

            # Rejoin filename segments before final separator string
            name = sep.join(name)

            # Add leading zeros to counter
            new_counter = counter.zfill(pad)

            # Rebuild filename using padded counter
            new_name = ''.join(name) + sep + new_counter
            new_path = file.with_stem(new_name)

            # Print results
            print('OLD:', file.name)
            print('NEW: ', new_name, file.suffix, '\n', sep='')

            # Rename file
            file.replace(new_path)
