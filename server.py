from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)


@app.route("/static/<path>")
def _static(path):
	return send_from_directory('static', path)


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/account")
def account():
	posting_row = [
		{
			"date": "07/27",
			"title": "Accounting Refund Clerk",
			"location": "West Chester",
			"category": "Jobs"	
		},
		{
			"date": "07/26",
			"title": "Entry Level Trader: Trade with Firm's Capital",
			"location": "Philly/Remote",
			"category": "Jobs"
		}
	]
	return render_template("account.html", posting_row=posting_row, signed_in=True, category_not_selected=True)

@app.route("/sign_in", methods=["GET", "POST"])
def sign_in():
	error = ""
	if request.method == "POST":
		error = "Unable to log in at this time."

	return render_template("sign_in.html", error=error, category_not_selected=True)


@app.route("/login")
def login():
	posting_row = [
		{
			"date": "07/27",
			"title": "Accounting Refund Clerk",
			"location": "Center City",
			"compensation": "$20/hr"
		},
		{
			"date": "07/27",
			"title": "Business Analyst",
			"location": "Center City",
			"compensation": "$100k/yr"
		},
		{
			"date": "07/27",
			"title": "Part-time Bookkeeper",
			"location": "University City",
			"compensation": "Negotiable"
		},
		{
			"date": "07/27",
			"title": "Staff Accountant",
			"location": "University City"
		},
		{
			"date": "07/26",
			"title": "Part Time Accounting/Tax Filing",
			"location": "University City",
			"compensation": "$40/hr"
		},
		{
			"date": "07/26",
			"title": "Entry Level Trader: Trade with Firm's Capital",
			"location": "Philly/Remote",
			"compensation": "Negotiable"
		},
		{
			"date": "07/26",
			"title": "Compliance Associate",
			"location": "Philadelphia",
			"compensation": "Negotiable"
		},
		{
			"date": "07/26",
			"title": "Financial Coordinator",
			"location": "Philadelphia",
			"compensation": "$20/hr"
		},
		{
			"date": "07/25",
			"title": "Accounting Technical Lead",
			"location": "Philadelphia",
			"compensation": "$70k/yr"
		},
		{
			"date": "07/25",
			"title": "Tax Preaparer",
			"location": "Conshohocken",
			"compensation": "Negotiable"
		},
		{
			"date": "07/24",
			"title": "Finance Director",
			"location": "Malvern",
			"compensation": "Negotiable"
		},
		{
			"date": "07/24",
			"title": "Senior Accountant",
			"location": "Paoli",
			"compensation": "$50/hr"
		}
	]

	keyword = request.args.get("keyword", "")

	location = request.args.get("location", "")

	search_result = {
		"number": 132,
		"keyword": keyword,
		"location": location
	}

	return render_template("log_in.html", posting_row=posting_row, search_result=search_result, keyword=keyword, location=location)


if __name__ == "__main__":
	app.run(debug=True, port=9090)