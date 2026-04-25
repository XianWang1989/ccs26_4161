
from flask import Flask, redirect, url_for, Response
import json

app = Flask(__name__)

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

    # Redirect to your desired route after deletion
    return redirect(url_for('your_redirect_view', region=region))

@app.route('/elastic_ips/<region>')
def your_redirect_view(region):
    # Here you can render the template that shows your list of elastic IPs or any other content
    return f"List of Elastic IPs in {region} (this should render your template)"
