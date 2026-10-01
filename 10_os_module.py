

#* OS Module in Python

# The `os` module lets Python talk to the underlying operating system:
# navigating/creating/removing files and folders, reading environment
# variables, running shell commands, inspecting file metadata, etc.
# It's part of the standard library - no pip install needed.

#* Why it matters for data engineering specifically
    # - Pipelines constantly read from and write to folders full of files
    #   (raw data drops, staging areas, output/export folders) - os lets
    #   you list, filter, and organize those files programmatically.
    # - os.walk() is the standard way to recursively scan a directory
    #   tree, e.g. finding every .csv/.json/.parquet file under a
    #   "data/" folder no matter how deeply nested.
    # - Config and secrets (DB passwords, API keys, S3 bucket names) are
    #   commonly passed to pipelines via environment variables, read with
    #   os.environ / os.getenv() - this is the standard way to avoid
    #   hardcoding secrets in code.
    # - File metadata (os.stat: size, last-modified time) is used to
    #   detect new/changed files before reprocessing them, or to skip
    #   empty files.
    # - Building output paths in a way that works on both Linux
    #   (production servers) and Windows/Mac (your laptop) requires
    #   os.path.join instead of manually concatenating strings with "/".


import os


#* Current directory & basic navigation
print(f"Current working directory: {os.getcwd()}")
# os.chdir(path) would change the working directory - commented out
# since it would affect every relative path below.

# List everything (files + folders) directly inside a directory
print(f"Contents of cwd: {os.listdir(os.getcwd())}")


#* os.path - path building & inspection
# Always prefer os.path.join over manually gluing strings with "/" -
# it uses the correct separator for the OS ("/" on Linux/Mac, "\" on
# Windows), which matters when a pipeline runs on different machines.
sample_path = os.path.join(os.getcwd(), "os_practice_sandbox", "data.csv")
print(f"Joined path: {sample_path}")

print(f"Absolute path of this script: {os.path.abspath(__file__)}")
print(f"Directory name: {os.path.dirname(sample_path)}")
print(f"Base name (file part): {os.path.basename(sample_path)}")
print(f"Split extension: {os.path.splitext(sample_path)}")  # -> ('.../data', '.csv')
print(f"Does it exist yet? {os.path.exists(sample_path)}")


#* Environment variables
# Used constantly in data pipelines to inject config/secrets without
# hardcoding them - e.g. database URLs, API tokens, environment name
# (dev/staging/prod), file paths that differ per deployment.
print(f"HOME env var: {os.getenv('HOME')}")
# os.getenv returns None (or a default) instead of raising if missing -
# safer than os.environ["KEY"], which raises KeyError if not set.
print(f"Missing env var with default: {os.getenv('SOME_PIPELINE_CONFIG', 'default_value')}")
# os.environ["MY_KEY"] = "value"   # sets an env var for this process (and subprocesses it spawns)


#* Creating directories & files - sandbox setup
# Everything below operates inside this sandbox folder so it's obvious
# what got created and safe to delete at any time.
SANDBOX = os.path.join(os.getcwd(), "os_practice_sandbox")

# os.mkdir() creates ONE directory and fails if the parent doesn't
# exist, or if the folder already exists. os.makedirs() creates any
# missing parent folders too, and exist_ok=True stops it erroring if
# it's already there - the safer default for pipeline code that might
# run more than once.
os.makedirs(SANDBOX, exist_ok=True)
os.makedirs(os.path.join(SANDBOX, "raw"), exist_ok=True)
os.makedirs(os.path.join(SANDBOX, "processed"), exist_ok=True)

# Create a few sample "data" files so we have something to scan below.
# (Plain file writing isn't part of `os`, but it's how a pipeline would
# actually produce the files os is then used to manage.)
sample_files = {
    os.path.join(SANDBOX, "raw", "sales_2024.csv"): "id,amount\n1,100\n2,200\n",
    os.path.join(SANDBOX, "raw", "customers.json"): '{"id": 1, "name": "Alice"}',
    os.path.join(SANDBOX, "raw", "readme.txt"): "just a notes file, not real data",
}
for file_path, content in sample_files.items():
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write(content)


#* Checking file vs directory
for item in os.listdir(SANDBOX):
    item_path = os.path.join(SANDBOX, item)
    if os.path.isfile(item_path):
        print(f"{item} is a file")
    elif os.path.isdir(item_path):
        print(f"{item} is a directory")
    else:
        print(f"{item} is neither a file nor a directory")


#* os.walk() - recursively scan a directory tree
# Yields (current_dir_path, [subdirectories], [files]) for every folder
# in the tree, starting at the given root. This is THE standard way to
# find every data file under a folder, no matter how deeply nested -
# e.g. "find every .csv under data/" for a batch ingestion job.
print("\nWalking the sandbox tree:")
for dirpath, dirnames, filenames in os.walk(SANDBOX):
    for filename in filenames:
        full_path = os.path.join(dirpath, filename)
        print(f"  found: {full_path}")


#* Filtering files by extension (a common data engineering task -
# e.g. "only process the CSVs, ignore everything else")
csv_files = []
for dirpath, dirnames, filenames in os.walk(SANDBOX):
    for filename in filenames:
        if filename.endswith(".csv"):
            csv_files.append(os.path.join(dirpath, filename))
print(f"\nCSV files found: {csv_files}")


#* File metadata with os.stat()
# Useful for pipelines that need to decide whether a file is new/changed
# since the last run, or whether to skip suspiciously empty files.
for file_path in csv_files:
    stats = os.stat(file_path)
    print(
        f"\n{os.path.basename(file_path)} -> "
        f"size: {stats.st_size} bytes, "
        f"last modified (epoch): {stats.st_mtime}"
    )
# os.path.getsize(path) is a shortcut for stats.st_size if that's all you need.


#* Renaming / moving files
# os.rename(src, dst) also works as a "move" if src and dst are in
# different directories - this is how a pipeline marks a file as
# processed, e.g. moving it from raw/ to processed/ after ingestion.
src = os.path.join(SANDBOX, "raw", "sales_2024.csv")
dst = os.path.join(SANDBOX, "processed", "sales_2024.csv")
if os.path.exists(src):
    os.rename(src, dst)
    print(f"\nMoved {src} -> {dst}")


#* Deleting files & directories
    # os.remove(path)  - deletes a single FILE
    # os.rmdir(path)   - deletes a directory, but ONLY if it's empty
    # shutil.rmtree(path) - deletes a directory AND everything inside it
    #                       (not part of `os`, but the standard pairing
    #                       for "delete this whole folder recursively")
# Example (commented out so re-running this script doesn't wipe the
# sandbox - uncomment to try it):
# os.remove(os.path.join(SANDBOX, "raw", "readme.txt"))
# import shutil; shutil.rmtree(SANDBOX)


#* A couple more useful ones
    # os.path.isabs(path)      - True if path is absolute, not relative
    # os.path.normpath(path)   - cleans up ".." and "./" in a path
    # os.listdir(path)         - non-recursive, one level only (unlike os.walk)
    # os.cpu_count()           - number of CPUs available, useful when
    #                             deciding how many parallel worker
    #                             processes to spin up for a data job
    # os.system(command)       - runs a shell command (subprocess module
    #                             is generally preferred nowadays - it's
    #                             safer and gives you the command's output)

print(
    f"\nNote: sample files were created under {SANDBOX} - "
    "safe to delete that folder any time, it's just for these examples."
)
