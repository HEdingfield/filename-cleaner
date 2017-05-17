from fc import filename_cleaner
import time

start_time = time.time()
folder = r"/home/username/test"
bad_chars = '\/*?:"<>|'
replacement_char = "_"
clean_type = "both"
actually_rename = False

filename_cleaner(folder, bad_chars, replacement_char, clean_type, actually_rename)

end_time = time.time()
print("Finished in " + str(round(end_time - start_time, 3)) + " seconds.")
