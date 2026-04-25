
from flask import Flask, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flashing messages

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

    # Flash a message after deletion
    flash(f'Successfully deleted IP: {ip}')

    # Redirect back to the desired route, e.g. a list of IPs
    return redirect(url_for('list_elastic_ips', region=region))

@app.route('/elastic_ips/<region>')
def list_elastic_ips(region):
    # Your logic to display the list of Elastic IPs for the given region
    return f'List of Elastic IPs in {region}'
