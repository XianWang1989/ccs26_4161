
@app.route('/elastic_ips/<region>')
def your_view_function(region):
    # Logic to display IPs
    return render_template('your_template.html', region=region)
