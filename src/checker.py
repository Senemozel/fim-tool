import os
import json
from datetime import datetime
from src.hasher import calculate_hash

BASELINE_FILE = "baseline/baseline.json"

def check_integrity(target_dir):
	if not os.path.exists(BASELINE_FILE):
		print("[ERROR] Baseline configuration not found. Please initialize the baseline first.")
		return
	with open(BASELINE_FILE, "r") as f:
		baseline = json.load(f)
	
	results = {
		"modified": [],
		"deleted": [],
		"new": [],
		"checked_at":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	}
	
	for file_path, info in baseline.items():
		if not os.path.exists(file_path):
			results["deleted"].append(file_path)
		else:
			current_hash = calculate_hash(file_path)
			if current_hash != info["hash"]:
				results["modified"].append({
					"file": file_path,
					"old_hash": info["hash"],
					"new_hash": current_hash
				})
	
	for root, dirs, files in os.walk(target_dir):
		for file_name in files:
			file_path = os.path.join(root, file_name)
			if file_path not in baseline:
				results["new"].append(file_path)
	
	print(f"\n[INTEGRITY REPORT] Generated at: {results['checked_at']}")
	print(f"  Modified files : {len(results['modified'])}")
	print(f"  Deleted files  : {len(results['deleted'])}")
	print(f"  New files      : {len(results['new'])}")

	if results["modified"]:
		print("\n  [!] Modified files detected:")
		for item in results["modified"]:
	    		print(f"      {item['file']}")

	if results["deleted"]:
		print("\n  [-] Missing/Deleted files:")
		for f in results["deleted"]:
	    		print(f"      {f}")

	if results["new"]:
		print("\n  [+] Newly added files:")
		for f in results["new"]:
			print(f"      {f}")

	return results
	
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
