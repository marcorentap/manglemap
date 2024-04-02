import sys
import subprocess

if len(sys.argv) < 2:
	print("Expected library path in argv[1]")
	exit()

lib_path = sys.argv[1]

# Get mangled and demangled symbols with nm
nm_out = subprocess.run(["nm", "--format=just-symbols", "--numeric-sort", lib_path], capture_output=True)
nm_out2 = subprocess.run(["nm", "--format=just-symbols", "--numeric-sort", "-C", lib_path], capture_output=True)
mangle_map = list(zip(nm_out.stdout.split(sep=b'\n'), nm_out2.stdout.split(sep=b'\n')))

for symbol in mangle_map:
	mangled_name = symbol[0].decode()
	demangled_name = symbol[1].decode()
	print(f"{mangled_name} {demangled_name}")
