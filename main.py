import os
import shutil
import zipfile


def unzip(f, l):
    with zipfile.ZipFile(f, 'r') as zip_ref:
        zip_ref.extractall(l)
        zip_ref.close()


def rename(f):
    filename = os.path.basename(f)
    add_ampersand = filename.replace("___", " & ")
    remove_underscore = add_ampersand.replace("_", " ")
    remove_leading_characters = remove_underscore[remove_underscore.find("-") + 1:]
    return remove_leading_characters


if __name__ == '__main__':
    
    path = r"C:\Users\jhwin\Music\Tracks\Drum and Bass"

    for file in os.listdir(path):
        if file.endswith(".zip"):

            zip_file = file
            zip_path = os.path.join(path, zip_file)
            zip_name_no_extension = os.path.splitext(zip_file)[0]

            unzipped_dir_path = os.path.join(path, "unzipped_" + zip_name_no_extension)
            unzip(zip_path, unzipped_dir_path)

            new_dir = os.path.join(path, "renamed_" + zip_name_no_extension)
            os.mkdir(new_dir)

            for unzipped_file in os.listdir(unzipped_dir_path):
                original_path = os.path.join(unzipped_dir_path, unzipped_file)
                new_file = rename(unzipped_file)
                new_path = os.path.join(new_dir, new_file)
                shutil.copy(original_path, new_path)

            shutil.rmtree(unzipped_dir_path)
