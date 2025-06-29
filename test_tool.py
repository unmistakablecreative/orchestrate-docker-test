import math

# --- Core Functions ---

def calculate_area(radius):
    area = math.pi * radius ** 2
    return {"area": area}

def calculate_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return {"volume": volume}

def sphere_surface_area(radius):
    surface_area = 4 * math.pi * radius ** 2
    return {"surface_area": surface_area}

# --- Action Router ---
def main():
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument("action")
    parser.add_argument("--params")
    args = parser.parse_args()
    params = json.loads(args.params) if args.params else {}
    if args.action == "calculate_area":
        result = calculate_area(**params)
    elif args.action == "calculate_volume":
        result = calculate_volume(**params)
    elif args.action == "sphere_surface_area":
        result = sphere_surface_area(**params)
    else:
        result = {"status": "error", "message": f"Unknown action {args.action}"}
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()