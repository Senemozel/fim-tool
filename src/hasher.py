import hashlib

def calculate_hash(file_path, algorithm="sha256"):
	h = hashlib.new(algorithm)
	
	try:
		with open(file_path, "rb") as f:
			while chunk := f.read(8192):
				h.update(chunk)
		return h.hexdigest()
	except (FileNotFoundError, PermissionError) as e:
		print(f"[HATA] {file_path}: {e}")
		return None
