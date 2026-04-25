
from flask import redirect, url_for, flash

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Flash a message to inform the user of the result
    flash("Elastic IP deleted successfully.")

    # Redirect to the page where the delete button is, or wherever you want
    return redirect(url_for('your_target_function', region=region))

# Make sure to include a route handler for 'your_target_function' as follows:
@app.route('/elastic_ips/<region>')
def your_target_function(region):
    # Logic to display elastic IPs or other relevant information
    return render_template('your_template.html', region=region)
