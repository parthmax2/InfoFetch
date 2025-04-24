from app.models.summarize import fetch_and_summarize

url = input("🔗 Enter a URL to summarize: ")

summary = fetch_and_summarize(url)

print("\n✅ Summary Generated Successfully!\n")
print(summary)
