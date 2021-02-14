import concurrent.futures

import flask
from google.cloud import bigquery


app = flask.Flask(__name__)
bigquery_client = bigquery.Client()


@app.route("/")
def main():
    # Perform a query
    query_job = bigquery_client.query(
        """
        SELECT
        CONCAT(
            'https://storage.googleapis.com/books/ngrams/books/datasetsv2.html',
            CAST(id as STRING)) as url,
        view_count
        FROM `bigquery-public-data.words.eng_fiction_1gram`
        WHERE tags like '%google-bigquery%'
        ORDER BY view_count DESC
        LIMIT 100
    """
    ) # API request
    return flask.redirect(
        flask.url_for(
            "results",
            project_id=query_job.project,
            job_id=query_job.job_id,
            location=query_job.location,
        )
    )
@app.route("/results") # Waits for query to finish and displays results
def results():
    project_id = flask.request.args.get("project_id")
    job_id = flask.request.args.get("job_id")
    location = flask.request.args.get("location")
    query_job = bigquery_client.get_job(
        job_id,
        project=project_id,
        location=location,
    )
    try:
        # Set a timeout because queries could take longer than one minute.
        results = query_job.result(timeout=30)
    except concurrent.futures.TimeoutError:
        return flask.render_template("timeout.html", job_id=query_job.job_id)
    return flask.render_template("query_result.html", results=results)
if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
