from fc import filename_cleaner
import time

start_time = time.time()
folder = r"C:\temp\fctest"
clean_types = ["dirs", "files"]
bad_chars = '_-@'
replacement_char = "_"
actually_rename = False

for clean_type in clean_types:
    filename_cleaner(folder, clean_type, bad_chars, replacement_char, actually_rename)

end_time = time.time()
print("Finished in " + str(round(end_time - start_time, 3)) + " seconds.")
