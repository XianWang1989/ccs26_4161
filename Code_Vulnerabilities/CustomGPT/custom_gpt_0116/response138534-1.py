
from flask import Flask, redirect, url_for, flash
import config

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Process the deletion
    for eli in elis:
        r = eli.release()
        flash(f'Successfully deleted IP: {ip}')  # Optional: Flash a message

    # Redirect back to the list of Elastic IPs or the relevant page
    return redirect(url_for('elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def elastic_ips(region):
    # Your code to display the list of Elastic IPs for the region
    return "List of Elastic IPs for region: {}".format(region)
