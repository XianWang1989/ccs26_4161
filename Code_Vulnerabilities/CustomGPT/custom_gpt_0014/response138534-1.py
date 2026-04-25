
from flask import Flask, redirect, url_for, Response
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

    # After deletion redirect to a specific page (e.g., list of Elastic IPs)
    return redirect(url_for('list_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # Logic to display list of Elastic IPs for the given region
    return "List of Elastic IPs for region: {}".format(region)

if __name__ == '__main__':
    app.run(debug=True)
