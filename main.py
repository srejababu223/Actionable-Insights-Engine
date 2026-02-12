import time

# 1. THE DATA: Imagine this is coming from a live IoT sensor API
# We use a list of dictionaries to represent different assets (Trucks, Machines, etc.)
operational_data = [
    {"id": "Asset-01", "label": "Unit A", "is_active": True, "productivity_score": 0, "duration_min": 45},
    {"id": "Asset-02", "label": "Unit B", "is_active": True, "productivity_score": 85, "duration_min": 10},
    {"id": "Asset-03", "label": "Unit C", "is_active": True, "productivity_score": 0, "duration_min": 120}
]

# 2. THE BUSINESS VARIABLE: The cost of running an idle asset (e.g., fuel/electricity)
WASTAGE_FEE_PER_HOUR = 5.00 

print("📡 CONNECTING TO OPERATIONS GATEWAY...")
time.sleep(1) # Makes the demo feel real
print("✅ DATA RECEIVED. ANALYZING FOR INEFFICIENCIES...\n")

# 3. THE LOGIC ENGINE
for item in operational_data:
    # A 'Waste' event occurs if the asset is ON but doing 0 work
    if item["is_active"] and item["productivity_score"] == 0:
        loss = (item["duration_min"] / 60) * WASTAGE_FEE_PER_HOUR
        
        print(f"🚨 ALERT: {item['id']} ({item['label']})")
        print(f"   STATUS: Idling for {item['duration_min']} minutes.")
        print(f"   IMPACT: ${loss:.2f} lost in overhead.\n")
    else:
        print(f"✨ {item['id']}: Operating efficiently.\n")

print("--- DIAGNOSIS COMPLETE ---")