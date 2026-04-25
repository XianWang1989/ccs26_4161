
from flask import Flask, redirect, url_for, Response
import json

app = Flask(__name__)

@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, 
                             aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Redirect to the list of Elastic IPs after the deletion.
    # Here, we're assuming you have a route like '/elastic_ips/<region>'
    return redirect(url_for('list_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # Here you'd retrieve the list of Elastic IPs and render the page
    return "List of Elastic IPs in region: {}".format(region)

if __name__ == '__main__':
    app.run(debug=True)
