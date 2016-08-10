from flask import Flask, render_template, send_from_directory

app = Flask(__name__)


@app.route("/static/<path>")
def _static(path):
	return send_from_directory('static', path)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/account")
def account():
	return render_template("account.html")


@app.route("/login")
def login():
	posting_row = [
		{
			"date": "07/27",
			"title": "Accounting Refund Clerk",
			"location": "Center City"
		},
		{
			"date": "07/27",
			"title": "Business Analyst",
			"location": "Center City"
		},
		{
			"date": "07/27",
			"title": "Part-time Bookkeeper",
			"location": "University City"
		},
		{
			"date": "07/27",
			"title": "Staff Accountant",
			"location": "University City"
		},
		{
			"date": "07/26",
			"title": "Part Time Accounting/Tax Filing",
			"location": "University City"
		},
		{
			"date": "07/26",
			"title": "Entry Level Trader: Trade with Firm's Capital",
			"location": "Philly/Remote"
		},
		{
			"date": "07/26",
			"title": "Compliance Associate",
			"location": "Philadelphia"
		},
		{
			"date": "07/26",
			"title": "Financial Coordinator",
			"location": "Philadelphia"
		},
		{
			"date": "07/25",
			"title": "Accounting Technical Lead",
			"location": "Philadelphia"
		},
		{
			"date": "07/25",
			"title": "Tax Preaparer",
			"location": "Conshohocken"
		},
		{
			"date": "07/24",
			"title": "Finance Director",
			"location": "Malvern"
		},
		{
			"date": "07/24",
			"title": "Senior Accountant",
			"location": "Paoli"
		}
	]

	search_result = {
		"number": 132,
		"keyword": "bookkeeping",
		"location": 19106
	}
	return render_template("log_in.html", posting_row=posting_row, search_result=search_result)


if __name__ == "__main__":
	app.run(debug=True, port=9090)