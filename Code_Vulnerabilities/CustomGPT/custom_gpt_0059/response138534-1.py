
from flask import Flask, redirect, url_for, request, flash
import json

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        r = eli.release()  # Perform the deletion

    # Flash a message to indicate success (optional)
    flash(f'Successfully deleted IP: {ip.decode("ascii")}')

    # Redirect back to the page listing IPs or wherever you want
    return redirect(url_for('list_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # Your logic to display elastic IPs in the specified region
    return "List of Elastic IPs for region: " + region
