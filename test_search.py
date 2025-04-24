from app.models.search import fetch_search_results

query = input("what you wanna know about :").strip()
results = fetch_search_results(query)

if results:
    print("✅ Search Results Fetched Successfully!")
    for i, result in enumerate(results.get("organic", []), 1):  # Correct key access
        print(f"{i}. {result.get('title', 'No Title')} - {result.get('link', 'No Link')}")
else:
    print("❌ No results found!")
