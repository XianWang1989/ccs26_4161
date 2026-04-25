
from flask import Flask, redirect, url_for, flash
import json

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'],
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])

    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Flash a message to notify the user
    flash('Elastic IP deleted successfully!')

    # Redirect back to the overview page or another relevant route
    return redirect(url_for('elastic_ip_overview', region=region))

@app.route('/elastic_ips/<region>/overview')
def elastic_ip_overview(region):
    # This function would render the HTML page with the overview of elastic IPs
    return render_template('elastic_ip_overview.html', region=region)
