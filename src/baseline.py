import os
import json
from datetime import datetime
from src.hasher import calculate_hash

BASELINE_FILE = "baseline/baseline.json"

def create_baseline(target_dir):
	baseline = {}
	
	for root, dirs, files in os.walk(target_dir):
		for file_name in files:
			file_path = os.path.join(root,file_name)
			file_hash = calculate_hash(file_path)
			
			if file_hash:
				baseline[file_path] = {
					"hash": file_hash,
					"size": os.path.getsize(file_path),
					"created_at": datetime.now().isoformat()
				}
	os.makedirs("baseline", exist_ok = True)
	with open(BASELINE_FILE, "w") as f:
		json.dump(baseline, f, indent=4)
	
	print(f"[SUCCESS] Baseline successfully generated. Total files tracked: {len(baseline)}")
	return baseline
