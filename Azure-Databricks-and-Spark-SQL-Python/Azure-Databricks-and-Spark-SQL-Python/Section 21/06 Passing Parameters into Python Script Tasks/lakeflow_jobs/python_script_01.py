import sys

script_name = sys.argv[0] # Its reserved by default, will always give script name

persons_name = sys.argv[1]

workspace_id = sys.argv[2]

print(sys.argv)

print(f"The script name is: {script_name}")

print(f"The persons name is: {persons_name}")

print(f"The workspace id is: {workspace_id}")
