import json

# --- Core Functions ---

def hello_world():
    return {"message": "Hello, world!"}

def get_status():
    return {"status": "Blueprint ready"}

# --- Action Router ---
def main():
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument("action")
    parser.add_argument("--params")
    args = parser.parse_args()
    params = json.loads(args.params) if args.params else {}
    if args.action == "hello_world":
        result = hello_world(**params)
    elif args.action == "get_status":
        result = get_status(**params)
    else:
        result = {"status": "error", "message": f"Unknown action {args.action}"}
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()