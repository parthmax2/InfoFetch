from flask import Blueprint, render_template, request
from app.models.search import fetch_search_results
from app.models.summarize import fetch_and_summarize, fetch_and_summarize_from_text

routes = Blueprint('routes', __name__)

@routes.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        results = fetch_search_results(query)

        if not results or "organic" not in results:
            return render_template("index.html", error="No results found.")

        articles = results["organic"][:5]
        combined_text = ""
        detailed_articles = []
 
        for article in articles:
            url = article.get("link")
            title = article.get("title")
            summary = fetch_and_summarize(url)
            combined_text += summary + " "
            detailed_articles.append({"title": title, "url": url, "summary": summary})

        final_summary = fetch_and_summarize_from_text(combined_text)

        return render_template("results.html", summary=final_summary, articles=detailed_articles)

    return render_template("index.html")
