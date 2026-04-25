
from flask import Flask, redirect, url_for, render_template
import json

app = Flask(__name__)

# Assuming your delete page also has the method to display all elastic IPs.
@app.route('/elastic_ips/<region>/delete/<ip>')
def delete_elastic_ip(region=None, ip=None):
    creds = config.get_ec2_conf()
    conn = connect_to_region(region, 
                             aws_access_key_id=creds['AWS_ACCESS_KEY_ID'], 
                             aws_secret_access_key=creds['AWS_SECRET_ACCESS_KEY'])
    ip = ip.encode('ascii')
    elis = conn.get_all_addresses(addresses=ip)

    # Perform the delete operation
    result = []
    for eli in elis:
        r = eli.release()
        result.append(r)

    # Redirect to the page that displays the elastic IPs after deletion
    return redirect(url_for('show_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def show_elastic_ips(region):
    # Logic to fetch and display elastic IPs in the specified region
    return render_template('elastic_ips.html', region=region)

if __name__ == '__main__':
    app.run(debug=True)
