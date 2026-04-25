
from flask import Flask, redirect, url_for, Response, jsonify
import json

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    for eli in elis:
        eli.release()

    return redirect(url_for('elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def elastic_ips(region):
    # Render your template or return your data
    return f"Elastic IPs for region: {region}"

if __name__ == '__main__':
    app.run(debug=True)
